from .base import ClientBase


class NameSpaceUtil:
    def __init__(self, client_base: ClientBase):
        self.client_base = client_base
        self.kwargs = {}

    def list(self):
        url = '/console/namespaces'
        response = self.client_base.handle(url, method='GET')
        return response

    def create(self, customNamespaceId: str, namespaceName: str, **kwargs):
        url = '/console/namespaces'
        kwargs['customNamespaceId'] = customNamespaceId
        kwargs['namespaceName'] = namespaceName
        self.kwargs = kwargs
        response = self.client_base.handle(url, data=self._get_data_dict(), method='POST')
        return response

    def edit(self, customNamespaceId: str, namespaceName: str, namespaceDesc: str, **kwargs):
        url = '/console/namespaces'
        kwargs['customNamespaceId'] = customNamespaceId
        kwargs['namespaceName'] = namespaceName
        kwargs['namespaceDesc'] = namespaceDesc
        self.kwargs = kwargs
        response = self.client_base.handle(url, data=self._get_data_dict(), method='PUT')
        return response

    def delete(self, namespaceId: str, **kwargs):
        url = '/console/namespaces'
        kwargs['namespaceId'] = namespaceId
        self.kwargs = kwargs
        response = self.client_base.handle(url, data=self._get_data_dict(), method='DELETE')
        return response

    def _get_params_dict(self):
        params_dict = {}
        params_dict.update(self.kwargs)
        return params_dict

    def _get_data_dict(self):
        data_dict = {}
        data_dict.update(self.kwargs)
        return data_dict
