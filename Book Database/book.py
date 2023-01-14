class Book():
    favs = [] #class

    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return True

    def __str__(self):
        return f"{self.title}, {self.pages} pages long"

    def __eq__(self,other):
        if(self.title == other.title and self.pages == other.pages):
            return True
    
    __hash__ = None

    def __repr__(self):
        return self.__str__()
