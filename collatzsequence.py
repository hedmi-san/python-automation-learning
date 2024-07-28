#solution neif
# def collatz(number): 
#     while(True):
#         if(number  == 1): 
#             return 1
#             break
#         else:
#             if(number % 2 == 0):
#                 number = number // 2
#                 print(number)
#             else:
#                 number = number*3 +1
#                 print(number)
# print('Enter a number',end='')
# number=input()
# collatz(int(number))


#solution recursive
import sys
def collatz(number):
    if(number == 1):
        return 1
    print(number)
    if(number % 2 == 0):
        return collatz(number // 2)
    else:
        return collatz(number*3+1)

print('Enter a number')
number=input()
print(collatz(int(number))) 