age= int(input("How old are you?:"))
student = input("are you a student?")
if age < 12 or age >65:
    print("£5 per ticket")
elif age >= 12 and age <65 and student == ("yes"):
    print ("£8 per ticket")
else:
    print("£10 per ticket")