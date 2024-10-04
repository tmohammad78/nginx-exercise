# Nginx exercise
This repo is to exercise nginx and know it better in simple version.

# Branches
I created some branches and in each branch you see a new folder with the name of the branch.

* [Hello World](https://github.com/tmohammad78/nginx-exercise/tree/01-hello-world)
* [Static Files](https://github.com/tmohammad78/nginx-exercise/tree/02-static-files)
* [Location Route](https://github.com/tmohammad78/nginx-exercise/tree/03-location-route)
* [Redirect Route](https://github.com/tmohammad78/nginx-exercise/tree/04-redirect-route)


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