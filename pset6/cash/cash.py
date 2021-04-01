from cs50 import get_float
change = 0.00
quarters = 0.25
dimes = 0.10
nickels = 0.05
pennies = 0.01
coins = 0
while True:
    change = get_float("Change owed:")
    if change > 0.00:
        break
while(change >= quarters):
    change = change - quarters
    coins += 1
while( change >= dimes):
    change = change - dimes
    coins += 1
while( change >= nickels):
    change = change - nickels
    coins += 1
while( change >= pennies):
    change = change - pennies
    coins += 1
print(f"Number of coins used:{coins}\n",end="" )
