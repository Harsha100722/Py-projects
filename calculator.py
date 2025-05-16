def additon():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    print(f"The additon of {num1} and {num2} numebrs is : {num1+num2}")

def subtraction():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    print(f"The subtraction of {num1} and {num2} numebrs is : {num1-num2}")


def multiplation():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    print(f"The multiplation of {num1} and {num2} numebrs is : {num1*num2}")


def division():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    print(f"The division of {num1} and {num2} numebrs is : {num1/num2}")


def modulus():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    print(f"The modulo of {num1} and {num2} numebrs is : {num1%num2}")


while True:
    x=int(input(''' ******** operations list ********
1.Addition
2.Subtraction
3.Multiplation
4.Division
5.Modulus
0.quit
enter the number here:'''))
    
    if x==1:
        additon()
    elif x==2:
        subtraction()
    elif x==3:
        multiplation()
    elif x==4:
        division()
    elif x==5:
        modulus()
    elif x==0:
        print("quitting the process..")
        break
    else:
        print("enter valid number..!")
