

# def prime(n):
#     if n < 2:  # 判断是否大于1的整数，且1不是素数
#         result = "false"
#     else:
#         for i in range(2, n):
#             if n % i == 0:  # 判断2——i是否有能被整除
#                 result = "false"
#                 break
#         else:
#             result = "true"
#     return result
#
# n = int(input("100"))
# print(prime(n))




def count(args,sum1):
    count1 = 0
    for i in range(0, len(args)):
        if args[i] < 0:
            count1 += 1
        if args[i] >= 0:
            sum1 += args[i]
    count2 = sum1 / (len(args) - count1)
    round(count2, 1)
    return count1, count2

n = 5
num = [1, 2, 3, 4, 5]
sum1 = 0
print(count(num,sum1))


# def judge(n):
#     if n == 0:
#         result = "false"
#     elif (n & (n - 1) == 0):
#         result = "true"
#     else:
#         result = "false"
#     return result
# print(judge(8))
