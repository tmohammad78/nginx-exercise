# Nginx exercise
This repo is to exercise nginx and know it better in simple version.

# Branches
I created some branches and in each branch you see a new folder with the name of the branch.

* [Hello World](https://github.com/tmohammad78/nginx-exercise/tree/01-hello-world/hello-world)
* [Static Files](https://github.com/tmohammad78/nginx-exercise/tree/02-static-files/static-files)
* [Location Route](https://github.com/tmohammad78/nginx-exercise/tree/03-location-route/location-route)
* [Redirect Route](https://github.com/tmohammad78/nginx-exercise/tree/04-redirect-route/redirect-route)
* [Worker](https://github.com/tmohammad78/nginx-exercise/tree/05-worker/worker)
* [Cache](https://github.com/tmohammad78/nginx-exercise/tree/06-cache/cache)
* [Gzip](https://github.com/tmohammad78/nginx-exercise/tree/07-gzip/gzip)
* [Proxy](https://github.com/tmohammad78/nginx-exercise/tree/08-proxy/proxy)
* [Load Balance](https://github.com/tmohammad78/nginx-exercise/tree/09-load-balance/load-balance)
* [Rate Limit](https://github.com/tmohammad78/nginx-exercise/tree/main/rate-limit)
* [React Nginx](https://github.com/tmohammad78/nginx-exercise/tree/10-react-nginx/react-nginx)


# How to run
With docker commands you can do it:
You should have docker up in your system, then run this:
```
cd <name of project>
docker build -t nginx-hello-world:1.0 .

```

after you can run it

```
docker run -d -p 80:80 -p 8080:8080 nginx-hello-world:1.0
```

then check your localhost on the port.
easy peasy.

<b>For Load balance example see its doc</b>