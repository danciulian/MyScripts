"""01. Prime number"""

# nums = range(1, 1000)
#
#
# # print(list(nums))
#
# def is_prime(num):
#     for x in range(2, num):
#         if (num % x) == 0:
#             return False
#     return True
# #     returns True if you traverse the entire loop without finding a factor
# print(is_prime(29))
# # primes = filter(is_prime, nums)
# # print(primes)
# # print(list(primes))

"""02. sys module"""

import sys
print("the script has the name:", sys.argv[0])

