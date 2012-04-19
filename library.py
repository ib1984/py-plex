from section import Section

class Library(object):
    def __init__(self, server):
        self.server = server
    
    def __str__(self):
        return "<Library: %s>" % server
    
    def __repr__(self):
        return "<Library: %s>" % server
    
    
    @property
    def sections(self):
        elem = self.server.query("/library/sections")
        seclist = [Section(e.attrib['title'], e.attrib['key'], self.server) for e in elem]
        return seclist
    
    @property
    def shows(self):
        elem = self.server.query("/library/sections")
        seclist = [Section(e.attrib['title'], e.attrib['key'], self.server) for e in elem if e.attrib['type'] == 'show']
        return seclist

    @property
    def movies(self):
        elem = self.server.query("/library/sections")
        seclist = [Section(e.attrib['title'], e.attrib['key'], self.server) for e in elem if e.attrib['type'] == 'movie']
        return seclist