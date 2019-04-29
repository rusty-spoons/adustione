class GenericScraper():
    def __init__(self):
        self.virtual = True
        self.currentPage = None
        self.host = None
    
    def scrape(self, startAt  = 0, stopAt= 5):
        """
        Defines how the data the scraper is supposed to output is found
        on the page.
        """
        raise NotImplementedError()
    
    def getNextPage(self):
        """
        Defines how the scrape function should get the next page.
        """
        raise NotImplementedError()
    
    def dumps(self, buffer):
        """
        Serializes the buffer object; Output may be json, protobuffers etc.
        """
        raise NotImplementedError()

    def process(self, startAt = 0, stopAt = 5):
        """
        Process calls the scrape and dumps function
        and returns the result.
        """
        objs = self.scrape(startAt, stopAt)
        return self.dumps(objs)
