from movie import Movie
from show import Show
from episode import Episode

class Playlist(object):
    def __init__(self, element, server):
        self.server = server

        try:
            self.title = element.attrib['title']
            self.key = element.attrib['key']
            self.type = element.attrib['type']
        except KeyError as e:
            print "Missing key in element: ", e.message

    def __str__(self):
        return "<Playlist: %s>" % self.title

    def __repr__(self):
        return "<Playlist: %s>" % self.title

    def __contains__(self, element):
        return element in self.getContent()

    def append(self, item):
        self.server.put("%s?uri=library://unknown/item%s" % (self.key, item.key))

    def remove(self, item):
        self.server.delete("%s/%s" % (self.key,                                                                       item.element.attrib['playlistItemID']))

    def getContent(self):
        container = self.server.query(self.key)

        content = []
        for e in container:
            if not 'type' in e.attrib:
                continue
            type_ = e.attrib['type']
            if type_ == 'movie':
                # append movie
                obj = Movie(e, self.server)
            if type_ == 'episode':
                obj = Episode(e, self.server)

            content.append(obj)

        return content
