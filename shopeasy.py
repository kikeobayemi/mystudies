#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""  
System Implementation task
 
Starting with the Merchant class that contains Merchant Data and merchant related functions.

"""  
import random
from datetime import datetime
  
class Merchant:
    
    #List of merchant items sold have been predefined in a dictionary
    
    def __init__(self, merchantid, name, category, merchantList = {300:["Primark", "Clothing", "* * * "], 
                301:["Fred Perry", "Clothing", "* * * *"], 302:["Wallis", "Clothing", "* * * * *"], 303:["Zara","Clothing", "* * * * "],
                304:["Clarks", "Footwear", "* * * * *"], 305: ["Carvela", "Footwear", "* * * *"]}):
        
        
        self.merchantid = merchantid
        self.name = name
        self.category = category
        self.merchantList = merchantList
        
        
      
    def merchantWindow(self): #provides merchant account creation and login funtions
        m = Merchant("","","") 
        merchantIdList = list(self.merchantList.keys())
        merchValueList = list(self.merchantList.values())
        
        userinput10 = input("Enter E for existing merchant or N for New Merchant: ").strip().upper()
        if userinput10 == "E":
            userinput11 = int(input("Enter your merchant id: "))
            if userinput11 in merchantIdList:
                merchantIdList.index(userinput11)
                print("")
                print("Welcome back {}!".format(merchValueList[merchantIdList.index(userinput11)][0]))
                
            else:
                print("merchant does not exist")
                #m=Merchant("","","")
                m.merchantWindow()
        elif userinput10 == "N":
            userinput12 = input("would you like to register? (y/n): ").strip().lower()
            if userinput12 == "y":
                #m=Merchant("","","")
                m.addMerchant()
                
            elif userinput12 == "n":
                 print("") 
                 print("Goodbye, come back soon")
            else:
                print("Oops! invalid option")
                #m=Merchant("","","")
                m.merchantWindow()
                   
        else:
            print("invalid, option")
            #m=Merchant("","","")
            m.merchantWindow()
            
    def addMerchant(self): #creates a new merchant in the system
         m = Merchant("","","") 
         idlist = list(self.merchantList.keys())
         self.merchantid = idlist[len(idlist)-1] + 1
       
         self.name = input("enter your name: ").strip().capitalize()
         self.category = input("enter your item category (Clothing/Footwear): ").strip().capitalize() 
         if self.category == "Clothing" or self.category == "Footwear":
             self.merchantList[self.merchantid] = [self.name, self.category, "*"]
             print("")
             print("Congrats {}, you have successfully registered as a merchant, your merchant id is {}".format(self.name, self.merchantid))
             print("-----------------------------------------------------------------")
             mp2 = Marketplace("","") #Object of marketplace created to take the program back to the marketplace main menu
             mp2.marketplaceWindow()
         else:
            print("")
            print("Oops!, you have entered an invalid option")
            m.addMerchant()
            
   
    def viewMerchants(self): #To view a list of registered merchants in the marketplace
            
          print("")  
          print("Our list of registered merchants: ")
          print("==========================")
          print ("{:<10} {:<10} {:<10}".format('NAME', 'CATEGORY', 'RATINGS'))
          print("==========================")
          for key, value in self.merchantList.items():
              name, category, ratings = value
              print ("{:<10} {:<10} {:<10} ".format(name, category, ratings)) 
            



"""
The Marketplace has 6 registered merchants and a list of items sold by them


