amountOfPurchase = 'amt'
stateSalesTax = 'st'
countySalesTax = 'ct'
totalSalesTax = 'tst'
totalSale = 'tts'
amt = float(input('HOW MUCH IN TOTAL IS THE COST OF YOUR SHOPPING?\n'))
st = 0.05 
ct = 0.025
tst = st + ct
tts = amt + tst
print("YOUR AMOUNT OF PURCHASE WAS $", format(amt, ',.2f'), sep='')
print("YOUR TOTAL SALES TAX IS $", format(tst, ',.3f'), sep='', end=' ')
print("WHERE THE COUNTY SALES TAX WAS $", format(ct, ',.3f'), sep='', end=' ')
print("AND THE STATE SALES TAX WAS $", format(st, ',.2f'), sep='')
print("SO YOUR TOTAL SALES IS $", format(tts, ',.2f'), sep='')