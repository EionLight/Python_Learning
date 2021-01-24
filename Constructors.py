class Test:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def repeat(self):
        print("In repeat")

    def repeat2(self):
        print("In repeat2")


#constructor
Tester=Test(10,20)
print(Tester.x)
print(Tester.y)
Tester.repeat()

