import datetime
from threading import Thread
from twisted.web import proxy, http
from twisted.internet import reactor
from core.utils.parser import Parser
from core.utils.handler import Handler

class HouseProxy(proxy.Proxy):
    def dataReceived(self, request):
        try:
            headers,content = Parser(request.decode())
            url = content['resource']
            host = headers['Host']
            client_ip = str(self.transport.getPeer().host)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            useragent = headers['User-Agent']
            result = Handler(date,request,host,url,client_ip,useragent)
            if result == 'Safe':
                return proxy.Proxy.dataReceived(self, request)
            else:
                return proxy.Proxy.dataReceived(self, b'GET http://house.proxy:8000/redirect HTTP/1.1\r\nHost: house.proxy:8000\r\n\r\n')
        except Exception as e:
            pass

class ProxyFactory(http.HTTPFactory):
    protocol = HouseProxy

class Proxy(object):
    def startProxy(self,port=3128):
        factory = ProxyFactory()
        reactor.listenTCP(3128, factory)
        t1 = Thread(target=reactor.run, args=(False,)).start()
