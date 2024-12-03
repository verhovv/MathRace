import { HTTP } from './common.js'

export const UserAPI = {
    register (config) {
        return HTTP.post('/register/', config).then(response => {
            return response.data
        })
    },
    login (config) {
        return HTTP.post('/login/', config).then(response => {
            return response.data
        })
    },
    logout (config) {
        return HTTP.post('/logout/', config).then(response => {
            return response.data
        })
    },
    profile () {
        return HTTP.get('/profile/', {headers}).then(response => {
            return response.data
        })
    }
}