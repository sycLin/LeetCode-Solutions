class Codec:
    
    def __init__(self):
        self.long2Short = {}
        self.short2Long = []
        self.counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # look up
        tmp = self.long2Short.get(longUrl)
        if tmp is not None:
            return tmp
        # add
        self.long2Short[longUrl] = str(self.counter)
        self.short2Long.append(longUrl)
        self.counter += 1
        return self.long2Short.get(longUrl)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        try:
            index = int(shortUrl)
            return self.short2Long[index]
        except:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))