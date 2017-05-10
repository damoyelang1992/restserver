FROM python:2.7.13

RUN  mkdir /root/.pip
COPY ./pip.conf    /root/.pip/pip.conf
COPY ./src/requirements.txt    /opt/requirements.txt
COPY ./run.sh    /run.sh

RUN  chmod 755 /run.sh
RUN  pip install -r /opt/requirements.txt

# 这里是在Docker 虚拟机里面创建的路径
VOLUME ["/code"]

EXPOSE 5000

CMD  /run.sh
