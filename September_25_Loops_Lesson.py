#Create for loop which uses range() to iterate to 20
#Inside the loop print out iteration number
#replace the range vallue to be a user value, make sure it is an integer
# Add if statement to check if iteration number is even or odd



#For loop
user_count = int(input("How many iterations?"))
for i in range(1,user_count +1):
    if i % 2 == 0:
        print(f"number {i} is divisible by 2")
    else:
        print(f"number {i} is not divisible by 2")

#While loop
user_while_count = int(input("What's the max value?"))
counter = 0
while counter <= user_while_count:
    if counter % 2 == 0:
        print(f"number {counter} is divisible by 2")
    else:
        print(f"number {counter} is not divisible by 2")
    counter += 1