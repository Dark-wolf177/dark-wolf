def collector():
    print("collector:")
    number1 = int(input("number1:"))
    number2 = int(input("number2:"))
    print (number1 +  number2)
def hit():
    print("hit")
    number1 = int(input("number1:"))
    number2 = int(input("number2:"))
    print (number1 * number2)
def Differentiation():
    print("menha")
    number1 = int(input("Number One : "))
    number2 = int(input("Number Two : "))
    print(number1 - number2)
def Distribution():
    print("taghsim")
    number1 = int(input("Number One : "))
    number2 = int(input("Number Two : "))
    print(number1 / number2)
while True:
    ab = int(input("0-collector\n1-hit\n2-diffrentiation\n3-Distribution\n4-exit\n :"))
    sleep(1)
    if ab ==0:
        collector()
    elif ab ==1:
        hit()
    elif ab ==2:
        Differentiation()
    elif ab == 3:
        Distribution()
    elif ab == 4:
        print("Good Bye from m4apower Digital Security")
        break
