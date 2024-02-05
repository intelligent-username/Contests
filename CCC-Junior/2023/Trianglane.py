# TRIANGLANE: COMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2023/ccc/seniorEF.pdf #1
# Not gonna follow exact required input methods for readability. Can simply remove text in the inputs to meet requirements.

# Initiate Variables Needed for calculations, etc. 
columns = int(input("Length of Columns: "))

row1 = list(map(int, input("Row 1: ").split()))
row2 = list(map(int, input("Row 2: ").split()))
print("Row 1:", row1, "\n\nRow 2:", row2)

# Store the string inputs into the lists by converting to bools

# Add false index to the end of each list to avoid going out of bounds during the loop
row1.append(False)
row2.append(False)

# Initiate variables
total_meters = 0
redundancy = 0