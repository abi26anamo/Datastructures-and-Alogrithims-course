from stack import Stack
def func(data):

    data=data.split(",")

    

    stack =[]

    for i in range(len(data)):

        if data[i].isdigit():

            stack.append(int(data[i]))

        elif data[i]=="+" or data[i]=="*" or data[i]=="-" or data[i]=="/":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(a)+int(b))

        elif data[i]=="*":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(a)*int(b))

        elif data[i]=="/":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)/int(a))

        elif data[i]=="-":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)-int(a))            

    return stack.pop()
s= input("enter the postiffix")
val = func(s)
print(val)