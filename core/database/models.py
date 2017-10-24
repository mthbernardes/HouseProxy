from pydal import DAL, Field

class models(object):
    def __new__(self,):
        #dalString  = 'mongodb://localhost/HomeProxy' #uncomment to use mongodb
        dalString  = 'sqlite://HomeProxy.db'  #uncomment to use sqlite
        db = DAL(dalString,migrate=True)
        db.define_table('logs',
            Field('date'),
            Field('url'),
            Field('client_ip'),
            Field('useragent'),
            Field('status'),
            Field('host'))
        db.define_table('blacklists',
            Field('url'),
            Field('host'))
        return db
