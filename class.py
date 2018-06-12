class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
    def printScore(self):
        print('%s: %s' % (self.name, self.score))
        #print(self.score)

student = Student("TOM",87)
student.printScore()

#x = input("please input x:")

#print("the length of %s is %d" % (x,y))
