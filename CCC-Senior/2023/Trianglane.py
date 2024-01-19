# Initiate lists to store the rows in
row1 = []
row2 = []

# Get the length of the columns
columns = int(input("#: "))

# Get the contents of the rows as a string
row1_input = input("Input 1: ")
row2_input = input("Input 2: ")

# Store the string inputs into the lists by converting to bools
for i in range(columns):
    row1.append(bool(int(row1_input[i])))
    row2.append(bool(int(row2_input[i])))

# Add false index to the end of each list to avoid going out of bounds during the loop
row1.append(False)
row2.append(False)

# Initiate variables
total_meters = 0
redundancy = 0

# Counting of metres of tape
for i in range(columns):
    
    if row1[i]:
        total_meters += 3
        # Base case, each triangle needs 3

        if row1[i +1]:
            redundancy += 1
            # If the item to the right of the triangle is painted, one less metre is needed

        if (i > 0) and row1[i-1]:
            redundancy += 1
            # Given that there is an item to the left of the triangle, check for redundancy
            
        if not (i % 2) and row2[i]:
            redundancy += 1
            # Only the evenly-indexed triangles will make contact with the row below to cause a redundancy

    if row2[i]:
        total_meters += 3
        # Base Case

        if row2[i+1]:
            redundancy +=1
        # Check the right

        if (i > 0) and row2[i - 1]:
            redundancy += 1
            # Check left if applicable
        
        if not (i % 2) and row1[i]:
            redundancy += 1
            # Only the evenly-indexed triangles will make contact with the row above to cause a redundancy            
        

total_meters = total_meters - redundancy
print(total_meters)