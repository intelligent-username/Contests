from random import randint

class example:
    x = randint(1, 100)
    def __init__(self, a, b = 12, c = 33):
        self.a= a
        self.b = b
        self.c = c

    if x % 2:
        # X is odd
        d = b * c + a
    else:
        d = b * a + c


    def display(self):
        print("d =", self.b * self.a + self.c)
    
        
example(1,2,3)
# Not useful but might as well use

for name in example.__dict__:
    print(name)


