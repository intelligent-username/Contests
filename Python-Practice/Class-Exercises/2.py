from random import randint

class example:
    def __init__(self, a, b = 12, c = 33):
        self.a= a
        self.b = b
        self.c = c

        x = randint(1, 100)

        if x % 2:
            
            # X is odd
            self.d = b * c + a
        else:
            self.d = b * a + c


    def display(self):
        print("d =", self.d)
    
        
example(1,2,3)
# Not useful but might as well use

for name in example.__dict__:
    print(name)


