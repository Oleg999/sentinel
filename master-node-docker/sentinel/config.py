# coding=utf-8
false, true = False, True
SENTINEL_ABI = [
    {"constant": true, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": false, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}],
     "name": "approve", "outputs": [{"name": "success", "type": "bool"}], "payable": false,
     "stateMutability": "nonpayable", "type": "function"},
    {"constant": true, "inputs": [{"name": "", "type": "bytes32"}], "name": "services",
     "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}],
     "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false,
                                                                        "inputs": [{"name": "_from", "type": "address"},
                                                                                   {"name": "_to", "type": "address"},
                                                                                   {"name": "_value",
                                                                                    "type": "uint256"}],
                                                                        "name": "transferFrom", "outputs": [
            {"name": "success", "type": "bool"}], "payable": false, "stateMutability": "nonpayable",
                                                                        "type": "function"},
    {"constant": true, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": false, "inputs": [{"name": "_value", "type": "uint256"}], "name": "burn",
     "outputs": [{"name": "success", "type": "bool"}], "payable": false, "stateMutability": "nonpayable",
     "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "address"}], "name": "balanceOf",
                           "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view",
                           "type": "function"},
    {"constant": false, "inputs": [{"name": "_from", "type": "address"}, {"name": "_value", "type": "uint256"}],
     "name": "burnFrom", "outputs": [{"name": "success", "type": "bool"}], "payable": false,
     "stateMutability": "nonpayable", "type": "function"}, {"constant": false,
                                                            "inputs": [{"name": "_serviceName", "type": "bytes32"},
                                                                       {"name": "_from", "type": "address"},
                                                                       {"name": "_to", "type": "address"},
                                                                       {"name": "_value", "type": "uint256"}],
                                                            "name": "payService", "outputs": [], "payable": false,
                                                            "stateMutability": "nonpayable", "type": "function"},
    {"constant": true, "inputs": [], "name": "owner", "outputs": [{"name": "", "type": "address"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": false, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
     "name": "transfer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"},
    {"constant": false, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"},
                                   {"name": "_extraData", "type": "bytes"}], "name": "approveAndCall",
     "outputs": [{"name": "success", "type": "bool"}], "payable": false, "stateMutability": "nonpayable",
     "type": "function"},
    {"constant": true, "inputs": [{"name": "", "type": "address"}, {"name": "", "type": "address"}],
     "name": "allowance", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view",
     "type": "function"},
    {"constant": false, "inputs": [{"name": "_owner", "type": "address"}], "name": "transferOwnership", "outputs": [],
     "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [
        {"name": "_serviceName", "type": "bytes32"}, {"name": "_serviceAddress", "type": "address"}],
                                                                              "name": "deployService", "outputs": [],
                                                                              "payable": false,
                                                                              "stateMutability": "nonpayable",
                                                                              "type": "function"}, {
        "inputs": [{"name": "_tokenName", "type": "string"}, {"name": "_tokenSymbol", "type": "string"},
                   {"name": "_decimals", "type": "uint8"}, {"name": "_totalSupply", "type": "uint256"}],
        "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [
        {"indexed": true, "name": "from", "type": "address"}, {"indexed": true, "name": "to", "type": "address"},
        {"indexed": false, "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"},
    {"anonymous": false, "inputs": [{"indexed": true, "name": "from", "type": "address"},
                                    {"indexed": false, "name": "value", "type": "uint256"}], "name": "Burn",
     "type": "event"}]
SENTINEL_ADDRESS = '0xa44E5137293E855B1b7bC7E2C6f8cD796fFCB037'
SENTINEL_NAME = 'Sentinel'
SENTINEL_TEST_ABI = [
    {"constant": true, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": false, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}],
     "name": "approve", "outputs": [{"name": "success", "type": "bool"}], "payable": false,
     "stateMutability": "nonpayable", "type": "function"},
    {"constant": true, "inputs": [{"name": "", "type": "bytes32"}], "name": "services",
     "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}],
     "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false,
                                                                        "inputs": [{"name": "_from", "type": "address"},
                                                                                   {"name": "_to", "type": "address"},
                                                                                   {"name": "_value",
                                                                                    "type": "uint256"}],
                                                                        "name": "transferFrom", "outputs": [
            {"name": "success", "type": "bool"}], "payable": false, "stateMutability": "nonpayable",
                                                                        "type": "function"},
    {"constant": true, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": false, "inputs": [{"name": "_value", "type": "uint256"}], "name": "burn",
     "outputs": [{"name": "success", "type": "bool"}], "payable": false, "stateMutability": "nonpayable",
     "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "address"}], "name": "balanceOf",
                           "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view",
                           "type": "function"},
    {"constant": false, "inputs": [{"name": "_from", "type": "address"}, {"name": "_value", "type": "uint256"}],
     "name": "burnFrom", "outputs": [{"name": "success", "type": "bool"}], "payable": false,
     "stateMutability": "nonpayable", "type": "function"}, {"constant": false,
                                                            "inputs": [{"name": "_serviceName", "type": "bytes32"},
                                                                       {"name": "_from", "type": "address"},
                                                                       {"name": "_to", "type": "address"},
                                                                       {"name": "_value", "type": "uint256"}],
                                                            "name": "payService", "outputs": [], "payable": false,
                                                            "stateMutability": "nonpayable", "type": "function"},
    {"constant": true, "inputs": [], "name": "owner", "outputs": [{"name": "", "type": "address"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": false, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
     "name": "transfer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"},
    {"constant": false, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"},
                                   {"name": "_extraData", "type": "bytes"}], "name": "approveAndCall",
     "outputs": [{"name": "success", "type": "bool"}], "payable": false, "stateMutability": "nonpayable",
     "type": "function"},
    {"constant": true, "inputs": [{"name": "", "type": "address"}, {"name": "", "type": "address"}],
     "name": "allowance", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view",
     "type": "function"},
    {"constant": false, "inputs": [{"name": "_owner", "type": "address"}], "name": "transferOwnership", "outputs": [],
     "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [
        {"name": "_serviceName", "type": "bytes32"}, {"name": "_serviceAddress", "type": "address"}],
                                                                              "name": "deployService", "outputs": [],
                                                                              "payable": false,
                                                                              "stateMutability": "nonpayable",
                                                                              "type": "function"}, {
        "inputs": [{"name": "_tokenName", "type": "string"}, {"name": "_tokenSymbol", "type": "string"},
                   {"name": "_decimals", "type": "uint8"}, {"name": "_totalSupply", "type": "uint256"}],
        "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [
        {"indexed": true, "name": "from", "type": "address"}, {"indexed": true, "name": "to", "type": "address"},
        {"indexed": false, "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"},
    {"anonymous": false, "inputs": [{"indexed": true, "name": "from", "type": "address"},
                                    {"indexed": false, "name": "value", "type": "uint256"}], "name": "Burn",
     "type": "event"}]
SENTINEL_TEST_ADDRESS = '0x29317B796510afC25794E511e7B10659Ca18048B'
SENTINEL_TEST_NAME = 'Sentinel Test Token'
VPNSERVICE_ABI = [
    {"constant": false, "inputs": [{"name": "_addr", "type": "address"}], "name": "addAuthorizedUser", "outputs": [],
     "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [
        {"name": "_from", "type": "address"}, {"name": "_to", "type": "address"},
        {"name": "_receivedBytes", "type": "uint256"}, {"name": "_sessionDuration", "type": "uint256"},
        {"name": "_amount", "type": "uint256"}, {"name": "_timestamp", "type": "uint256"},
        {"name": "_sessionId", "type": "bytes32"}], "name": "addVpnUsage", "outputs": [], "payable": false,
                                                                              "stateMutability": "nonpayable",
                                                                              "type": "function"}, {"constant": false,
                                                                                                    "inputs": [{
                                                                                                        "name": "_from",
                                                                                                        "type": "address"},
                                                                                                        {
                                                                                                            "name": "_amount",
                                                                                                            "type": "uint256"},
                                                                                                        {
                                                                                                            "name": "_sessionId",
                                                                                                            "type": "bytes32"}],
                                                                                                    "name": "payVpnSession",
                                                                                                    "outputs": [],
                                                                                                    "payable": false,
                                                                                                    "stateMutability": "nonpayable",
                                                                                                    "type": "function"},
    {"constant": false, "inputs": [{"name": "_addr", "type": "address"}], "name": "removeAuthorizedUser", "outputs": [],
     "payable": false, "stateMutability": "nonpayable", "type": "function"},
    {"constant": false, "inputs": [{"name": "_addr", "type": "address"}, {"name": "_isPaid", "type": "bool"}],
     "name": "setInitialPaymentStatusOf", "outputs": [], "payable": false, "stateMutability": "nonpayable",
     "type": "function"},
    {"constant": false, "inputs": [{"name": "_owner", "type": "address"}], "name": "transferOwnership", "outputs": [],
     "payable": false, "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor"},
    {"constant": true, "inputs": [{"name": "", "type": "address"}], "name": "authorizedUsers",
     "outputs": [{"name": "", "type": "bool"}], "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [{"name": "_address", "type": "address"}], "name": "getDueAmountOf",
     "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [{"name": "_addr", "type": "address"}], "name": "getInitialPaymentStatusOf",
     "outputs": [{"name": "", "type": "bool"}], "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [{"name": "_address", "type": "address"}], "name": "getVpnSessionsCountOf",
     "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [{"name": "_address", "type": "address"}, {"name": "_sessionId", "type": "bytes32"}],
     "name": "getVpnUsageOf",
     "outputs": [{"name": "", "type": "address"}, {"name": "", "type": "uint256"}, {"name": "", "type": "uint256"},
                 {"name": "", "type": "uint256"}, {"name": "", "type": "uint256"}, {"name": "", "type": "bool"}],
     "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [], "name": "owner", "outputs": [{"name": "", "type": "address"}], "payable": false,
     "stateMutability": "view", "type": "function"}]
VPNSERVICE_ADDRESS = '0x86c592a4Ab2De10D8F1Ad3AD91e40BD676F559f2'
VPNSERVICE_NAME = 'Vpn_service'
COINBASE_ADDRESS = '0xA3F1592D8a09a91a7238f608620fFDe7C4B26029'
COINBASE_PRIVATE_KEY = ''
CENTRAL_WALLET = ''
CENTRAL_WALLET_PRIVATE_KEY = ''
MAX_TX_TRY = 60
DECIMALS = (10 ** 8) * 1.0
LIMIT_10MB = 10 * 1024 * 1024
LIMIT_100MB = 100 * 1024 * 1024
SESSIONS_SALT = ''.encode('utf-8')
