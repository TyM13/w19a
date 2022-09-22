def fizzbuzz(number):      
    if((number % 3 == 0)and number % 5 == 0):
        print(number,'fizzbuzz')
    elif(number % 5 == 0):
        print(number,'buzz')
    elif(number % 3 == 0):
        print(number,'fizz')
    else:
        print(number,'something went wrong')    

random_numbers = [3,5,7,9,30,300,25,54,60,22,1535,12464567,123,122,150]

for number in random_numbers:
    fizzbuzz(number)
