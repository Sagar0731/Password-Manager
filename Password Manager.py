Mpass=input("What is the Master Password? ")

def view():
    with open("password.txt","r")as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split(":")
            print("user:",user,":","Password:",passw)
def add():
    name=input("Account Name: ")
    pwd=input("password: ")
    with open('password.txt','a')as f:
        f.write(name + "  " + pwd + "\n")
while True:
    mode=input("would you like to add a new password or view existing ones(view,add),press q to quit?").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid mode")
        continue
