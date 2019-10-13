FROM python:3.6

#设置源信息
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  software-properties-common \
  git \
  wget \
  vim \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple django==2.2.5 \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib==3.0.2 \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple fcsparser \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql \
  && pip3 install cryptography

COPY *.py /usr/local/lib/python3.6/site-packages/django/db/backends/mysql/

#前端
WORKDIR /build/tools
COPY node-v12.11.1-linux-x64.tar.xz /build/tools/node-v12.11.1-linux-x64.tar.xz
RUN tar xf node-v12.11.1-linux-x64.tar.xz \
  && mv /build/tools/node-v12.11.1-linux-x64 /build/tools/nodejs \
  && ln -s /build/tools/nodejs/bin/npm   /usr/local/bin/ \
  && ln -s /build/tools/nodejs/bin/node   /usr/local/bin/

RUN pip3 install django-cors-headers

WORKDIR /build/cytoflow

EXPOSE 8000