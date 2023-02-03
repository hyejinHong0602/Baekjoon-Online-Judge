# import sys
#
# def binary_search(target, data):
#     data.sort()
#     start = 0
#     end = len(data) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[mid] == target:
#             return 1 # 함수를 끝내버린다.
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid -1
#
#     return None
#
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split(' ')))
#
# m = int(sys.stdin.readline())
# b = list(map(int, sys.stdin.readline().split(' ')))
#
# for i in range(m) :
#     if binary_search(b[i], a) == 1 :
#         print(1, end = " ")
#     else :
#         print(0, end=" ")
#
#
# # 10815
# #import sys
# # n = int(sys.stdin.readline())
# # a = list(map(int, sys.stdin.readline().split(' ')))
# #
# # m = int(sys.stdin.readline())
# # b = list(map(int, sys.stdin.readline().split(' ')))
# #
# # for i in range(m) :
# #     if b[i] in a :
# #         print(1, end=' ')
# #     else:
# #         print(0, end=' ')
#
# # 이진탐색
# import sys
# n = int(sys.stdin.readline())
# left = 0
# right = n-1
#
# a = list(map(int, sys.stdin.readline().split(' ')))
# a.sort()
#
# m = int(sys.stdin.readline())
# b = list(map(int, sys.stdin.readline().split(' ')))
#
# for i in range(m) :
#     target = b[i]
#     print(target)
#     res = 0
#     # print(target)
#     while left <= right:
#         mid = (left + right) // 2
#         if a[mid] == target:
#             res=1
#             break
#         elif a[mid] > target:
#             right = mid-1
#         else :
#             left = mid+1
#     if res == 1:
#         print(1, end= " ")
#     else :
#         print(0, end= " ")
#
#
# def binary_search(target, data):
#     data.sort()
#     start = 0
#     end = len(data) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[mid] == target:
#             return 1 # 함수를 끝내버린다.
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid -1
#
#     return None
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split(' ')))
#
# m = int(sys.stdin.readline())
# b = list(map(int, sys.stdin.readline().split(' ')))
#
# for i in range(m) :
#     if binary_search(b[i], a) == 1 :
#         print(1, end = " ")
#     else :
#         print(0, end=" ")


# 14425
# import sys
# n, m= map(int, sys.stdin.readline().split())
# s = {}
# target_m = []
# res = 0
# for i in range(n) :
#     word = sys.stdin.readline().rstrip()
#     s[word] = 0
#
# for j in range(m):
#     target = sys.stdin.readline().rstrip()
#     target_m.append(target)
#
# for k in range(m) :
#     if target_m[k] in s :
#         res+=1
#
# print(res)

# 10816


# 1764
# 못들은 사람 중에서 보지도 못한 사람 뽑아내
# import sys
# n, m= map(int, sys.stdin.readline().split())
# s = {}
# target_m = []
# res = 0
# ans = []
# for i in range(n) :
#     word = sys.stdin.readline().rstrip()
#     s[word] = 0
#
# for j in range(m):
#     target = sys.stdin.readline().rstrip()
#     target_m.append(target)
#
# for k in range(m) :
#     if target_m[k] in s :
#         ans.append(target_m[k])
#         res+=1
#
# print(res)
# ans.sort()
# for _ in range(len(ans)) :
#
#     print(ans[_])

# 1269
# import sys
# n, m= map(int, sys.stdin.readline().split())
#
# a = set(map(int, sys.stdin.readline().split(' ')))
# b = set(map(int, sys.stdin.readline().split(' ')))
#
# a_num = len(a-b)
# b_num = len(b-a)
#
# print(a_num+b_num)

# 11478
# from itertools import combinations
# import sys
#
# a = sys.stdin.readline().rstrip()
# print(a)
# set_a = [char for char in a]
# print(set_a)
# res=[]
# for i in range(len(set_a)+1):
#     res = res+list(combinations(set_a,i))
#
# print(len(set(res)))
## 틀림림
# s = sys.stdin.readline().rstrip()
# total = set()
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         total.add(s[i:j+1]) #i번째 문자부터 부분문자열 구하기
#
# print(len(total))

# 1620
import sys
n, m= map(int, sys.stdin.readline().split())

p_dict={}
p_dict_re = {}
for i in range(n) :
    a = sys.stdin.readline().rstrip()
    p_dict[a] = i+1
    p_dict_re[str(i+1)] = a


# p_dict_re={str(v):k for k,v in p_dict.items()}

for j in range(m) :
    b = sys.stdin.readline().rstrip()
    if b in p_dict.keys() :
        print(p_dict[b])
    else :
        print(p_dict_re[b])
