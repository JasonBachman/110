'''
Jason Bachman
CSC 110 - Homework 2 - Programming in Python
Due 2/4/19
'''
#gets the sale price
price = int(input("Enter amount of sale:"))
#Checks the price of sale and assigns the correct discount
if price<=2000:
	print("Your discounted price is: $",price)
elif price>2000 and price<=4000:
	price=price*.8
	print("Your discounted price is: $",price)
elif price>4000 and price<=8000:
	price=price*.65
	print("Your discounted price is: $",price)
else:
	price=price*.5
	print("Your discounted price is: $",price)

#prints the new total
