# Gzip
We want to reduce size of files, we can use gzip directive in nginx, but pay attention that you should add header to see the redult of gzip.
if you want to see the result you can do it :

```
curl -I -H "Accept-Encoding: gzip" http://localhost:8080/react.js
```
and you will see 
```
HTTP/1.1 200 OK
Server: nginx/1.27.2
Date: Sat, 05 Oct 2024 08:26:37 GMT
Content-Type: application/javascript
Last-Modified: Sat, 05 Oct 2024 08:21:00 GMT
Connection: keep-alive
Vary: Accept-Encoding
ETag: W/"6700f6ec-1c774"
Expires: Mon, 04 Nov 2024 08:26:37 GMT
Cache-Control: max-age=2592000
Cache-Control: public
Pragma: public
Vary: Accept-Encoding
Content-Encoding: gzip
```

Now i you want to see the reult really in size of file you can do it:

```
curl http://localhost:8080/react.js > react-unzip.js
```

and 

```
curl -H "Accept-Encoding: gzip" http://localhost:8080/react.js > react-zip.js
```
so if you see the size of them you see unzip version is around <b>119 KB</b> and zip version is <b>33 KB</b>, <b>Nice!</b>.