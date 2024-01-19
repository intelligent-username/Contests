# INCOMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2007/stage1/seniorEn.pdf
people = []

def main():
    # Each student will have a friend (one-way)
    n = int(input("Input # of students in class: "))

    for i in range(n):
        friendship_maker(input("Friendship pair #", i+1, ": "))

    # For friendship loops
    loops = []
    temp = ""
    while temp != "0 0":
       temp = input("Input comparison: ")
       if temp != "0 0":
          loops.append(tuple(temp.split()))
    
    lengths = []

    for i in loops:
       if i[0] in people:
          lengths += chain_finder(i[0], i[1])
    
    for h in lengths:
        if h:
            print("Yes ", h)
        else:
           print("No")

def chain_finder(person1, person2):
    p1_pointer = ""
    for x in range(len(people)):
        if people[x].get_value() == person1:
            p1_pointer = x
            break
        else:
            print("Error, person doesn't exist")
            return 1
    
    length = 0
    for j in range(len(people)):
        if people[p1_pointer].get_next_node() == person2:
            return length
    
    return False


def friendship_maker(raw):
   temp_pair = raw.split()

   one = Node(temp_pair[0])
   two = Node(temp_pair[1])
   one.set_next_node(two)

   people.append(one)
   people.append(two)


class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value

if __name__ == "__main__":
    main()
