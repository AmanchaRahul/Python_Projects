#super-market bill generator
from datetime import datetime

name=input("enter your name: ")
lists='''
Rice      Rs 20/kg
Sugar     Rs 30/kg
Salt      Rs 20/kg
Oil       Rs 80/litre
Paneer    Rs 110/kg
Maggi     Rs 50/kg
Boost     Rs 90/kg
Pepsodent Rs 85/kg
'''


ilist=[]    #item list
plist=[]    #price list
qlist=[]    #quantity list
pricelist=[]  
totalprice=0

#Rates for items
#it is stored in the dictionary format
items={"Rice":20,"Sugar":30,"Salt":20,"Oil":80,"Paneer":110,"Maggi":50,"Boost":90,"Pepsodent":85}
option=int(input("enter 1 to show the list of items: "))
if option==1:
    print(lists)

for i in range(len(items)):
    input1=int(input("Enter 1 to buy items or enter 2 to exit:"))
    if input1==2:
        break
    if input1==1:
           item=input("Enter the item you want to buy: ")
           quantity=int(input("Enter the quantity you want: "))
           if item in items.keys():
                price=quantity*(items[item])
                pricelist.append((item,quantity,price))  #pricelist=[(Rice,2,20),(Boost,3,90),(Maggi,1,50)]
                totalprice=totalprice+price                         # index=0   , index=1   , index=2         
                plist.append(price)
                qlist.append(quantity)
                ilist.append(item)     
                gst=(totalprice*5)/100 #5% rate of gst on all the items
                finalamount=totalprice+gst
           else:
                print("You entered an invalid item which is not present!")
    else:
         print("invalid option!")
    inp=input("Can I bill Now,please enter 'yes' or 'no': ")
    if inp=="yes":
        if finalamount!=0:
           print(25*"=","SuperMarket",25*"=")
           print("Name:",name,30*" ","Date:",datetime.now())
           
           print('sno',8*" ",'Item',8*" ",'Quantity',8*" ",'Price')
           for i in range(len(pricelist)):
                print(i,10*" ", ilist[i],12*" ",qlist[i],12*" ",plist[i])
           print(75*"-")
           print('TotalAmount:',50*" ",'Rs',totalprice)
           print("GstAmount:",54*" ",'Rs',gst)
           print(75*"-")
           print(50*" ","FinalAmount:",finalamount)
           print(75*"-")
           print(25*"-","Thanks for visiting!",25*"-")
print()
        
         
        
        


