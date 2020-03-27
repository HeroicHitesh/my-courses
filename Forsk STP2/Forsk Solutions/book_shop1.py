"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number    Book Title              Author      Quantity  Price per Item
    34587           Learning Python,        Mark Lutz   4           40.95
    98762           Programming Python,     Mark Lutz   5           56.80
    77226           Head First Python,      Paul Barry  3           32.95
    88112           Einführung in Python3,  Bernd Klein 3           24.99    
    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 

    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 98.85), ('88112', 74.97)]
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.
    
    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 108.85), ('88112', 84.97)]
    
    

  Hint: 
    Write a Python program using lambda and map.
    orders = 
    [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
    ]

"""

    
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
           ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
         ]




order_summary = list(map(lambda x: (x[0], round(x[2] * x[3],2)), orders))
print(order_summary)


min_order = 100

invoice_totals = list(map(lambda x: x if x[1] >= 100 else (x[0], x[1] + 10), order_summary))
print(invoice_totals)


# or 

print(list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), 
                    map(lambda x: (x[0],round(x[2] * x[3],2)), orders))))







# Alternative Solution without map, lambda 

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
           ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
         ]

for order in orders :
    #print (order)
    #print (order[0],order[2]*order[3])
    print (order[0],round(order[2]*order[3],2))
  
    
invoice = []
for order in orders :
    orderNum = int(order[0])
    quantity = order[2]
    price = order[3]
    total = quantity * price
    if total<=100:
        total =total + 10
    else:
        total
        
    invoice.append((orderNum,round(total,2)))  
    
print(invoice)    










