#6.1
class Nguoi(object):
 def getGender( self ):
 return "Unknown"

class Nam( Nguoi ):
 def getGender( self ):
 return "Nam"
class Nu( Nguoi ):
 def getGender( self ):
 return "Nữ"

aNam = Nam()
aNu= Nu()
print (aNam.getGender())
print (aNu.getGender())
#6.2
class Shape(object):
    def __init__(self):
       pass

    def area(self):
       return 0
class Square(Shape):
    def __init__(self, l):
       Shape.__init__(self)
       self.length = l

    def area(self):
       return self.length*self.length

aSquare= Square(3)
print (aSquare.area())
