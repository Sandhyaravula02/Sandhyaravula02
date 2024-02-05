from datetime import datetime 


username=input("Enter your name:")
#list of items we want to buy
list='''
Sugar 20/kg
Rice  30/kg 
Maggie 50/kg
Teapowder 45/kg
Paneer 60/kg
Boost 40/each
Oil   90/litre
Sensodyne  80/each
Redgram    110/kg
'''
print(list)

# declaration of items 
price=0
pricelist=[]
totalprice=0
finalprice=0
qlist=[]
plist=[]
ilist=[]

# rate of items
items={
'Sugar':20,
'Rice':30,
'Maggie':50,
'Tea powder':45,
'Paneer':60,
'Boost':40,
'Oil':90,
'Sensodyne':80,
'Redgram':110
}
option=int(input("click your option:"))
if option==1:
    print(items)
    for x in range(len(items)):
        inp1=int(input("if you want to buy an item click 1 or click 2 to exit:"))
        if inp1==2:
            break
        if inp1==1:
            item=input("Enter your items:")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5/100)
            finalamount=gst+totalprice
        else:
            print("you entered item is not available")
    else:
            print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=="yes":
        pass
    if finalamount!=0:
        print(25*"=","Manandhari Market",25*"=")
        print(28*" ","Hyderabad")
        print("Name:","name",30*" ","Date:",datetime.now())
        print(75*"-")
        print("sno",8*" ","items",8*" ","quantity",8*" ","price")
        for x in range(len(pricelist)):
            print(x,4*' ',5*' ',ilist[x],8*' ',qlist[x],16*' ',plist[x])
            print(75*"-")
            print(50*"-","Total amount:",'Rs',"total price")
            print("gst amount:",40*' ','Rs',gst)
            print(75*"-")
            print(50*"-",'final amount:','Rs','final price')
            print(75*"-")
            print(15*"-","Thanks for visiting ")
            print(75*" ")
            
            
        
        








