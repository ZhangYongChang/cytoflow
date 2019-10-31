FROM centos:7.6.1810

WORKDIR /build/tools

RUN set -ex \
  && yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make wget vim git libXext libSM libXrender \
  && yum clean all

COPY *.tar.xz /build/tools/
RUN tar xf node-v12.11.1-linux-x64.tar.xz \
  && mv /build/tools/node-v12.11.1-linux-x64 /build/tools/nodejs \
  && ln -s /build/tools/nodejs/bin/npm   /usr/local/bin/ \
  && ln -s /build/tools/nodejs/bin/node   /usr/local/bin/ \
  && rm /build/tools/node-v12.11.1-linux-x64.tar.xz \
  && mkdir /usr/local/python3 \
  && tar -xvJf  Python-3.6.8.tar.xz && rm -f Python-3.6.8.tar.xz \
  && cd Python-3.6.8 \
  && ./configure prefix=/usr/local/python3 \
  && make && make install \
  && ln -s /usr/local/python3/bin/python3.6 /usr/local/bin/python3 \
  && ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3 \
  && cd .. \
  && rm -rf Python-3.6.8 \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple django==2.2.5 \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib==3.0.2 \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple fcsparser \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple cryptography \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pdfkit \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple django-cors-headers \
  && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple jinja2 \
  && tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
  && mv wkhtmltox/bin/wkhtmltopdf /usr/bin/wkhtmltopdf

COPY *.ttc /usr/share/fonts/
COPY *.py /usr/local/python3/lib/python3.6/site-packages/django/db/backends/mysql/

WORKDIR /build/cytoflow
EXPOSE 8000
