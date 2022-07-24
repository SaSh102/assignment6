from pyfiglet import Figlet

def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])


def show_menu():
    print('1- Add Product')
    print('2- Edit Product')
    print('3- Delete Product')
    print('4- Search')
    print('5- Show List')
    print('6- Buy')
    print('7- Exit')

def load():
    print('Loading...')
    myfile = open('database.txt', 'r')
    # print(myfile)
    data = myfile.read()
    # print(data)
    products_list = data.split('\n')
    # print(products_list)

    
    for i in range(len(products_list)):
        product_info = products_list[i].split(',')
        mydict={}
        myfile['id'] = product_info[0]
        myfile['name'] = product_info[1]
        myfile['price'] = product_info[2]
        myfile['count'] = product_info[3]
        PRODUCTS.append(mydict)
    print('Welcome')

PRODUCTS = []
print(PRODUCTS)

f = Figlet(font='standard')
print (f.renderText('Samira Store'))



show_menu()
choice = int(input('Please choose a number: '))

if choice == 1:
    pass
elif choice == 2:
    pass
elif choice == 3:
    pass
elif choice == 4:
    pass
elif choice == 5:
    show_list()

elif choice == 6:
    pass
elif choice == 7:
    pass


