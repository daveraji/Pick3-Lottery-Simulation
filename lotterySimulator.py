import Pick3
import pandas as pd
import random


days = 1 #int(input("how many times you wanna run for?"))
numguesses = 20 #int(input('number of random guesses'))
c=0
dollars=0
expected_prize=0

#send generate number of gueses for the day
def generateGuesses(num):
    '''
    Automatically generate random guesses for you to play on a given day
    '''
    guesses = [0]*num
    for i in range(num):
        guesses[i]=str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        #guesses[i]=input('guess') #input gueses yourself
        #guesses[i] = str(100+i)
    return guesses

#set up dataframe
df = pd.DataFrame(columns=['days', 'wins'])
for a in range(days):
    df.loc[a] = [a] + [0]*1

#print(df)
#run test and collect results
#for pick in guesses:
for n in range(days):
    count, result = Pick3.pick3(generateGuesses(numguesses))
    dollars+=numguesses
    for j in range(numguesses):
        if count[j][4] !=0:
            df.loc[c][1] = count[j][4]
            print(count[j][0]) #print winning number
            expected_prize+=122
    c+=1

#print(df)
print(dollars, 'dollars spent and you won', expected_prize)
