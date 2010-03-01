# pipefetch.py
#

import feedparser

def pipe_fetch(URL):
    """This source fetches and parses one or more feeds to yield the feed entries.
    
    Keyword arguments:
    URL -- url generator
    
    Yields (_OUTPUT):
    feed entries
    """
    for item in URL:
        d = feedparser.parse(item)
        
        for entry in d['entries']:
            yield entry

# Example use

if __name__ == '__main__':
    feeds = pipe_fetch(["test/feed.xml"])
    for f in feeds:
        print f
        print f.keys()