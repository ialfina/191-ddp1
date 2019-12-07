"""
Contoh Solusi Latihan Class
DDP 1 Kelas B, Semester Gasal 2019/2020

@Author Ika Alfina (ika.alfina@cs.ui.ac.id)
@last_update December 7, 2019

"""
from datetime import date

class Document:
    def __init__(self, authors = [], date = date.today()):
        self.__authors = authors
        self.__date = date

    def getAuthors(self):
        return self.__authors

    def addAuthor(self, name):
        self.__authors.append(name)

    def getDate(self):
        return self.__date

    def __str__(self):
        return "Authors: " + str(self.__authors) + \
             ", Date: " + str(self.__date)

    def __eq__(self, anotherItem):
        if anotherItem.__class__ == Document:
            if self.__authors == anotherItem.getAuthors() and \
                self.__date == anotherItem.getDate():
                return True
            else:
                return False
        else: 
            return False

    def __lt__(self, anotherItem):
        return self.__date < anotherItem.__date

class Book(Document):

    def __init__(self, authors=[], date=date.today(), \
         title = ""):
        # super().__init__(authors, date)
        Document.__init__(self,authors, date)
        self.__title = title

    def getTitle(self):
        return self.__title

    def __str__(self):
        return super().__str__() + ", Title: " + self.__title

    def __eq__(self, anotherItem):
        if type(anotherItem) == Book:
            if super().__eq__(anotherItem):
                if self.__title == anotherItem.getTitle():
                    return True
                else:
                    return False
            return False
        else:
            return False

class Email(Document):

    def __init__(self, authors=[], date=date.today(), \
        subject="", to="dia@cs.ui.ac.id"):
        super().__init__(authors, date)
        self.__subject = subject
        self.__to = to

    def __str__(self):
        return super().__str__() + \
            ", Subject: " + self.__subject + ", To: " + self.__to

    def getSubject(self):
        return self.__subject
    
    def getTo(self):
        return self.__to

    def __eq__(self, anotherItem):
        if type(anotherItem) == Email:
            if super().__eq__(anotherItem):
                if self.__subject == anotherItem.getSubject() and \
                    self.__to == anotherItem.getTo():
                    return True
                else:
                    return False
            return False
        else:
            return False

"""
Class DocList represents a collection of Document(s) (and its subclasses)
"""
class DocList:
    def __init__(self, dlist=[]):
        self.dlist = dlist

    def addDoc(self, aDoc):
        self.dlist.append(aDoc)

    def __str__(self):
        result=""
        for elemen in self.dlist:
            result += str(elemen) + "\n"
        return result
