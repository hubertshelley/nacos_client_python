from .base import ClientBase
from .instance import InstanceUtil
from .namespace import NameSpaceUtil
from .service import ServiceUtil


class NacosClient:
    def __init__(self, nacos_host: str, nacos_port: int = None, api_level: str = 'v1'):
        if nacos_port:
            nacos_host = f'{nacos_host}:{nacos_port}'
        self.client_base = ClientBase(nacos_host, api_level)

    def instance(self):
        instance_util = InstanceUtil(self.client_base)
        return instance_util

    def namespace(self):
        namespace_util = NameSpaceUtil(self.client_base)
        return namespace_util

    def service(self):
        service_util = ServiceUtil(self.client_base)
        return service_util
