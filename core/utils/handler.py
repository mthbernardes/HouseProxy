import requests
from threading import Thread
from core.database.database import Database

class Handler(object):
    def __new__(self,date,request,host,url,client_ip,useragent):
        db = Database()
        status = 'Safe'
        result = db.checkBlacklist(host,url)
        if result:
            status = 'Unsafe'
        else:
            pass
            #t1 = Thread(target=self.checkAgain, name="checkAgain", args=(self,url,host,))
            #t1.start()
        db.insertLog(date=date,url=url,host=host,client_ip=client_ip,useragent=useragent,status=status)
        return status

    def checkAgain(self,url,host):
        results = list()
        results.append(self.globaSiteSafety(self,url))
        if True in results:
            db = Database()
            db.insertBlacklist(url,host)

    def globaSiteSafety(self,malicious_url):
        #Get cookies
        url = 'https://global.sitesafety.trendmicro.com/'
        r = requests.get(url)
        cookies = r.cookies
        #Get result
        url = 'https://global.sitesafety.trendmicro.com/result.php'
        data = {'urlname':malicious_url,'getinfo':'Check Now'}
        r = requests.post(url,data=data,cookies=cookies)
        return 'Dangerous' in r.text
