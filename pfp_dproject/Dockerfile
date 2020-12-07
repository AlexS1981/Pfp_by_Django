FROM ubuntu:20.10
ENV TZ=Europe
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
MAINTAINER Alex_VS "alex1449242@gmail.com"
WORKDIR .
COPY . .
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt
ENV NODE_ENV development
ENTRYPOINT [ "bash", "entrypoint.sh" ]
EXPOSE 8000
CMD ['python ', 'manage.py ', 'runserver ', '127.0.0.1:8000']