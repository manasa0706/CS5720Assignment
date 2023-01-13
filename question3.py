res = input("enter your score")
pc = float(res)
percentage = pc * 100 / 600
if percentage>=91 and percentage<=100:
    print("Your Grade is A")
elif percentage>=81 and percentage<91:
    print("Your Grade is B")
elif percentage>=71 and percentage<81:
    print("Your Grade is C")
elif percentage>=61 and percentage<71:
    print("Your Grade is D")
elif percentage>=0 and percentage<61:
    print("Your Grade is F")
else:
    print("Invalid Input!")
