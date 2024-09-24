#Import numpy and set seed
import numpy as np
from numpy import random
np.random.seed(123)


#Lets use randint() to simulate a dice

print(np.random.randint(1,7))

#Repeat it again to see if the second throw is any different

print(np.random.randint(1,7))

#Lets use If-elif-else statements too to make it fun

# first, lets set our starting step as 50. Remember we are on the empire state building.
step = 50

#Roll the dice, use randint to create the variable "dice"
dice = np.random.randint(1,7)

#If dice is 2 or 1 you will go one step down from 50 (remember step)
if dice <= 2 :
    # We need to make sure that the step can never go below O, here is the code to do just that

    step = max(0, step - 1)

    step = step - 1
#If dice is 3,4 or 5, you will go one step up from 50
elif 5 >= dice :
     step = step + 1
else :
    step = step + np.random.randint(1, 7)
    print(dice)
    print(step)
#You threw 6, which activated the else statement, you throw again and now you got 3 = 53

tails = [0]
for x in range(10) :
    coin = np.random.randint(0,100)
    tails.append(tails[x] + coin)
    print(tails)

#Now lets visualise the results with matplotlib
import matplotlib.pyplot as plt
plt.plot(tails)
plt.show()
#Ahh looks nice eh!














