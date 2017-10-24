import hug
from threading import Thread
from core.proxy.houseProxy import Proxy
from core.utils.templates import get_template
from core.database.database import Database
from core.utils.blacklists import Blacklists

print("Starting the proxy service...")
Proxy().startProxy()
print("Proxy service started!")

user,passwd = open('etc/HouseProxy.conf').read().split(':')
admin_area = hug.http(requires=hug.authentication.basic(hug.authentication.verify(user.strip(), passwd.strip())))

@hug.get('/redirect',output=hug.output_format.html)
def blocked():
    return "<script>document.location= 'http://house.proxy:8000/blocked'</script>"

@hug.get('/blocked',output=hug.output_format.html)
def blocked():
    template = get_template('blocked.html')
    return template.render()

@admin_area.get('/',output=hug.output_format.html)
def index():
    db = Database()
    totalRequests = len(db.getAllLogs())
    totalBlacklists = len(db.getAllBlacklist())

    template = get_template('index.html')
    return template.render({"total_requests":totalRequests,'total_blacklists':totalBlacklists})

@admin_area.get('/blacklists/',output=hug.output_format.html)
def blacklistsUpdate():
    db = Database()
    blacklists =  db.getAllBlacklist()
    template = get_template('blacklists.html')
    return template.render({"blacklists":blacklists,"total":len(blacklists)})

@admin_area.get('/blacklists/update',output=hug.output_format.html)
def blacklistsUpdate():
    bl = Blacklists()
    Thread(target=bl.update, args=()).start()
    template = get_template('updateBlacklist.html')
    return template.render()


@admin_area.get('/blacklists/delete/{bid}',output=hug.output_format.html)
def blacklistsDelete(bid):
    db = Database()
    db.deleteBlacklist(bid)
    return hug.redirect.to('/blacklists')

@admin_area.get('/logs',output=hug.output_format.html)
def logs():
    db = Database()
    allLogs = db.getAllLogs()
    template = get_template('logs.html')
    return template.render({"logs":allLogs})

@hug.static('/static')
def my_static_dirs():
    return('static/',)
