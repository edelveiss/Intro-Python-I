your_number = int(input("Enter an integer number: "))


def is_prime(num):
    num_is_prime = True
    if num >1:
        for k in range(2,int(num/2)):
            if num % k == 0:
                num_is_prime = False
    else:
        num_is_prime = False
    return num_is_prime

       
if is_prime(your_number):
    print(your_number, " is a prime number")
else:
    print(your_number, " is not a prime number")





            
       





        

# for index, element in enumerate(bool_list):
#     print(f"index {index} number {element}")

