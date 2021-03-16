# nacos_client_python

#### 介绍
服务于**nacos**的自动化服务注册插件

#### 软件架构
推荐使用py3.7或以上环境使用  
基本上是模块化的Nacos open-api,使用参数与open-api一致。 
并提供了nacos实例的自动心跳包功能


#### 安装教程
源码安装
```
git clone https://gitee.com/hubert22/nacos_client_python.git
cd nacos_client_python
python setup.py install
```

#### 使用说明

请参照client_test运行

或参照
```python
import threading
import time

import uvicorn
from nacos import NacosClient


def regis_server_to_nacos(service_ip, port, service_name, namespaceId):
    """
    注册服务到nacos
    """
    nacos_client = NacosClient('hostname')
    # 注册服务
    try:
        response = nacos_client.instance().register(ip=service_ip, port=port, serviceName=service_name,
                                                    namespaceId=namespaceId, ephemeral=True)
        print('register', response)
    except Exception as e:
        print(e.__str__())
    # 自动心跳包
    try:
        response = nacos_client.instance().auto_beat(ip=service_ip, port=port, serviceName=service_name,
                                                     namespaceId=namespaceId)
        print('send_beat', response)
    except Exception as e:
        print(e.__str__())


if __name__ == '__main__':
    # 运行服务器地址
    service_ip = '192.168.111.89'
    # 运行服务名称
    service_name = 'service.test'
    # 命名空间ID
    namespaceId = 'd479f2e8-62af-47a0-af66-70be48f15080'
    # 运行服务器运行端口
    port = 9014
    regis_server_to_nacos(service_ip, port, service_name, namespaceId)
    # uvicorn运行django程序
    uvicorn.run("hikvim_oa.asgi:application", host="0.0.0.0", port=port, log_level="info", reload=True)

```

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
