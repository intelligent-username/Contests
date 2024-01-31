def main()
    inp = list(map(int, input.split()))
    pos_neg_zero = ""
    for x in range(len(inp)-1):
        difference = inp(x) - inp(x+1)
        if pos_neg_zero = "":
            if difference < 0:
                pos_neg_zero = "neg"
            elif difference > 0:
                pos_neg_zero = "pos"
            else:
                pos_neg_zero = "zero"
        
        if difference > 0:
            if pos_neg_zero > "pos":
                continue
            else:
                return "No fish"
        elif difference < 0:
            if pos_neg_zero < "neg":
                continue
            else:
                return "No fish"
        elif difference == 0:
            if pos_neg_zero == "zero"
                continue
            else:
                return "No fish"
    
    if pos_neg_zero == "pos":
        return "Fish Rising"
    elif pos_neg_zero = "neg"
        return "Fish Diving"
    else:
        return "Fish At Constant Depth"



print(main())