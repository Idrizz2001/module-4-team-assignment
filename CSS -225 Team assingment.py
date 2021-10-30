#Javonnie Garner & Idris
#10-29-2021

# our program is going to print a list of options and alow the user to pick one

print("Please pick an option from the list:")

print("1: Python")
print("2: Watch TV")
print("3: Go outside")
print("4: Go on a fild trip")
print("5: Go to school")
print("6: Relax at home")
print("7: Play viedo games")
print("8: Go shopping")
print("0: Exit")

opt= input("Pick a number 0-8")

if opt == "1":
    print("Python is loading")
elif opt == "2":
    print("Go have fun watching TV!")
elif opt == "3":
    print("Go have fun outside!")
elif opt == "4":
    print("Have fun on your fild trip")
elif opt == "5":
    print("Have fun at school")
elif opt == "6":
    print("Go relax at home")
elif opt == "7":
    print("Have fun playing your video games")
elif opt == "8":
    print("Be safe shoping")
elif opt == "0":
    print("Goodbye, Exit")
else:
    print("This input is invalet")
