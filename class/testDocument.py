from document import Document, Book, Email, DocList
from datetime import date

### test constructor dan __str__     
a = Document()
print(a)
b = Book()
print(b)
c = Email()
print(c)
print()
a = Document(["Chairil Anwar"], date(2020, 8, 17))
print(a)
b = Book(["Hinkle", "Elmasri"], date.today(), "Python for Dummy")
print(b)
c = Email(["Super Maung"], date(2018, 12, 1),\
        "Latihan DDP1", "2019@cs.ui.ac.id")
print(c)

### test method get
# print()
# print(b.getAuthors())
# print(b.getDate())

# print(b.getTitle())
# print(c.getDate())
# print(c.getSubject())
# print()

### test dir dan dict
# print(dir(a))
# print()
# print(dir(b)) 
# print()
# print(dir(c))
# print()
# print(a.__dict__)
# print()
# print(b.__dict__)
# print()
# print(b.__dict__)

### test DocList
# print()
# aDocList = DocList([a, b])
# aDocList.addDoc(c)
# print(aDocList)

# test equality
print()
x = Document(["pen1"], date.today())
y = Book(["pen1"], date.today(), "judul")
z = Email(["pen1"], date.today(), "subject", "dia@cs")

print(isinstance(x, Document))
print(isinstance(y, Document))
print(isinstance(z, Document))
print()
print(type(x)==Document)
print(type(y)==Document)
print(type(z)==Document)
print()
x2 = Document(["pen2"], date.today())
print(x == x2)
print(x == y)
print(x == z)

### test sort
print()
x = Document(["pen1"], date.today())
y = Book(["pen1"], date(1991, 4, 16), "judul")
z = Email(["pen1"], date(2019, 2, 6), "subject", "dia@cs")

print(x<y)
aDocList2 = DocList([x, y, z])
print(aDocList2)
aDocList2.dlist.sort()
print(aDocList2)

