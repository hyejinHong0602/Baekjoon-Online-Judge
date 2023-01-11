
#2750
# import sys
# from collections import Counter
#
# n = int(sys.stdin.readline()) # n은 입력받을 숫자 개수 (홀수)
# n_list = []
#
# for i in range(n):
#     a = int(sys.stdin.readline()) # 숫자 하나씩 입력받기
#     n_list.append(a) # 리스트에 넣어주기
#
#
# n_list.sort() # 정렬
#
# for i in range(n):
#         print(n_list[i])

#2587
# import sys
# from collections import Counter
# n_list = []
# sum = 0
#
# for i in range(5):
#     a = int(sys.stdin.readline()) # 숫자 하나씩 입력받기
#     n_list.append(a) # 리스트에 넣어주기
#     sum += a
#
# print(sum/5)
# print(n_list[2])

#25305
# import sys
#
# n,k = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split(' ')))
#
# a.sort()
# print(a[n-k])

# 2751
# import sys
#
# n = int(sys.stdin.readline())
# n_list = []
#
# for i in range(n) :
#         a = int(sys.stdin.readline())  # 숫자 하나씩 입력받기
#         n_list.append(a)
# n_list = sorted(n_list)
#
# for i in range(n) :
#         print(n_list[i])

# 10989 -- 이거 틀림. memory 오류

# import sys
#
# count_dict = {}
# n_list=[]
# n = int(sys.stdin.readline())
# for i in range(n):
#     a = int(sys.stdin.readline()) # 숫자 하나씩 입력받기
#     n_list.append(a) # 리스트에 넣어주기
#
#
# for num in n_list:
#         if num in count_dict:
#                 count_dict[num] += 1
#
#         else:
#                 count_dict[num] = 1
#
# result = []
#
# for num in range(n + 1):
#         while num in count_dict and count_dict[num] != 0:
#                 result.append(num)
#                 count_dict[num] -= 1
#
# print(result)


#11651
# import sys
#

# n_list=[]
# n = int(sys.stdin.readline())
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split()) # 숫자 하나씩 입력받기
#
#     n_list.append([a,b]) # 리스트에 넣어주기
#
# n_list.sort(key=lambda x :(x[1], x[0]))
#
# for i in range(n) :
#         print(n_list[i][0],n_list[i][1])

# 10814
# import sys
#
# n_list=[]
# n = int(sys.stdin.readline())
# for i in range(n):
#     a, b = map(str, sys.stdin.readline().split()) # 숫자 하나씩 입력받기
#
#     n_list.append([int(a),b]) # 여기를 int 로 해서 넣어줘야 에러가 안남.
# n_list.sort(key=lambda x : x[0])
#
# for i in range(n) :
#         print(n_list[i][0], n_list[i][1])

# 1181 - sorted 알파벳 정렬도 됨.

# import sys
#
# n_list=[]
# n = int(sys.stdin.readline())
# for i in range(n):
#     a = sys.stdin.readline().strip() # sys.stdin.readline() 여기서 개행문자 제거 .strip()
#     n_list.append(list[a, len(a)])
# n_list=list[set(n_list)]
# n_list.sort(key=lambda x :(x[1], x[0]))

#----------------------------
# import sys
#
# n_list=[]
# n = int(sys.stdin.readline())
# for i in range(n):
#     a = sys.stdin.readline().strip() # sys.stdin.readline() 여기서 개행문자 제거 .strip()
#     n_list.append(a)
# n_list=set(n_list) # 중복된 단어 제거
#
# k=[]
# for i in n_list :
#         k.append(i)
# k_list=[]
#
# for i in range(len(k)):
#         k_list.append([k[i], len(k[i])])
#
#
# k_list=sorted(k_list) # 사전순으로 한번 정렬
# k_list.sort(key = lambda x : x[1]) # 글자수로 한번 정렬
# for i in range(len(k_list)) :
#         print(k_list[i][0])

#18870

# import sys
#
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split(' '))) # sys.stdin.readline() 여기서 개행문자 제거 .strip()
#
# a_sort=sorted(list(set(a)))
#
# dic={}
#
# for i in range(len(a_sort)) :
#         dic[a_sort[i]] = i
#
# for i in range(n) :
#         print(dic[a[i]], end=' ')
#


# 카운트정렬 참고
# import sys
#
# count_dict = {}
# n_list=[]
# n = int(sys.stdin.readline())
# for i in range(n):
#     a = int(sys.stdin.readline()) # 숫자 하나씩 입력받기
#     n_list.append(a) # 리스트에 넣어주기
#
#
# for num in n_list:
#         if num in count_dict:
#                 count_dict[num] += 1
#
#         else:
#                 count_dict[num] = 1
#
# result = []
#
# for num in range(n + 1):
#         while num in count_dict and count_dict[num] != 0:
#                 result.append(num)
#                 count_dict[num] -= 1
#
# print(result)

#10989
# import sys
#
# buffer = [0 for i in range(10000)]
#
# n = int(sys.stdin.readline())
# for i in range(n):
#     a = int(sys.stdin.readline()) # 숫자 하나씩 입력받기
#     buffer[a+1]+=1
#
# for i in range(10000):
#     if buffer[i] != 0:
#         for j in range(buffer[i]) :
#             print(i-1)