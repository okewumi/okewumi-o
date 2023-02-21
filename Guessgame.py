import random
a=random.randint(1,31)
b=1
while b<=5:
    c=int(input('Enter your guess: '))
    if c==a:
        
        print("You guesses right in",b,'Trials')
        
        break
    elif c!=a and b==5:
        print ('Opps try again later')
    elif c>a:    
        print ("Your guess is high, guess lower")
    elif c<a:
               
        print ("Your guess is low, guess higher")
               
                   
        print("please guess between 1 and 30")
    b+=1


