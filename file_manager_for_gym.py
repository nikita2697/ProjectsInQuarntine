
def getdate():
    import datetime
    return datetime.datetime.now()


def write_file(a,b):
    if b==1:
        z1='y'

        data=input("enter food name:")
        with open(clients[a]+"_food.txt","a") as f:
                #f.write("[" +str(getdate()) +"]:" + data))
            f.write("[ " + str(getdate()) + " ] : " + data + "\n")
    else:
        data = input("enter exercise name:")
        with open(clients[a] + "_exercise.txt", "a") as f:
            # f.write("[" +str(getdate()) +"]:" + data))
            f.write("[ " + str(getdate()) + " ] : " + data + "\n")
    print("added successfully!!!")

def read_file(a,b):
    if b==1:
        z1='y'
        while(z1!='n'):
            with open(clients[a]+"_food.txt","w+") as f:
                content = f.readlines()
                if f.tell() == 0:
                    print("you have to write data first to read . There is nothing to read in file\n")
                else:
                    for i in content:
                        print(i)
            z1=input("do you want to add more[y/n]?")
    else:
        with open(clients[a]+"_exercise.txt","w+") as f:
            content=f.readlines()
            if f.tell()==0:
                print("you have to write data first to read . There is nothing to read in file\n")
            else:
                for i in content:
                    print(i)



try:
    clients = {1: "Harry", 2: "Rohan", 3: "Nikita"}
    z='y'
    while(z != 'n'):
        print("Enter name of client")
        for i,j in clients.items():
            print("Press", i, "for", j, "\n", end="")
        clientname=int(input())
        print("What you want to do read or write?\npress 1 for write \npress 2 for read")
        k=int(input())
        print("Select file type:\npress 1 for Food \npress 2 for Exercise:")
        x = int(input())
        if k==1:
            write_file(clientname,x)
        elif k==2:
            read_file(clientname,x)
        z=input("do you want to continue[y/n]:\n")
    else:
        print("Invalid input Enter 1 or 2 as a input")

except Exception as e:
    print(e)



