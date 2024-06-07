'''print("Welcome to our village resturant")
print("Plese have a drink a cup of water . and see this menu sir !")
menu = {
    'chana anda':120,
    'black tea':30,
    'milk tea':45,
    'samosa tarkali': 50,
    'chuira tarkali': 70,
    'roti tarkali': 90
}
print("chana anda price :Rs 120\n black tea price :Rs 30\n  milk tea price :Rs 45\n samosa tarkali price :Rs 50\n chuira tarkali price : Rs 70 \n roti tarkali price : Rs 90\n ")
order_cost = 0
items = input("Enter any item of order that you want to have:")
if items in menu:
    order_cost += menu[items]
#print(order_cost)  suppose i order chana anda display that 120 
    print(f'your {items} item is on order list has been added successfully')
else:
    print(f'your {items} item is not available in our services!')
another_item1 = input("Do you want to another item in your list (yes or no:")
if another_item1 == "yes":
 next_item = input("Enter the next item that you want to have:")
 if next_item in menu:
    order_cost+=menu[next_item]
    print(f'your {next_item} is on the order list has been added successfuully')
 elif another_item1 == "no":
     print("the do not add furthur service")
 else:
     print(f'your {next_item} item is not available in our services!')

another_item2 = input("Do you want to another item in your list (yes or no:")
if another_item2 == "yes":
 next_item1 = input("Enter the next item that you want to have:")
 if next_item1 in menu:
    order_cost+=menu[next_item]
    print(f'your {next_item1} is on the order list has been added successfuully')

 else:
     print(f'your {next_item} item is not available in our services!')
    
another_item3= input("Do you want to another item in your list (yes or no:")
if another_item3 == "yes":
 next_item2 = input("Enter the next item that you want to have:")
 if next_item2 in menu:
    order_cost+=menu[next_item]
    print(f'your {next_item2} is on the order list has been added successfuully')

 else:
     print(f'your {next_item} item is not available in our services!')
print(f'the total cost of order in your list is {order_cost}')


    

#print(f'the total order of item cost is {order_cost}')'''

'''print("Welcome to our village resturant")
print("Please enjoy a refreshing cup of water while you take a look at our delightful menu, sir!")
menu = {
    'chana anda':120,
    'black tea':30,
    'milk tea':45,
    'samosa tarkali': 50,
    'chuira tarkali': 70,
    'roti tarkali': 90
}
print(" 1)chana anda price :Rs 120\n 2)black tea price :Rs 30\n 3)milk tea price :Rs 45\n 4)samosa tarkali price :Rs 50\n 5)chuira tarkali price : Rs 70 \n 6)roti tarkali price : Rs 90\n ")
order_cost = 0
items = input("Enter any item of order that you want to have:")
if items in menu:
    order_cost += menu[items]
    print(f'your {items} item is on order list has been added successfully')
    print("I will bring your order as quickly as possible. Meanwhile, please have a seat and enjoy our services!")
    
else:
    print(f'your {items} item is not available in our services!')
    print("You can sit and enjoy our place while sipping your water. Please stay as long as you like.")
item1 = input(" Do you want another item of our menu list :(yes or no)")

if item1 == "yes":
   for another_item1 in menu:
       another_item1 = input("enter the another any  item in our list:")
       order_cost = menu[another_item1]
       print(f'your n{another_item1} has been added in our menu list successfully')
       break
else:
    print("Thanks for giving service oppertunity to us ")
    print("we will give you bill detail later on sir!")



item2 = input(" Do you want another item of our menu list :(yes or no)")

if item2 == "yes":
   for another_item2 in menu:
       another_item2 = input("enter the another any  item in our list:")
       order_cost = menu[another_item2]
       print(f'your {another_item2} has been added in our menu list successfully')
       break
else:
    print("Thanks for giving service oppertunity to us ")
    print("we will give you bill detail later on sir!")

item3 = input(" Do you want another item of our menu list :(yes or no)")

if item3 == "yes":
   for another_item3 in menu:
       another_item3 = input("enter the another any  item in our list:")
       order_cost = menu[another_item3]
       print(f'your {another_item3} has been added in our menu list successfully')
       break
else:
    print("Thanks for giving service oppertunity to us ")
    print("we will give you bill detail later on sir!")

item4 = input(" Do you want another item of our menu list :(yes or no)")

if item4 == "yes":
   for another_item4 in menu:
       another_item4 = input("enter the another any  item in our list:")
       order_cost = menu[another_item4]
       print(f'your {another_item4} has been added in our menu list successfully')
       break
else:
    print("Thanks for giving service oppertunity to us ")
    print("we will give you bill detail later on sir!")


item5 = input(" Do you want another item of our menu list :(yes or no)")

if item5 == "yes":
   for another_item5 in menu:
       another_item5 = input("enter the another any  item in our list:")
       order_cost = menu[another_item5]
       print(f'your {another_item5} has been added in our menu list successfully')
       break
else:
    print("Thanks for giving service oppertunity to us ")
    print("we will give you bill detail later on sir!")

item6 = input(" Do you want another item of our menu list :(yes or no)")

if item6 == "yes":
   for another_item6 in menu:
       another_item6 = input("enter the another any  item in our list:")
       order_cost = menu[another_item6]
       print(f'your {another_item6} has been added in our menu list successfully')
       break
else:
    print("Thanks for giving service oppertunity to us ")
    print("we will give you bill detail later on sir!")'''


''' another_item1 = input("enter the another item in our menu list:")
if another_item1 in menu:
order_cost = menu[another_item1]
print(f'your n{another_item1} has been added in our menu list successfully')'''






print("Welcome to our village restaurant")
print("Please enjoy a refreshing cup of water while you take a look at our delightful menu, sir!")

menu = {
    'chana anda': 120,
    'black tea': 30,
    'milk tea': 45,
    'samosa tarkali': 50,
    'chuira tarkali': 70,
    'roti tarkali': 90
}

print(
    " 1) chana anda price : Rs 120\n 2) black tea price : Rs 30\n 3) milk tea price : Rs 45\n 4) samosa tarkali price : Rs 50\n"
    " 5) chuira tarkali price : Rs 70\n 6) roti tarkali price : Rs 90\n"
)

order_cost = 0

while True:
    item = input("Enter any item of order that you want to have: ")
    if item in menu:
        order_cost += menu[item]
        print(f"Your {item} has been added to your order list successfully.")
        print("I will bring your order as quickly as possible. Meanwhile, please have a seat and enjoy our services!")
    else:
        print(f"Sorry, {item} is not available in our services!")
        print("You can sit and enjoy our place while sipping your water. Please stay as long as you like.")

    another_item = input("Do you want another item from our menu list? (yes or no): ")
    if another_item == "no":
        print("Thanks for giving us the opportunity to serve you.")
        print("We will give you the bill details shortly.")
        break
    elif another_item == "yes":
        continue
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        break

print(f"Your total order cost is Rs {order_cost}. Thank you for your order sir!")