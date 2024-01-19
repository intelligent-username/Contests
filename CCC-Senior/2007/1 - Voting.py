# COMPLETE
# Determine Federal Voting Age, https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2007/stage1/seniorEn.pdf
def main():
    n = int(input("# of voters: "))

    birthdays = []

    for i in range(n):
        input_date = input("Birthday: ").split(" ")

        birthdays.append({
            "year": int(input_date[0]),
            "month": int(input_date[1]),
            "day": int(input_date[2])
        })

        print(f"\n\n---------------Appended birthday #{i+1}-------------------\n\n")


    # Checking
    length = len(birthdays)
    for i in range(length):
        print(f"Birthday #{i+1} year: {birthdays[i]['year']}")
        print(f"Birthday #{i+1} month: {birthdays[i]['month']}")
        print(f"Birthday #{i+1} day: {birthdays[i]['day']}")

    answers = validator(birthdays)

    for i in answers:
        if i:
            print("Yes")
        else:
            print("No")


def validator(birthdays):
    # Checking if 18 on February 27th, 2007
    result = []
    for x in birthdays:
        
        if 2007 - x['year'] > 18:
            result.append(True)

        elif 2007 - x['year'] == 18:
            if 2 - x['month'] > 0:
                result.append(True)

            elif 2 - x['month'] == 0:
                if 27 - x['day'] >= 0:
                    result.append(True)
                else:
                    result.append(False)

            else:
                result.append(False)
        else:
            result.append(False)    

        # GPT-Made alternative #1:            
        #    for x in birthdays:
                # age = 2007 - x['year']
                # if age > 18:
                #     result.append(True)
                # elif age == 18:
                #     if x['month'] < 2 or (x['month'] == 2 and x['day'] <= 7):
                #         result.append(True)
                #     else:
                #         result.append(False)
                # else:
                #     result.append(False)  
        
        # GPT-Made alternative #2:      
        # from datetime import datetime
        # ...def validator()...      
        # cutoff_date = datetime(year=2007, month=2, day=7)
        # result = []
        # for birthday in birthdays:
        #     age = (cutoff_date - birthday).days // 365  # Simplified age calculation
        #     result.append(age >= 18)

    return result

# actually Start program
if __name__ == "__main__":
    main()
