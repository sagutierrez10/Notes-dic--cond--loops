# 1. Basic - Print all intergers from 0 to 150
for x in range(0,151):
    print(x)
# 2. Multiples of Five- Print all the multiples of 5 from 5 to 1,000
for x in range(5,1001,5):
    print(x)
# 3.Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range (1,101,1):
    if i % 10 == 0:
        print ('Coding Dojo')
    elif i % 5 == 0:
        print ('Coding')
    else:
        print(i)    

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def add_odds_function():
    for i in range(0,500000,1):
        sum=0
        if i%2 == 1:
            sum = sum + i
    print(sum)
add_odds_function()

# 5.Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def down_by_four():
    y = 2018
    while y > 0:
        print(y)
        y = y - 4
down_by_four()

# 6.Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
def flexible_counter(low, high, mult):
    for i in range(low, high):
        if i % mult == 0:
            print(i)
flexible_counter(2, 9, 3)
