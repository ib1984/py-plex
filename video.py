from media import Media
class Video(object):

    def __init__(self, element, server):
        self.element = element
        self.server = server

        # browse element and extract some information
        self.key = element.attrib['key']
        self.type = 'video'
        self.title = element.attrib['title']
        self.summary = element.attrib['summary']

        self.viewed = ('viewCount' in element.attrib) and (element.attrib['viewCount'] >= '1')
        self.duration = int(element.attrib['duration']) / 1000 if 'duration' in element.attrib else 0
        self.offset = int(element.attrib['viewOffset']) / 1000 if 'viewOffset' in element.attrib else 0

        self.media = [Media(e, self.server) for e in element.findall('.Media')]

    def __str__(self):
        return "<Video: %s>" % (self.key)

    def __repr__(self):
        return "<Video: %s>" % (self.key)

    def __eq__(self, other_video):
        return self.__repr__() == other_video.__repr__()
