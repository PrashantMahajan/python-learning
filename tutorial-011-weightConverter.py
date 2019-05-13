weight = float(input("Weight: "));
poudsOrKgs = input("(L)bs or (K)g: ");


if poudsOrKgs.lower() == 'l':
    print(f"You are {weight*0.453592} Kgs");
elif poudsOrKgs.lower() == 'k':
    print(f"You are {weight*2.20462} Pounds");
else:
    print("Please Enter Valid Values");