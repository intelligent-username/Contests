# FAVORITE TIMES; INCOMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf #4

# Start at Noon, find arithmetic series

# Steps
# Figure out how to encode time
# Figure out what the max increments of arithmetic series are (6? 4?)
# Then it's just simple math
def main():
    Noon = [12, 00]
    Passed = int(input()) # The number of minutes passed

    Hours = Passed // 60
    Minutes = Passed - Hours * 60
    
    Endtime = [Noon[0] + Hours, Noon[1] + Minutes]
    
    palindrome_counter = 0




def arithmetic_checker(time):
    if int(time[3]) - int(time[2]) == int(time[1]) - time[0] and time[2] - time[1] == time[3] - time[2]:
        return True

if __name__ == "__main__":
    main()
