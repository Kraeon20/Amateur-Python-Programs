from os import sep


item1= float(input('PRICE1:\n'))
item2= float(input('PRICE2:\n'))
item3= float(input('PRICE3:\n'))
item4= float(input('PRICE4:\n'))
item5= float(input('PRICE5:\n'))
subTotal = (item1 + item2 + \
item3 + item4 + item5)
salesTax = 0.07 * subTotal
total = subTotal - (0.07 * subTotal)
print("SUBTOTAL IS $", format(subTotal, ",.2f"), sep='', end='')
print("TOTAL IS $", format(total, ",.2f"), sep='', end='')
print("SALES TAX WAS $", format(salesTax, ",.2f"), sep='')