#Take the number of months to save for, then the number of days to save for within the month, accept the amounts to be saved for the number of days. Print the total for each month saved, print the total for the year saved.

month = int(input('Enter the number of months'))
month_days = []
for i in range(month):
    print('Select the number of days for month ',(i+1))
    month_days.append(int(input('Enter the days')))

sum_amount =[]
sum = 0

#collecting data for month days

for i in range(len(month_days)):
    print('Month ', (i+1), '\n')
    for i in range(month_days[i]):
        print('Savings for day',(i+1))
        sum = sum + int(input('Enter amount'))
    sum_amount.append(sum)
    sum = 0
                   


print('month:',month)
print('Day in month',month_days)

for i in range(month):
    print('Month', (i+1), 'Saving',sum_amount[i] )




