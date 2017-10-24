import requests
from urllib.parse import urlparse
from core.database.database import Database

class Blacklists(object):
    def update(self,):
        self.db = Database()
        self.phishiTank()
        self.openPish()

    def phishiTank(self,):
        r = requests.get('http://data.phishtank.com/data/online-valid.csv')
        csvcontent = r.text.split('\n')
        urls = list()
        for i in range(1,len(csvcontent)-1):
            url = csvcontent[i].split(',')[1]
            urls.append({'url':url,'host':urlparse(url).netloc})
        self.db.bulkInsertBlacklist(urls)

    def openPish(self,):
        r = requests.get('https://openphish.com/feed.txt')
        feed = r.text.split('\n')
        urls = list()
        for url in feed:
            if url:
                url = url.strip()
                urls.append({'url':url,'host':urlparse(url).netloc})
        self.db.bulkInsertBlacklist(urls)
