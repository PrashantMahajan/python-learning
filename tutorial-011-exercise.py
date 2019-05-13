name = input("Please Enter Your Name:\n");

if 3 > len(name):
    print("Name Looks Short");
elif len(name) < 50:
    print("Name Looks Good");
else:
    print("Name Looks Long");
