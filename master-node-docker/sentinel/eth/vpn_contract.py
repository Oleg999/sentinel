# coding=utf-8
import rlp
from ethereum.transactions import Transaction

from .eth import rinkeby
from ..config import COINBASE_PRIVATE_KEY
from ..config import MAX_TX_TRY
from ..config import VPNSERVICE_ABI
from ..config import VPNSERVICE_ADDRESS
from ..config import VPNSERVICE_NAME


class VpnServiceManager(object):
    def __init__(self):
        self.contract = rinkeby.web3.eth.contract(contract_name=VPNSERVICE_NAME, abi=VPNSERVICE_ABI,
                                                  address=VPNSERVICE_ADDRESS)

    def pay_vpn_session(self, account_addr, amount, session_id, nonce):
        count = 0
        while count < MAX_TX_TRY:
            try:
                tx = Transaction(nonce=nonce + count,
                                 gasprice=rinkeby.web3.eth.gasPrice,
                                 startgas=1000000,
                                 to=VPNSERVICE_ADDRESS,
                                 value=0,
                                 data=rinkeby.web3.toBytes(hexstr=self.contract.encodeABI(fn_name='payVpnSession',
                                                                                          args=[account_addr, amount,
                                                                                                session_id])))
                tx.sign(COINBASE_PRIVATE_KEY)
                raw_tx = rinkeby.web3.toHex(rlp.encode(tx))
                tx_hash = rinkeby.web3.eth.sendRawTransaction(raw_tx)
                if len(tx_hash) > 0:
                    break
            except Exception as err:
                err = str(err)
                if '-32000' in err:
                    count = count + 1
                if (count >= MAX_TX_TRY) or ('-32000' not in err):
                    return {'code': 301, 'error': err}, None
        return None, tx_hash

    def set_initial_payment(self, account_addr, nonce, is_paid=True):
        count = 0
        while count < MAX_TX_TRY:
            try:
                tx = Transaction(nonce=nonce + count,
                                 gasprice=rinkeby.web3.eth.gasPrice,
                                 startgas=1000000,
                                 to=VPNSERVICE_ADDRESS,
                                 value=0,
                                 data=rinkeby.web3.toBytes(
                                     hexstr=self.contract.encodeABI(fn_name='setInitialPaymentStatusOf',
                                                                    args=[account_addr, is_paid])))
                tx.sign(COINBASE_PRIVATE_KEY)
                raw_tx = rinkeby.web3.toHex(rlp.encode(tx))
                tx_hash = rinkeby.web3.eth.sendRawTransaction(raw_tx)
                if len(tx_hash) > 0:
                    break
            except Exception as err:
                err = str(err)
                if '-32000' in err:
                    count = count + 1
                if (count >= MAX_TX_TRY) or ('-32000' not in err):
                    return {'code': 302, 'error': err}, None
        return None, tx_hash

    def get_due_amount(self, account_addr):
        try:
            caller_object = {
                'from': account_addr,
                'to': VPNSERVICE_ADDRESS,
                'data': rinkeby.web3.toHex(
                    rinkeby.web3.toBytes(hexstr=self.contract.encodeABI(fn_name='getDueAmountOf', args=[account_addr])))
            }
            due_amount = rinkeby.web3.toInt(hexstr=rinkeby.web3.eth.call(caller_object))
        except Exception as err:
            return {'code': 303, 'error': str(err)}, None
        return None, due_amount

    def get_vpn_sessions_count(self, account_addr):
        try:
            caller_object = {
                'from': account_addr,
                'to': VPNSERVICE_ADDRESS,
                'data': rinkeby.web3.toHex(rinkeby.web3.toBytes(
                    hexstr=self.contract.encodeABI(fn_name='getVpnSessionsCountOf', args=[account_addr])))
            }
            sessions_count = rinkeby.web3.toInt(hexstr=rinkeby.web3.eth.call(caller_object))
        except Exception as err:
            return {'code': 304, 'error': str(err)}, None
        return None, sessions_count

    def get_initial_payment(self, account_addr):
        try:
            caller_object = {
                'from': account_addr,
                'to': VPNSERVICE_ADDRESS,
                'data': rinkeby.web3.toHex(rinkeby.web3.toBytes(
                    hexstr=self.contract.encodeABI(fn_name='getInitialPaymentStatusOf', args=[account_addr])))
            }
            is_paid = rinkeby.web3.toInt(hexstr=rinkeby.web3.eth.call(caller_object))
        except Exception as err:
            return {'code': 305, 'error': str(err)}, None
        return None, is_paid == 1

    def get_vpn_usage(self, account_addr, session_id):
        try:
            caller_object = {
                'from': account_addr,
                'to': VPNSERVICE_ADDRESS,
                'data': rinkeby.web3.toHex(rinkeby.web3.toBytes(
                    hexstr=self.contract.encodeABI(fn_name='getVpnUsageOf', args=[account_addr, session_id])))
            }
            usage = rinkeby.web3.eth.call(caller_object)[2:]
            usage = [usage[i:i + 64] for i in range(0, len(usage), 64)]
            usage[0] = rinkeby.web3.toChecksumAddress(usage[0])
            usage[1:] = [rinkeby.web3.toInt(hexstr=usage[i]) for i in range(1, len(usage))]
            usage[-1] = usage[-1] != 0
        except Exception as err:
            return {'code': 306, 'error': str(err)}, None
        return None, usage

    def add_vpn_usage(self, from_addr, to_addr, sent_bytes, session_duration, amount, timestamp, session_id, nonce):
        count = 0
        while count < MAX_TX_TRY:
            try:
                tx = Transaction(nonce=nonce + count,
                                 gasprice=rinkeby.web3.eth.gasPrice,
                                 startgas=1000000,
                                 to=VPNSERVICE_ADDRESS,
                                 value=0,
                                 data=rinkeby.web3.toBytes(hexstr=self.contract.encodeABI(fn_name='addVpnUsage',
                                                                                          args=[from_addr, to_addr,
                                                                                                sent_bytes,
                                                                                                session_duration,
                                                                                                amount,
                                                                                                timestamp,
                                                                                                session_id])))
                tx.sign(COINBASE_PRIVATE_KEY)
                raw_tx = rinkeby.web3.toHex(rlp.encode(tx))
                tx_hash = rinkeby.web3.eth.sendRawTransaction(raw_tx)
                if len(tx_hash) > 0:
                    break
            except Exception as err:
                err = str(err)
                if '-32000' in err:
                    count = count + 1
                if (count >= MAX_TX_TRY) or ('-32000' not in err):
                    return {'code': 307, 'error': err}, None
        return None, tx_hash


vpn_service_manager = VpnServiceManager()
