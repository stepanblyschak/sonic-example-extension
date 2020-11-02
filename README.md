# Example SONiC Application Extension

This repository contains an example SONiC compatible Docker image - a SONiC Package.

## Build

You need to have ```j2cli``` and ```docker``` installed.

To build SONiC Package:

```
$ make
```

In case you want to override version pass it as parameter to make:

```
$ make VERSION=1.0.0
```

## Publish via DockerHub

Login to your DockerHub user account using ```docker login``` command and push the image to your repository.

```
docker tag cpu-report:1.0.0 ${DOCKERHUB_USER}/cpu-report:1.0.0
docker push ${DOCKERHUB_USER}/cpu-report:1.0.0
```

## Install on the switch

Add repository entry to the database:

```
admin@sonic:~$ sudo sonic-package-manager repository add cpu-report \
    ${DOCKERHUB_USER}/cpu-report \
    --description="SONiC CPU report feature" \
    --default-reference=1.0.0
```

Install the package:

```
admin@sonic:~$ sudo sonic-package-manager install cpu-report
```
