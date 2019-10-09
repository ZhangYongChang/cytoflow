FROM python:3.6

#设置源信息
RUN apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:chris-lea/node.js
RUN apt-get install git -y
RUN apt-get install wget -y

#后端
RUN pip3 install django==2.2.5
RUN pip3 install mysqlclient
RUN pip3 install matplotlib==3.0.2
RUN pip3 install fcsparser

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