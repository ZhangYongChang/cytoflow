FROM python:3.6

#设置源信息
RUN apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:chris-lea/node.js
RUN apt-get install git -y
RUN apt-get install wget -y

#后端
#COPY Django-2.2.5-py3-none-any.whl Django-2.2.5-py3-none-any.whl
#RUN pip3 install Django-2.2.5-py3-none-any.whl
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple django==2.2.5
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple mysqlclient
#COPY matplotlib-3.0.2-cp36-cp36m-manylinux1_x86_64.whl matplotlib-3.0.2-cp36-cp36m-manylinux1_x86_64.whl
#RUN pip3 install matplotlib-3.0.2-cp36-cp36m-manylinux1_x86_64.whl
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib==3.0.2
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple fcsparser

#前端
WORKDIR /build/tools
RUN wget https://cdn.npm.taobao.org/dist/node/v12.11.1/node-v12.11.1-linux-x64.tar.xz
RUN tar xf node-v12.11.1-linux-x64.tar.xz
RUN mv /build/tools/node-v12.11.1-linux-x64 /build/tools/nodejs 
RUN ln -s /build/tools/nodejs/bin/npm   /usr/local/bin/ 
RUN ln -s /build/tools/nodejs/bin/node   /usr/local/bin/

WORKDIR /build
RUN git clone https://github.com/ZhangYongChang/cytoflow.git
WORKDIR /build/cytoflow/frontend
RUN npm install --ignore-scripts
RUN npm install axios
RUN npm install echarts
RUN npm install echarts-stat

EXPOSE 8000
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak
RUN rm /etc/apt/sources.list
RUN echo "deb http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse\
  deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse\
  deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse\
  deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse\
  deb http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse\
  deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse\
  deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse\
  deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse\
  deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse\
  deb-src http://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse">/etc/apt/sources.list
RUN sudo apt-get update
RUN apt-get install vim -y