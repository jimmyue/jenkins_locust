FROM locustio/locust:latest
MAINTAINER jimmy
user root 
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