"""

#Marketplace items have also been predefined in a dictionary

class Marketplace:

     def __init__(self, searchItem, merchant,
                  merchantItemList={"007":[ "socks", "clothing",  2.60, 20, "Primark"],"008": ["shirt", "clothing", 12.00, 12, "Fred Perry"],
                "009": ["dress", "clothing", 20.50, 15, "Wallis"], "010": ["pants", "clothing", 14.00, 11, "Zara"],"011": ["loafers", "footwear",  32.00, 10, "Clarks"],
                "012": ["mules", "footwear",  25.00, 20, "Carvela"]}):
        
         self.searchItem = searchItem
         self.merchantItemList = merchantItemList
         self.obj_merchant = merchant #object of class Merchant to show aggregation relationship
         
     def marketplaceWindow(self): #fumction to view marketplace options
            m=Marketplace("","","")
            m1=Merchant("","", "")
            print("*************|| MARKETPLACE ||****************")
            print("1: Item Search")
            print("2: View Registered Merchants")
            print("3: Merchant Options")
            print("4: Back to Main Menu")
            userinput3 = input("Enter the desired option (1/2/3/4): ").strip()
            if userinput3 == "1":
                userinput1 = input("Enter a keyword to search, for example: 'dress':  ").strip().lower()
                
                
             
                m11= Marketplace(userinput1,"")
                m11.searchItemsMP()
                print("")
                print("To place an order, navigate to the main site. ")
                print("In the meantime, take a look around the marketplace")
                print("")
                m.marketplaceWindow()
            
            elif userinput3 == "2":
                merchant = Merchant("","","")
                mp1=Marketplace("", merchant)
                mp1.viewMerchantsMP()
                print("")
                mp2 = Marketplace("","")
                mp2.marketplaceWindow()
            
            elif userinput3 == "3":
               
                m1.merchantWindow()
                
            elif userinput3 == "4":  
                w3 = Website("*************|| wwww.shopeasy.com ||****************", {"001":[ "socks", "clothing",  2.60, 10],"002": ["shirt", "clothing", 12.00, 10],
                "003": ["dress", "clothing", 20.50, 10], "004": ["pants", "clothing", 14.00, 10],"005": ["loafers", "footwear",  32.00, 10],
                "006": ["mules", "footwear",  25.00, 10]}, "")
                w3.websiteWindow()
            else:  
                print("Sorry, invalid option!")
                print("")
                w3 = Website("*************|| wwww.shopeasy.com ||****************", {"001":[ "socks", "clothing",  2.60, 10],"002": ["shirt", "clothing", 12.00, 10],
                "003": ["dress", "clothing", 20.50, 10], "004": ["pants", "clothing", 14.00, 10],"005": ["loafers", "footwear",  32.00, 10],
                "006": ["mules", "footwear",  25.00, 10]}, "")
                w3.websiteWindow()
     
     def searchItemsMP(self): #search function for market place items
        merchantValueList = list(self.merchantItemList.values())
        
        merchantNameList = []   
        for a in range(len(merchantValueList)):
           merchantNameList.append(merchantValueList[a][0])
           
        if self.searchItem in  merchantNameList:
           for b in range (len(merchantValueList)):
              if self.searchItem == merchantValueList[b][0]:
        #Print item details
                print("================================================")
                print ("{} {} available from marketplace".format(merchantValueList[b][3], self.searchItem))
                print("================================================")
                print("")
               
     
           
            
        else:
          print("")
          print("Oops! item ({}) not found in marketplace, see list of available marketplace items:".format(self.searchItem))   
          print("===================================================================")
          print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('ID', 'ITEM', 'CATEGORY', 'PRICE($)', 'QTY', 'MERCHANT'))
          print("===================================================================")
          for key, value in self.merchantItemList.items():
              itemid = key
              item, category, price, qty, merchant = value
              print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(itemid, item, category, price, qty, merchant))
         
     def displayMPLItems(self):  
            print("===================================================================")
            print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('ID', 'ITEM', 'CATEGORY', 'PRICE($)', 'QTY', 'MERCHANT'))
            print("===================================================================")
            for key, value in self.merchantItemList.items():
              itemid = key
              item, category, price, qty, merchant = value
              print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(itemid, item, category, price, qty, merchant))
            
            
     #aggregation relationship with Merchant class to view the marketplace merchants       
     def viewMerchantsMP(self):
          return self.obj_merchant.viewMerchants()

"""
The Website has a marketplace where merchant items are displayed.
It has been implemented in aggregation with class Marketplace.
"""

class Website:

  
    userinput = ""
    userinput1 = ""
    userinput2 = ""
    userinput3 = ""
    w1 = ""
 
   
    
    def __init__(self,url, webItemList, mp): 
           
        self.url = url
        self.webItemList = webItemList
        self.obj_mp = mp #instance of Marketplace object passed as an argument to the website class(aggregation)
        
       
        
    def websiteWindow(self):  #introduces user to website options
        global url
        global userinput1
        global userinput2
        global userinput3
        global w1
        print(self.url)
        print("Welcome to our online clothing and shoe store")
        print("====================================")
        print("1: Main Store")
        print("2: Marketplace")
        print("3: Exit")             
        print("====================================")
    
        
        userinput = input("Enter the desired option (1/2/3): ").strip()
        
        if userinput == "1":
            print("")
            print("======= SHOPEASY STORE ========")
            userinput1 = input("Enter a keyword to search, for example: 'dress': ").strip().lower()

           #arguments passed every time a function is to be used
            w1 = Website("*************|| wwww.shopeasy.com ||****************", {"001":[ "socks", "clothing",  2.60, 10],"002": ["shirt", "clothing", 12.00, 10],
                "003": ["dress", "clothing", 20.50, 10], "004": ["pants", "clothing", 14.00, 10],"005": ["loafers", "footwear",  32.00, 10],
                "006": ["mules", "footwear",  25.00, 10]}, userinput1)
            
            
            w1.searchProductsAll()
            
            #aggregation relationship implemented here
            mp = Marketplace(userinput1,"")# object of Marketplace class passed into website to include marketplace items in the search
            w2 = Website("*************|| wwww.shopeasy.com ||****************", {"001":[ "socks", "clothing",  2.60, 10],"002": ["shirt", "clothing", 12.00, 10],
                "003": ["dress", "clothing", 20.50, 10], "004": ["pants", "clothing", 14.00, 10],"005": ["loafers", "footwear",  32.00, 10],
                "006": ["mules", "footwear",  25.00, 10]}, mp)
            w2.searchProductsMPL()
            
            userinput20 = input("Would you like to place an order (y/n)?: ")
            
            if userinput20 == "y":
                print("")
                print("Our list of items")
                print("================================================")
                print ("{:<10} {:<10} {:<10} {:<10} {:<10}".format('ID', 'ITEM', 'CATEGORY', 'PRICE($)', 'QTY'))
                print("================================================")
                for key, value in self.webItemList.items():
                    itemid = key
                    item, category, price, qty = value
                    print ("{:<10} {:<10} {:<10} {:<10} {:<10}".format(itemid, item, category, price, qty)) 
                
                w2.displayMPLItem()   
                print("-----------------------")
                print("To place an order, please input details below: ")
                it = Item("","", "", "")
                it.isAvailable()
            else:
                #back to main menu
                w2 = Website("*************|| wwww.shopeasy.com ||****************", {"001":[ "socks", "clothing",  2.60, 10],"002": ["shirt", "clothing", 12.00, 10],
                "003": ["dress", "clothing", 20.50, 10], "004": ["pants", "clothing", 14.00, 10],"005": ["loafers", "footwear",  32.00, 10],
                "006": ["mules", "footwear",  25.00, 10]}, "")
                w2.websiteWindow()
                
        elif userinput == "2": #marketplace menu
            mp2 = Marketplace("","")
            mp2.marketplaceWindow()
                
        elif userinput == "3": #exit website and program run
            print("Goodbye, Come back Soon!")
            
     
            
        else:
            
            print("Sorry, invalid option!")
            print("")
            #back to main menu
            w3 = Website("*************|| wwww.shopeasy.com ||****************", {"001":[ "socks", "clothing",  2.60, 10],"002": ["shirt", "clothing", 12.00, 10],
                "003": ["dress", "clothing", 20.50, 10], "004": ["pants", "clothing", 14.00, 10],"005": ["loafers", "footwear",  32.00, 10],
                "006": ["mules", "footwear",  25.00, 10]}, "")
            w3.websiteWindow()
           
            
           
    def searchProductsAll(self): #function to search website items
    
       valuelist = list(self.webItemList.values())
       
       namelist = []
       for i in range(len(valuelist)):
           namelist.append(valuelist[i][0]) 
           
       if userinput1 in namelist:
          for j in range (len(valuelist)):
              if userinput1 == valuelist[j][0]:
        #Print item details
                print("================================================")
                print ("{} {} available from shopeasy".format(valuelist[j][3], userinput1)) #prints amout of items available
                print("================================================")
    
       else:
          print("")
          print("Oops!")
          print("item ({}) not found, see our list of available items:".format(userinput1))   
          print("================================================")
          print ("{:<10} {:<10} {:<10} {:<10} {:<10}".format('ID', 'ITEM', 'CATEGORY', 'PRICE($)', 'QTY'))
          print("================================================")
          for key, value in self.webItemList.items():
              itemid = key
              item, category, price, qty = value
              print ("{:<10} {:<10} {:<10} {:<10} {:<10}".format(itemid, item, category, price, qty)) 
    
    #aggregation relationship with Marketplace to search for marketplace items through the website
    def searchProductsMPL(self):        
       return self.obj_mp.searchItemsMP()

     
    def displayMPLItem(self):        
       return self.obj_mp.displayMPLItems() 
   
    
class Item:
    def __init__(self, itemid, name, merchant, price):
        
        self.websiteList = {"001":[ "socks", "clothing",  2.60, 10,"shopeasy"],"002": ["shirt", "clothing", 12.00, 10, "shopeasy"],
                "003": ["dress", "clothing", 20.50, 10, "shopeasy"], "004": ["pants", "clothing", 14.00, 10, "shopeasy"],"005": ["loafers", "footwear",  32.00, 10, "shopeasy"],
                "006": ["mules", "footwear",  25.00, 10, "shopeasy"]}
        
        self.marketplaceList = {"007":[ "socks", "clothing",  2.60, 20, "Primark"],"008": ["shirt", "clothing", 12.00, 12, "Fred Perry"],
                "009": ["dress", "clothing", 20.50, 15, "Wallis"], "010": ["pants", "clothing", 14.00, 11, "Zara"],"011": ["loafers", "footwear",  32.00, 10, "Clarks"],
                "012": ["mules", "footwear",  25.00, 20, "Carvela"]}
        
        self.itemid = itemid
        
        self.price = price
        
        self.name = name
        
        self.merchant = merchant
    
    def isAvailable(self): #function checks if item is available
       
        
        list1 = list(self.websiteList.keys())
       
        list2 = list(self.marketplaceList.keys())
       
        
        itemid = input("enter item id: ").strip()
        


        if itemid in list1:
            try:
                input2 = int(input("enter qty: "))
            except ValueError:
                   print("invalid entry, check available quantity above")
           
            else:
                if input2 > 0 and input2 < self.websiteList[itemid][3]:
                    
                      
                    
                    print("{} {} added to cart".format(input2, self.websiteList[itemid][0]))
                
                    print("")
                    print("1. Add more items")
                    print("2: Proceed to Checkout")
                    print("")
                    input3 = input("Enter the desired option (1/2): ").strip()
                    if input3 == "1":
                        it1 = Item("","","","")
                        it1.isAvailable() 
                    elif input3 == "2":
                        userinput4 = input("enter your name for quick registration: ").strip()
                        userinput5 = input("enter your delivery address: ").strip()
                        userinput6 = input("enter your email address: ").strip()
                        cust = Customer(userinput4, userinput5, userinput6,"")
                        cust.registerCustomer()
                        sc= ShoppingCart(itemid, self.websiteList[itemid][0], self.websiteList[itemid][4] ,self.websiteList[itemid][2] , input2, (float(input2) * self.websiteList[itemid][2]), "")
                        sc.addToCart()
                        
                        it2 = Item(itemid, self.websiteList[itemid][0], self.websiteList[itemid][4], self.websiteList[itemid][2])
                        ohd = OrderHeader(cust, random.randint(402, 463), datetime.now(), it2, input2,"")
                        ohd.createOrderHeader()
                        ohd.mergeLineItems()
                        ohd.placeOrder()
                        print("")
                        print ("***************************************************************")
                        print ("FOR ADMINISTRATOR'S USE")
                        print ("***************************************************************")  
                        
                        stk1 = Stock(itemid,input2)
                        stk1.updateStock()
                        print("****************************************************************")
                        print("")
                        ohd.cancelOrder()
                    else:
                        print("invalid option")
                        it1 = Item("","","","")
                        it1.isAvailable() 
                        
                elif input2 > self.websiteList[itemid][3]:
                    print("")
                    print("Oops! not enough items to fulfil your request, we have only {} {} left".format(self.websiteList[itemid][3], self.websiteList[itemid][0]))
                    it1 = Item("","", "")
                    it1.isAvailable()
        
        elif itemid in list2:
            try:
                input2 = int(input("enter qty: "))
            except ValueError:
                   print("invalid entry, check available quantity above")
            
            else:
                if input2 > 0 and input2 < self.marketplaceList[itemid][3]:
                    
                    print("{} {} added to cart".format(input2, self.marketplaceList[itemid][0]))
                                 
                    print("")
                    print("1. Add more items")
                    print("2: Proceed to Checkout")
                    print("")
                    input3 = input("Enter the desired option (1/2): ")
                    if input3 == "1":
                        it1 = Item(""," ","","")
                        it1.isAvailable() 
                    elif input3 == "2":
                        userinput4 = input("enter your name for quick registration: ").strip()
                        userinput5 = input("enter your delivery address: ").strip()
                        userinput6 = input("enter your email address: ").strip()
                        cust = Customer(userinput4, userinput5, userinput6,"")
                        cust.registerCustomer()
                        it2 = Item(itemid, self.marketplaceList[itemid][0],self.marketplaceList[itemid][4], self.marketplaceList[itemid][2])
                        
                        sc= ShoppingCart(itemid, self.marketplaceList[itemid][0], self.marketplaceList[itemid][4] ,self.marketplaceList[itemid][2] , 
                                         input2, (float(input2) * self.marketplaceList[itemid][2]), "")
                        sc.addToCart()
                        
                        
                        ohd = OrderHeader(cust, random.randint(402, 463), datetime.now(), it2, input2,"")
                        ohd.createOrderHeader()
                        ohd.mergeLineItems()
                        ohd.placeOrder()
                        print("")
                        print ("***************************************************************")
                        print ("FOR ADMINISTRATOR'S USE")
                        print ("***************************************************************")  
                        
                        stk1 = Stock(itemid,input2)
                        stk1.updateStock()
                        print("****************************************************************")
                        w2 = Website("*************|| wwww.shopeasy.com ||****************", {"001":[ "socks", "clothing",  2.60, 10],"002": ["shirt", "clothing", 12.00, 10],
                        "003": ["dress", "clothing", 20.50, 10], "004": ["pants", "clothing", 14.00, 10],"005": ["loafers", "footwear",  32.00, 10],
                        "006": ["mules", "footwear",  25.00, 10]}, "")
                        w2.websiteWindow()
                     
                    else:
                        print("invalid option")
                        it1 = Item("","","","")
                        it1.isAvailable() 
                       
                elif input2 > self.marketplaceList[itemid][3]:
                    print("")
                    print("Oops! not enough items to fulfil your request, we have only {} {} left".format(self.marketplaceList[itemid][3], self.marketplaceList[itemid][0]))
                    it1 = Item(""," ","", "")
                    it1.isAvailable()    
          
        else:
            print("item id does not exist, refer to list above ")    
            it1 = Item("","","","")
            it1.isAvailable()    


class ShoppingCart:
    
   
    
    def __init__(self, itemid, itemname, merchantname, price, qtyordered, linetotal, lineitemid):
        
        self.merchantname = merchantname
        self.itemid = itemid
        self.itemname = itemname
        self.qtyordered = qtyordered
        self.price = price
        self.linetotal = linetotal
        self.lineitemid = lineitemid
        self.cartdata = {lineitemid:[itemid, itemname, merchantname, price, qtyordered, linetotal]}
        
                         
        
    def addToCart(self):
          
        self.cartdata[self.lineitemid] = [self.itemid, self.itemname, self.merchantname, self.price, self.qtyordered,
                         self.linetotal]
        #print(self.cartdata)
        
   
#class OrderLineItem is part of class OrderHeader . Both make up an Order. Composition relation exists here

class OrderLineItem: 
    
    def __init__(self, it2, qtyordered, lineitemid):
        self.obj_it2 = it2 
        self.qtyordered = qtyordered
        self.lineitemid = lineitemid
    
    def generateLineItem(self): # generates line item selected by customer 
        
        self.lineitemid = random.randint(1000,1999)
        
        linetotal = float(self.qtyordered) * self.obj_it2.price
       
        
        print("====================================================================================")
        print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<13}".format('LINEITEM ID', 'ID', 'NAME', 'MERCHANT', 'PRICE($)', 'QTYORDERED', 'LINE TOTAL'))
        print("====================================================================================")
        print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<13}".format( self.lineitemid, self.obj_it2.itemid, self.obj_it2.name, self.obj_it2.merchant, "{:.2f}".format(self.obj_it2.price),
                "{:.2f}".format(self.qtyordered), "{:.2f}".format(linetotal)))

        
        oli = OrderLineItem("","",self.lineitemid)
        sc = ShoppingCart("", "", "", "", "", "", oli.lineitemid)
        sc.addToCart()


class OrderHeader:
    
    def __init__(self, cust, orderid, orderdate, it2, qtyordered, lineitemid): #object of class customer is passed into order header
        self.cust = cust
        self.orderid = orderid
        self.orderdate = orderdate
        self.obj_oli = OrderLineItem(it2, qtyordered, lineitemid)
    
     
    
    def createOrderHeader(self):
        print("---------------------------------------------")
        print("Hello {}, here is your order  details".format(self.cust.name))
        print("Customer id: {}".format(self.cust.custid))
        print("Address: {} ".format(self.cust.address))
        print("email: {} ".format(self.cust.email))
        print("Order id: {}".format(self.orderid)) 
        print("Order date {}".format(self.orderdate))
        print("---------------------------------------------")
    
    def mergeLineItems(self): #composition relationship with class OrderLineItem.
        return self.obj_oli.generateLineItem()
    
    
   
        
    def placeOrder(self): #this function places order and should ideally communicate with  class Checkout
        print("")
        print("1. Submit Order")
        print("2: Cancel Order")
        print("")
        input3 = input("Enter the desired option (1/2): ").strip()
        if input3 == "1":
            
            print("Your order {} is on its way to you, Thank you {} for shopping with us".format(self.orderid, self.cust.name))
            #back to main menu
            
            return
            
            
        elif input3 == "2":
            print("your order has been cancelled")
            #back to main menu
            w2 = Website("*************|| wwww.shopeasy.com ||****************", {"001":[ "socks", "clothing",  2.60, 10],"002": ["shirt", "clothing", 12.00, 10],
                "003": ["dress", "clothing", 20.50, 10], "004": ["pants", "clothing", 14.00, 10],"005": ["loafers", "footwear",  32.00, 10],
                "006": ["mules", "footwear",  25.00, 10]}, "")
            w2.websiteWindow()
            
        else:
            print("invalid option")
            #back to main menu
            w2 = Website("*************|| wwww.shopeasy.com ||****************", {"001":[ "socks", "clothing",  2.60, 10],"002": ["shirt", "clothing", 12.00, 10],
                "003": ["dress", "clothing", 20.50, 10], "004": ["pants", "clothing", 14.00, 10],"005": ["loafers", "footwear",  32.00, 10],
                "006": ["mules", "footwear",  25.00, 10]}, "")
            w2.websiteWindow()
            return
       
            
class Customer:
    def __init__(self, name, email, address, custid ):
        self.name = name
        self.email = email
        self.address = address
        self.custid = custid
        
    def registerCustomer(self): #generates a customer id after customer registration
        
        self.custid = random.randint(500, 600)
        
    
            
    
class Stock:
    def __init__(self, itemid, orderedqty):
        
        
        self.orderedqty = orderedqty
        self.itemid = itemid
        
        self.websiteList = {"001":[ "socks", "clothing",  2.60, 10,"shopeasy"],"002": ["shirt", "clothing", 12.00, 10, "shopeasy"],
                "003": ["dress", "clothing", 20.50, 10, "shopeasy"], "004": ["pants", "clothing", 14.00, 10, "shopeasy"],"005": ["loafers", "footwear",  32.00, 10, "shopeasy"],
                "006": ["mules", "footwear",  25.00, 10, "shopeasy"]}
        
        self.marketplaceList = {"007":[ "socks", "clothing",  2.60, 20, "Primark"],"008": ["shirt", "clothing", 12.00, 12, "Fred Perry"],
                "009": ["dress", "clothing", 20.50, 15, "Wallis"], "010": ["pants", "clothing", 14.00, 11, "Zara"],"011": ["loafers", "footwear",  32.00, 10, "Clarks"],
                "012": ["mules", "footwear",  25.00, 20, "Carvela"]}
        
       
        
    def updateStock(self):
         
        
         list1 = list(self.websiteList.keys())
       
         list2 = list(self.marketplaceList.keys())
        
         if self.itemid in list1:
        
             updatedqty =  self.websiteList[self.itemid][3] - self.orderedqty    
             self.websiteList[self.itemid][3] = updatedqty
           
            
             print("==========================")
             print ("{:<10} {:<10} {:<10} {:<10} {:<10}".format('ITEM ID', 'ITEM NAME', 'CATEGORY', 'PRICE', 'QTY' ))
             print("==========================")
             for key, value in self.websiteList.items():
                itemid, name, category, price, qty = value
                print ("{:<10} {:<10} {:<10} {:<10} {:<10} ".format(itemid, name, category, price, qty))
        
        
         elif self.itemid in list2:
             
            updatedqty =  self.marketplaceList[self.itemid][3] - self.orderedqty 
            self.marketplaceList[self.itemid][3] = updatedqty
            
            
            print("==========================")
            print ("{:<10} {:<10} {:<10} {:<10} {:<10}".format('ITEM ID', 'ITEM NAME', 'CATEGORY', 'PRICE', 'QTY' ))
            print("==========================")
            for key, value in self.marketplaceList.items():
                itemid, name, category, price, qty = value
                print ("{:<10} {:<10} {:<10} {:<10} {:<10} ".format(itemid, name, category, price, qty))
                        
         else:
            return
    

#Initial Test Data

w2 = Website("*************|| wwww.shopeasy.com ||****************", {"001":[ "socks", "clothing",  2.60, 10],"002": ["shirt", "clothing", 12.00, 10],
                "003": ["dress", "clothing", 20.50, 10], "004": ["pants", "clothing", 14.00, 10],"005": ["loafers", "footwear",  32.00, 10],
                "006": ["mules", "footwear",  25.00, 10]}, "")
w2.websiteWindow()

  
        
        
            





        
        