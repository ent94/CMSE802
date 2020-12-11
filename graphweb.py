# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
from html.parser import HTMLParser  
from urllib import parse
from urllib.request import urlopen  
from urllib.request import urlretrieve

class LinkParser(HTMLParser):
    """A website Parser to recursivly look though links in a webpage"""
    # This is a function that HTMLParser normally has
    # but we are adding some functionality to it
    def handle_starttag(self, tag, attrs):
        """Function to look for the begining of a link. Links normally look
        like <a href="www.someurl.com"></a>"""
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # We are grabbing the new URL. We are also adding the
                    # base URL to it. For example:
                    # www.netinstructions.com is the base and
                    # somepage.html is the new URL (a relative URL)
                    #
                    # We combine a relative URL with the base URL to create
                    # an absolute URL like:
                    # www.netinstructions.com/somepage.html
                    newUrl = parse.urljoin(self.baseUrl, value)
                    # And add it to our colection of links:
                    self.links = self.links + [newUrl]

    def getLinks(self, url):
        """This is a new function that we are creating to get links
        that our spider() function will call"""
        self.links = []
        # Remember the base URL which will be important when creating
        # absolute URLs
        self.baseUrl = url
        # Use the urlopen function from the standard Python 3 library
        response = urlopen(url)
        # Make sure that we are looking at HTML and not other things that
        # are floating around on the internet (such as
        # JavaScript files, CSS, or .PDFs for example)
        if 'text/html' in response.getheader('Content-Type'):
            htmlBytes = response.read()
            # Note that feed() handles Strings well, but not bytes
            # (A change from Python 2.x to Python 3.x)
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString,self.links #htmlString, self.links
        if 'text/plain' in response.getheader('Content-Type'):
            return url,[]
        else:
            return "",[]


def spider(url, maxPages):  
    """Main Spider function which takes in a URL and the number of pages 
    to search through before Stopping."""
    pagesToVisit = [url]
    numberVisited = 0

    # The main loop. Create a LinkParser and get all the links on the page.
    # Also search the page for the word or string
    # In our getLinks function we return the web page
    # (this is useful for searching for the word)
    # and we return a set of links from that web page
    # (this is useful for where to go next)
    while numberVisited < maxPages and pagesToVisit != []:
        numberVisited = numberVisited +1
        # Start from the beginning of our collection of pages to visit:
        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]

        try:
            print(numberVisited, "Visiting:", url)
            parser = LinkParser()
            data, links = parser.getLinks(url)
            pagesToVisit = pagesToVisit + links
        except:
            print(" **Failed to parse page!**")