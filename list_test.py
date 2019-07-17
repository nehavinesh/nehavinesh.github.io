#imports the ability to get a random number (we will learn more about this later!)
import random


names = ["Priyanka", "Marcelle", "Lucy", "Nicole", "Neha", "Shriya"]
business = ["Pizzeria", "Cupcakeria", "Wingeria", "Freezeria", "Burgeria", "Sushiria"]

num1 = random.randint(0,5)
num2 = random.randint(0,5)

company_name = (names[num1]+"'s", business[num2])

for i in range(len(company_name)):
    print(company_name[i], end =" ")

print()
