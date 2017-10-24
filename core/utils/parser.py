import re

class Parser(object):
    def __new__(self,http_request):
        req_line = re.compile(r'(?P<method>GET|POST|OPTIONS|DELETE|PUT|CONNECT|HEAD|TRACE|PATCH)\s+(?P<resource>.+?)\s+(?P<version>HTTP/1.1)')
        field_line = re.compile(r'\s*(?P<key>.+\S)\s*:\s+(?P<value>.+\S)\s*')
        first_line_end = http_request.find('\n')
        headers_end = http_request.find('\n\n')
        request = req_line.match(
            http_request[:first_line_end]
        ).groupdict()
        headers = dict(
            field_line.findall(
                http_request[first_line_end:headers_end]
            )
        )
        body = http_request[headers_end + 2:]
        return headers,request
