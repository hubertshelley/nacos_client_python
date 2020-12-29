import json
import threading
import time

from .base import ClientBase


class InstanceUtil:
    def __init__(self, client_base: ClientBase):
        self.client_base = client_base
        self.ip = None
        self.port = None
        self.serviceName = None
        self.kwargs = {}
        self.beat = None
        self.is_auto_beat = True

    def register(self, ip: str, port: int, serviceName: str, **kwargs):
        self.ip = ip
        self.port = port
        self.serviceName = serviceName
        self.kwargs = kwargs
        url = '/ns/instance'
        response = self.client_base.handle(url, params=self._get_params_dict(), method='POST')
        return response

    def delete(self, ip: str, port: int, serviceName: str, **kwargs):
        self.ip = ip
        self.port = port
        self.serviceName = serviceName
        self.kwargs = kwargs
        url = '/ns/instance'
        response = self.client_base.handle(url, params=self._get_params_dict(), method='DELETE')
        return response

    def edit(self, ip: str, port: int, serviceName: str, **kwargs):
        self.ip = ip
        self.port = port
        self.serviceName = serviceName
        self.kwargs = kwargs
        url = '/ns/instance'
        response = self.client_base.handle(url, params=self._get_params_dict(), method='PUT')
        return response

    def list(self, serviceName: str, **kwargs):
        self.serviceName = serviceName
        self.kwargs = kwargs
        url = '/ns/instance/list'
        response = self.client_base.handle(url, params=self._get_params_dict(), method='GET')
        return response

    def detail(self, ip: str, port: int, serviceName: str, **kwargs):
        self.ip = ip
        self.port = port
        self.serviceName = serviceName
        self.kwargs = kwargs
        if not kwargs.get('groupName'):
            self.kwargs['groupName'] = 'DEFAULT_GROUP'
        url = '/ns/instance'
        response = self.client_base.handle(url, params=self._get_params_dict(), method='GET')
        self.beat = response
        return response

    def send_beat(self, ip: str, port: int, serviceName: str, **kwargs):
        self.ip = ip
        self.port = port
        self.serviceName = serviceName
        self.kwargs = kwargs
        beat_data = {
            "serviceName": serviceName,
            "ip": ip,
            "port": port
        }
        beat_data.update(kwargs)
        params = self._get_params_dict()
        params['beat'] = json.dumps(beat_data)
        url = '/ns/instance/beat'
        response = self.client_base.handle(url, params=params, method='PUT')
        return response

    def auto_beat(self, ip: str, port: int, serviceName: str, **kwargs):
        def beat():
            def heart_beat():
                try:
                    response = self.send_beat(ip, port, serviceName, **kwargs)
                    # print(f'beat response:{response}')
                except Exception as e:
                    print(f'beat exception:{e.__str__()}')

            while self.is_auto_beat:
                heart_beat()
                time.sleep(4)

        _beat_thread = threading.Thread(target=beat)
        _beat_thread.setDaemon(True)
        _beat_thread.start()

    def set_healthy(self, ip: str, port: int, serviceName: str, healthy: bool, **kwargs):
        self.ip = ip
        self.port = port
        self.serviceName = serviceName
        self.kwargs = kwargs
        self.kwargs['healthy'] = healthy
        url = '/ns/instance/list'
        response = self.client_base.handle(url, params=self._get_params_dict(), method='PUT')
        return response

    def _get_params_dict(self):
        params_dict = {
            'ip': self.ip,
            'port': self.port,
            'serviceName': self.serviceName,
        }
        params_dict.update(self.kwargs)
        return params_dict

    def _get_data_dict(self):
        data_dict = {
            'ip': self.ip,
            'port': self.port,
            'serviceName': self.serviceName,
        }
        data_dict.update(self.kwargs)
        return data_dict
