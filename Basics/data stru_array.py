exp = {
    'Jan': 2200,
    'Feb': 2350,
    'Mar': 2600,
    'Apr': 2130,
    'May': 2190
}
#Feb to Jan expense
print('The expense of Feb to Jan is: ', exp['Jan']-exp['Feb'])
print('Total expense of first quarter is: ', exp['Jan']+exp['Feb']+exp['Mar'])
f = True
for n in exp:
    if exp[n] == 2000:
        print('The expense of the month ', n, 'was 2000')
        f = False
if f:
    print('Expense of no month is 2000')
exp['June'] = 1980
exp['Apr'] = exp['Apr'] - 2005
print(exp)
