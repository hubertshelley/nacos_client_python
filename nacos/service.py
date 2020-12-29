from .base import ClientBase


class ServiceUtil:
    def __init__(self, client_base: ClientBase):
        self.client_base = client_base
        self.kwargs = {}

    def create(self, serviceName: str, **kwargs):
        url = '/ns/service'
        kwargs['serviceName'] = serviceName
        self.kwargs = kwargs
        response = self.client_base.handle(url, params=self._get_params_dict(), method='POST')
        return response

    def delete(self, serviceName: str, **kwargs):
        url = '/ns/service'
        kwargs['serviceName'] = serviceName
        self.kwargs = kwargs
        response = self.client_base.handle(url, params=self._get_params_dict(), method='DELETE')
        return response

    def edit(self, serviceName: str, **kwargs):
        url = '/ns/service'
        kwargs['serviceName'] = serviceName
        self.kwargs = kwargs
        response = self.client_base.handle(url, params=self._get_params_dict(), method='PUT')
        return response

    def detail(self, serviceName: str, **kwargs):
        url = '/ns/service'
        kwargs['serviceName'] = serviceName
        self.kwargs = kwargs
        response = self.client_base.handle(url, params=self._get_params_dict(), method='GET')
        return response

    def list(self, pageNo: int, pageSize: int, **kwargs):
        url = '/ns/service/list'
        kwargs['pageNo'] = pageNo
        kwargs['pageSize'] = pageSize
        self.kwargs = kwargs
        response = self.client_base.handle(url, params=self._get_params_dict(), method='GET')
        return response

    def _get_params_dict(self):
        params_dict = {}
        params_dict.update(self.kwargs)
        return params_dict

    def _get_data_dict(self):
        data_dict = {}
        data_dict.update(self.kwargs)
        return data_dict
