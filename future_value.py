future_value = float(input('Enter the desired future value:\n'))
rate = float(input('Enter the annual interest rate:\n'))
years = int(input('How many years should your money grow?\n'))
present_value = future_value / (1.0 + rate) ** years
print('YOU WILL NEED TO DEPOSIT THIS AMOUNT:\n', (format(int (present_value), ',.2f')))
