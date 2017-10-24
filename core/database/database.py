import time
from core.database.models import models

class Database(object):
    def insertLog(self,date,host,url,client_ip,useragent,status):
        db = models()
        db.logs.insert(date=date,url=url,host=host,client_ip=client_ip,useragent=useragent,status=status)
        db.commit()

    def getAllLogs(self,):
        db = models()
        results = db().select(db.logs.ALL,orderby=~db.logs.id)
        return results

    def insertBlacklist(self,url,host):
        db = models()
        db.blacklists.update_or_insert(url=url,host=host)
        db.commit()

    def deleteBlacklist(self,bid):
        db = models()
        db(db.blacklists.id == bid).delete()
        db.commit()

    def bulkInsertBlacklist(self,blacklists):
        db = models()
        for bl in blacklists:
            db.blacklists.update_or_insert(url=bl['url'],host=bl['host'])
        db.commit()

    def getAllBlacklist(self,):
        db = models()
        results = db().select(db.blacklists.ALL,orderby=~db.blacklists.id)
        return results

    def checkBlacklist(self,host,url):
        db = models()
        result = db((db.blacklists.url == url) | (db.blacklists.host == host)).select()
        return len(result)
