## 运行

git clone https://github.com/ZhangYongChang/cytoflow.git
cd cytoflow/env
docker-compose up -d

Mysql 和 webapp 容器启动

前端是使用 nodejs 和 vue 框架开发 需要编译前端代码。

可以进入容器 执行命令编译也可本地编译

进入容器编译方案
docker exec -it 容器 ID /bin/bash
cd frontend

第一次编译需要初始化依赖库 npm install

让后执行 npm run build 可进行前端代码编译，在浏览器中默认绑定的本地主机端口为 8000
http://127.0.0.1:8000/

数据库刷新：
python3 manage.py makemigrations
python3 manage.py migrate
