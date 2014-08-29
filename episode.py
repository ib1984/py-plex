from video import Video
from media import Media
class Episode(Video):

    def __init__(self, element, server):
        super(Episode, self).__init__(element, server)

        self.type = 'episode'
        try:
            self.episode = int(element.attrib['index'])
            self.season = int(element.attrib['parentIndex'])
            self.show_title = element.attrib['grandparentTitle']
        except KeyError as e:
            print "Missing key in element: ", e.message

    def __str__(self):
        return "<Episode: %s - %dx%.2d - %s>" % (self.show_title, self.season, self.episode, self.title)

    def __repr__(self):
        return "<Episode: %s - %dx%.2d - %s>" % (self.show_title, self.season, self.episode, self.title)

    def __eq__(self, other_episode):
        return self.__repr__() == other_episode.__repr__()

