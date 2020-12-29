import socket
from http import HTTPStatus
from urllib.request import Request, urlopen, ProxyHandler, build_opener
from urllib.parse import urlencode, unquote_plus, quote, quote_plus
from urllib.error import HTTPError, URLError


class ClientBase:
    def __init__(self, nacos_host: str, api_level: str = 'v1'):
        self.host = nacos_host
        self.level = api_level
        self.base_url = f'{nacos_host}/nacos/{api_level}'

    def handle(self, url: str, headers: dict = {}, params: dict = {}, data: dict = {}, method: str = 'GET'):
        def _get_params_str():
            params_list = []
            for key in params.keys():
                value = params.get(key, None)
                if value is not None:
                    if not isinstance(value, str):
                        value = str(value)
                    params_list.append(f'{key}={quote_plus(value)}')
            return '&'.join(params_list)

        try:
            url += '?' + _get_params_str()
            req = Request(self.base_url + url, headers=headers, data=urlencode(data).encode(), method=method)
            resp = urlopen(req)
            response = resp.read()
            resp.close()
            return response
        except HTTPError as e:
            if e.code == HTTPStatus.FORBIDDEN:
                raise Exception("Insufficient privilege.")
            else:
                raise Exception(e)
        except socket.timeout:
            raise Exception(f"{self.host} request timeout")
        except URLError as e:
            raise Exception(f"{self.host} connection error:{e.reason}")
