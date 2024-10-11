num1 = int(input("enter a whole number"))
num2 = int(input("enter a whole number"))
operand = input("enter and operation")
match operand:
    case "+":
        num3= num1+num2
        print(num3)
    case "-":
        num3= num1-num2
        print(num3)
    case "*":
        num3= num1*num2
        print(num3)
    case "/":
        num3= num1/num2
        print(num3)
    case "^":
        num3=num1**num2
        print(num3)
    case "%":
        num3=num1/num2
        num4= num3*100
        print(num4)
        

