from library import Library
from client import Client
from playlist import Playlist

import urllib2
from xml.etree.ElementTree import XML

class Server(object):

    def __init__(self, address, port=32400):
        # TODO: clean up address, remove http:// etc

        # remove slash at end of address
        if address[-1] == '/':
            address = address[:-1]
        self.address = address
        self.port = int(port)


    def put(self, path):
        if path[0] == '/':
            path = path[1:]

        try:
            opener = urllib2.build_opener(urllib2.HTTPHandler)
            request = urllib2.Request("http://%s:%d/%s" % (self.address, self.port, path))
            request.get_method = lambda: 'PUT'
            opener.open(request)
        except urllib2.URLerror, e:
            print e

    def delete(self, path):
        if path[0] == '/':
            path = path[1:]

        try:
            opener = urllib2.build_opener(urllib2.HTTPHandler)
            request = urllib2.Request("http://%s:%d/%s" % (self.address, self.port, path))
            request.get_method = lambda: 'DELETE'
            opener.open(request)
        except urllib2.URLerror, e:
            print e

    def execute(self, path):
        if path[0] == '/':
            path = path[1:]

        # open url
        try:
            urllib2.urlopen("http://%s:%d/%s" % (self.address, self.port, path))
        except urllib2.URLError, e:
            print e


    def query(self, path):
        if path[0] == '/':
            path = path[1:]

        # open url and get raw xml data
        try:
            response = urllib2.urlopen("http://%s:%d/%s" % (self.address, self.port, path))
        except urllib2.URLError, e:
            print e

        # create element from xml data
        xmldata = response.read()
        element = XML(xmldata)
        return element


    def __str__(self):
        return "<Server: %s:%d/>" % (self.address, self.port)

    def __repr__(self):
        return "<Server: %s:%d/>" % (self.address, self.port)


    @property
    def library(self):
        elem = self.query("/library")
        return Library(self)

    @property
    def clients(self):
        elem = self.query("/clients")
        clist = [Client(e, self) for e in elem]
        return clist

    @property
    def playlists(self):
        elem = self.query("/playlists")
        plist = [Playlist(e, self) for e in elem]
        return plist

    def playlist(self, title):
        for plist in self.playlists:
            if plist.title.lower() == title.lower():
                return plist

        return None

