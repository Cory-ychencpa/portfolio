print("Welcome to the Royal Name Generator!")
print("Enter your name: ")
name = input().strip()
space = name.find(" ")
first = (name[0 : space]).capitalize()
last = (name[space : ]).upper()
initial = (name[0 : 1]).capitalize()
print("Are you a male or female?(m/f)")
gender = input()
if gender == "m":
    print("Sir "+initial+"."+last+" King "+first)
elif gender == "f":
    print("Madam "+initial+"."+last+" Queen "+first)
else:
    print("You are an idiot, not royalty")
