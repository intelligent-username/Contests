# Airport GATES; COMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2015/stage%201/seniorEn.pdf #3

G = int(input()) 
# # Of Gates at Airport

availability = [True] * G

P = int(input())
# # Of Planes that will land

landings = 0

for x in range(P):
    Accomplishment = False
    
    # Preferred docking gate, but can dock anywhere from position 1 to g, inclusive
    g = int(input())
    if availability[g-1]:
        landings += 1
        availability[g-1] = False
        Accomplishment = True
    else:
        g-=1
        while g >= 0:
            if availability[g]:
                landings += 1
                availability[g] = False
                Accomplishment = True
                break
            g -= 1
    
    if not Accomplishment:
        break

print("ANASWER:", landings)
