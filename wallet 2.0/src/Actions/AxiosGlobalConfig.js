import React from 'react';
import axios from 'axios';
import { ROOT_URL } from './types';
axios.defaults.baseURL = localStorage.getItem('B_URL');
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token');
axios.defaults.headers.common['Cache-Control'] = 'no-cache';

let authTokenRequest;
function getAuthToken () {
    if (!authTokenRequest) {
        authTokenRequest = axios.post('/client/token', { 'address': localStorage.getItem('B_URL'), 'auth_code': localStorage.getItem('authcode') }).then((response) => {
            return response
        }).catch((error) => {
            return error
        });
        authTokenRequest.then(resetAuthTokenRequest, resetAuthTokenRequest).catch( err => { return err} )
    }
    return authTokenRequest
}


function resetAuthTokenRequest () {
    authTokenRequest = null
}

axios.interceptors.response.use(function (response) {
    return response
}, function (error) {

    if (error.response.status === 500) {
        console.log('ServerError globalconfig')
    }

    //expired refresh tokens
    if (error.response.data.description === 'Invalid payload padding') {
            localStorage.removeItem('token');
            localStorage.removeItem('refreshToken');
            return
    }

    // xs-token expired

    if (error.response.data.description === 'Signature has expired' && !error.response.config.__isRetryRequest) {
        return new Promise((resolve, reject) => {
            return getAuthToken().then((response) => {
                let data = JSON.stringify(response.data);
                data = JSON.parse(data);

                if (response.status === 200) {
                    localStorage.removeItem('access_token');
                    localStorage.setItem('access_token', data.token);
                    error.config.__isRetryRequest = true;
                    error.config.headers.Authorization = 'Bearer ' + data.token;
                    resolve(axios(error.config))
                }
            }).catch((error) => {
                reject(error)
            });
        });
    } else if(error.response.data.status === 'Signature verification failed') {
        localStorage.clear();
    }

    return Promise.reject(error)
});


export const axiosInstance = axios;