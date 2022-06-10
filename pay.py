highestHour = 40
overTimeRate = 1.5
hoursWorked = float(input("HOW MANY HOURS DID YOU WORK:\n"))
pay = highestHour * 40

if hoursWorked > highestHour:
    overtimePay = (hoursWorked - highestHour) * overTimeRate
    grossPay = pay + overtimePay 
    print("YOUR OVERTIME PAY IS $", format(overtimePay, ",.2f"), sep='', end='')
    print(" AND YOUR GROSS PAY IS $", format(grossPay, ",.2f"))
else:
    grossPay = highestHour * overTimeRate
    print(" AND YOUR GROSS PAY IS $", format(grossPay, ",.2f"))

