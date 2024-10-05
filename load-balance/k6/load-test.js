import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    vus: 50,      
    duration: '1m', 
};

export default function () {
    http.get('http://nginx:80/'); 
    sleep(1);
}
