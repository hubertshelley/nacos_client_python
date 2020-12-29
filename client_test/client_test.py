import time

from nacos import NacosClient

client = NacosClient('192.168.222.128', nacos_port=8848)

# 注册服务
try:
    response = client.instance().register(ip='192.168.111.89', port=8080, serviceName='service.test',
                                          namespaceId='628da9e7-d34d-4e0c-b87e-118807ecca70', ephemeral=True)
    print('register', response)
except Exception as e:
    print(e.__str__())

time.sleep(2)
# 查询服务详情
try:
    response = client.instance().detail(ip='192.168.111.88', port=8080, serviceName='service.test',
                                        namespaceId='628da9e7-d34d-4e0c-b87e-118807ecca70')
    print('detail', response)
except Exception as e:
    print(e.__str__())

time.sleep(2)
# 自动心跳包
try:
    response = client.instance().auto_beat(ip='192.168.111.88', port=8080, serviceName='service.test',
                                           namespaceId='628da9e7-d34d-4e0c-b87e-118807ecca70')
    print('send_beat', response)
except Exception as e:
    print(e.__str__())

while True:
    time.sleep(2)
