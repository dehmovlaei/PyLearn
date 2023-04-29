import qrcode
<<<<<<< HEAD
=======

>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
PRODUCTS = []

def readFromDataBase():
    f = open('07\dataBase.txt')
    for line in f:
        result = line.split(',')
        myDic = {'code': int(result[0]), 'name': result[1], 'price': int(result[2]), 'count': int(result[3])}
        PRODUCTS.append(myDic)
    f.close

def writeToDataBase():
<<<<<<< HEAD
    strWrite = ''
    f = open('07\dataBase.txt', 'w')
    for product in PRODUCTS:
        f.write(str(product['code']) + ',' + product['name'] + ',' + str(product['price']) + ',' + 
                str(product['count']) + '\n')
=======
    f = open('07\dataBase.txt')
    for product in PRODUCTS:
>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
        print(product['code'], product['name'], product['price'], product['count'])
    f.close

def showMenu():
    print('1- Add')
    print('2- Edit')
    print('3- Remove')
    print('4- Search')
    print('5- ShowList')
    print('6- Buy')
    print('7- QR')
    print('8- Exit')

def add():
<<<<<<< HEAD
    code = int(input('enter code: '))
    name = input('enter name: ')
    price = int(input('enter price: '))
    count = int(input('enter count: '))
=======
    code = input('enter code: ')
    name = input('enter name: ')
    price = input('enter price: ')
    count = input('enter count: ')
>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
    newProduct = {'code': code, 'name': name, 'price': price, 'count': count}
    PRODUCTS.append(newProduct)

def edit():
    productCode = int(input('enter product code for edit: '))
    for product in PRODUCTS:
        if product['code'] == productCode:
<<<<<<< HEAD
            print(f'''\nwhich item of {product['name']} do you want to edit:''')
            print(f'''1- Name  - current name  is {product['name']}''')
            print(f'''2- Price - current price is {product['price']}''')
            print(f'''3- count - current count is {product['count']}''')
=======
            print('\nwhich item do you want to edit:')
            print('1- Name')
            print('2- Price')
            print('3- Count')
>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
            item = int(input('your choice: '))
            if item > 3:
                print('enter valid menu item!')
                break
            else:
                newValue = input('enter new value: ')
                if item == 1:
                    product['name'] = newValue
                    print('product name edited successfully')
                    break
                elif item == 2:
                    product['price'] = newValue
                    print('product price edited successfully')
                    break
                elif item == 3:
                    product['count'] = newValue
                    print('product count edited successfully')
                    break
    else:
        print('enter valid product code!!!')
        
def remove():
    productCode = int(input('enter product code for remove: '))
    for product in PRODUCTS:
        if product['code'] == productCode:
            PRODUCTS.remove(product)
<<<<<<< HEAD
            print(f'''product {product['name']} removed successfully''')
=======
            print('product removed successfully')
>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
            break
    else:
        print('this product code not found!')

def search():
    userInput = input('type your keyword:')
    for product in PRODUCTS:
<<<<<<< HEAD
        if str(product['code']) == userInput or product['name'] == userInput:
=======
        if product['code'] == int(userInput) or product['name'] == userInput:
>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
            print(product['code'], '\t\t', product['name'], '\t\t', product['price'])
            break
    else:
        print('not found!!!')

def showList():
    print('code\t\tname\t\tprice\t\tcount')
    for product in PRODUCTS:
        print(product['code'], '\t\t', product['name'], '\t\t', product['price'],
               '\t\t', product['count'])

def buy():
    buyFlag = True
    buyList = []
    sumFactor = 0

    while (buyFlag):
<<<<<<< HEAD
        productCode = int(input('enter product code for buy (ZERO 0 for exit): '))
=======
        productCode = int(input('enter product code for buy (ZIRO 0 for exit): '))
>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
        if productCode == 0:
            buyFlag = False
            break
        for product in PRODUCTS:
            if product['code'] == productCode:
                userCount = int(input(f'''how many {product['name']} do you have? '''))
                if userCount <= product['count']:
                    newCount = product['count'] - userCount
                    product['count'] = newCount
<<<<<<< HEAD
                    tmpDic = {'code': product['code'], 'name': product['name'], 'price': product['price'],
                               'count': userCount}
=======
                    tmpDic = {'code': product['code'], 'name': product['name'], 'price': int(product['price']), 'count': userCount}
>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
                    buyList.append(tmpDic)
                    break
                else:
                    print(f'''Insufficient inventory! inventory of {product['name']} is {product['count']} tray again''')
                    buy()
                    break
        else:
            print('this product code not found!')
    for factor in buyList:
        print(factor['name'], ' price:', factor['price'], ' amount:', factor['count'])
        sumFactor += factor['count'] * factor['price']
    print('totall Sum of your factor is: ', sumFactor)
<<<<<<< HEAD
    
=======
    print(buyList)

>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
def qr():
    productCode = int(input('enter product code for generate QR: '))
    for product in PRODUCTS:
         if product['code'] == productCode:
            qrString = product
            qr = qrcode.make(qrString)
            qr.save('07\productQR.png')
<<<<<<< HEAD
            print('QR generated successfully')
            break
    else:
         print('this product code not found!')
=======
            print('QR generated succesfully')
            break
    else:
         print('this product code not found!')
    
>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2

print('WELCOME to My Store')
print('Loading...')
readFromDataBase()
print('Data Loaded')
<<<<<<< HEAD
while(True):
    showMenu()
    choice = int(input('enter your choice: '))
=======

while(True):
    showMenu()
    choice = int(input('enter your choice: '))

>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
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
        qr()
    elif choice == 8:
        writeToDataBase()
        exit(0)
    else:
<<<<<<< HEAD
        print('enter valid number!!!')
=======
        print('enter valid number')
>>>>>>> f858a550a465b0bda85c92520a4ea81c224bf0f2
