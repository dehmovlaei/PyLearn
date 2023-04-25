PRODUCTS = [ ]

def readFromDataBase():
    f = open("07\dataBase.txt")
    for line in f:
        result = line.split(",")
        myDic = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
        print(result)
        PRODUCTS.append(myDic)
    f.close

def writeToDataBase():
    pass

def showMenu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- ShowList")
    print("6- Buy")
    print("7- Exit")

def add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    newProduct = {'code': code, 'name': name, 'price': price, 'count': count}
    PRODUCTS.append(newProduct)

def edit():
    pass

def remove():
    pass

def search():
    pass

def showList():
    print("code\t\tname\t\tprice\t\tcount")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"], "\t\t", product["count"], end="")

def buy():
    pass

print("WELCOME to My Store")
print("Loading...")
readFromDataBase()
print("Data Loaded")

while(True):
    showMenu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        showList()
    elif choice == 6:
        buy()
    elif choice == 7:
        writeToDataBase()
        exit(0)
    else:
        print("enter valid number")
