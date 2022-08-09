file = 'expenses.txt'
avgFile = 'monthly_avg.txt'

def display():
    with open(file,'r') as f:
        for line in f:
            print(line,end='')

def calculateExpenditure():
    total = 0
    with open(file,'r') as f:
        for line in f:
            if not line.startswith('@') and not line.startswith('-'):
                exp = float(line)
                total = total + exp
    return total

def calculateIncome():
    total = 0
    with open(file,'r') as f:
        for line in f:
            if line.startswith('-'):
                exp = float(line)
                total = total + exp
    return total*-1

def calculateDays():
    days = 0
    with open(file,'r') as f:
        for line in f:
            if line.startswith('@'):
                days = days + 1
    return days

def getStartAndEndDay():
    days = list()
    with open(file,'r') as f:
        for line in f:
            if line.startswith('@'):
                days.append(line[1:-1])
    return (days[0],days[len(days)-1])


def showRecord():
    duration = getStartAndEndDay()
    print(f'RECORD FROM {duration[0]} TO {duration[1]}')
    days = calculateDays()
    print('Total number of days =',days)
    expenditure = calculateExpenditure()
    print('Total spending =',expenditure)
    income = calculateIncome()
    print('Total earning =',income)
    avg = float(expenditure/days)
    print('Average spending per day =',avg)

def addToFile():
    with open(avgFile,'a') as f:
        duration = getStartAndEndDay()
        f.write(f'{duration[0]} TO {duration[1]}\n')
        f.write(f'\tNumber of days = {calculateDays()}\n')
        f.write(f'\tTotal spending = {calculateExpenditure()}\n')
        f.write(f'\tTotal earning ={calculateIncome()}\n')
        f.write(f'\tAverage spending per day = {float(calculateExpenditure())/calculateDays()}\n')
        f.write(f'\n-----------------------------\n')
        print('Added successfully')
    with open(file,'w') as f:
        f.write('')

showRecord()
saveToFile = input('\n\nDo you want to add the record to file?? (y for Yes) : ')
if saveToFile == 'y':
    addToFile()

print('Thank you!!')


# RULES:
# adding expenses to the file:
# Use '@' in the starts of date
# if expeniture then write normally
# if income then write '+' in the starting without any spaces