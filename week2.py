# # 10872
# import sys
#
# n = int(sys.stdin.readline())
# res = 1
# for i in range(1, n+1) :
#     res = res*i
#
# print(res)

# # 10870
# import sys
#
# n = int(sys.stdin.readline())
# f_1 = 0
# f_2 = 1
# f_n = 0
# if n > 2 :
#     f_1 = 1
#     f_2 = 1
#     for i in range(2, n) :
#         # print(f_1, f_2)
#         f_n = f_1+f_2
#         res = f_n
#         f_1 = f_2
#         f_2 = f_n
#
# elif n == 2:
#     f_n = f_1+f_2
#     res = f_n
# else :
#     res = n
#
# print(res)


# 2447

# import sys
#
# n = int(sys.stdin.readline())
#
# star_list = ['***', '* *', '***']
#
# if n == 3:
#     for i in range(3):
#         print(star_list[i])
# else :
#
# n = int(input())
#
#
# def star(l):
#     if l == 3:
#         return ['***', '* *', '***']
#
#     arr = star(l // 3)
#     stars = []
#
#     for i in arr:
#         stars.append(i * 3)
#
#     for i in arr:
#         stars.append(i + ' ' * (l // 3) + i)
#
#     for i in arr:
#         stars.append(i * 3)
#
#     return stars
#
#
# print('\n'.join(star(n)))


#25501

#include <stdio.h>
#include <string.h>
# import sys
#
# n = sys.stdin.readline()
#
# def recursion(s, l, r):
#     global cnt  # 함수 내에서 전역 변수로 cnt를 활용하기 위해 global로 명시해준다.
#     cnt += 1
#
#     if l >= r:
#         return 1
#     elif s[l] != s[r]:
#         return 0
#     else:
#         return recursion(s, l + 1, r - 1)
#
#
# def isPalindrome(s):
#     return recursion(s, 0, len(s) - 1)
#
#
# for i in range(int(n)):
#     cnt = 0
#     a = sys.stdin.readline().strip('\n')
#     print(isPalindrome(a), cnt)

# 11729

# import sys
# n = int(sys.stdin.readline())


# 10989 - 카운팅 정렬 (런타임에러(index error)가 나는데 이유를 모르겠음)
# import sys
#
# buffer = [0 for i in range(10001)]
#
# n = int(sys.stdin.readline())
# for i in range(n):
#     a = int(sys.stdin.readline()) # 숫자 하나씩 입력받기
#     buffer[a+1]+=1
#
# for i in range(10001):
#     if buffer[i] != 0:
#         for j in range(buffer[i]) :
#             print(i-1)


# import sys
#
# buffer = [0 for i in range(10001)]
#
# n = int(sys.stdin.readline())
# for i in range(n):
#     a = int(sys.stdin.readline()) # 숫자 하나씩 입력받기
#     buffer[a]+=1
#
# for i in range(10001):
#     if buffer[i] != 0:
#         for j in range(buffer[i]) :
#             print(i)

