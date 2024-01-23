# FAVORITE TIMES; INCOMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf #4

# Start at Noon, find arithmetic series

# Steps
# Figure out how to encode time
# Max increment: 4
# Then it's just simple math

# Examples:
# 12:34, 1:11, 1:23, 1:35, 1:47, 1:59
# 2:10, 2:22, 2:34, 2:46, 2:58, 3:21
# 3:33, 3:45, 3:57, 4:20, 4:32, 4:44
# 4:56, 5:55, 5:43, 5:31, 6:54
#  6:42, 7:53, 8:52, 9:51, 11:11

# 28 during 12 hours

def main():
    Start_Time = [12, 00]
    Passed = int(input()) # The number of minutes passed

    Hours = Passed // 60
    Minutes = Passed - Hours * 60
    
    End_time = [Start_Time[0] + Hours, Start_Time[1] + Minutes]
    palindrome_counter = 0


    if End_time[1] > 60:
        End_time[1] -= 60
        End_time[0] += 1
    
    End_time[1].zfill(2)

    if End_time[0] > 12:
        while End_time[0] > 12:
            End_time[0] -= 12
            palindrome_counter += 28







def arithmetic_checker(time):
    if int(time[3]) - int(time[2]) == int(time[1]) - time[0] == time[3] - time[2]:
        return True

if __name__ == "__main__":
    main()
