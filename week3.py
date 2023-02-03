# 2798
# 풀이방법 : 하나하나 다 더해서 m 을 넘는 숫자는 패스하고, m이 넘지 않는 합은 새로운 배열에 저장. 그리고 마지막에 그 배열의 max 값 출력.
# 풀이 이후 찾아본 방법 : 순열 조합 라이브러리 itertools 모듈의 combinations 함수 사용.
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split(' ')))
# sum_3=[]
#
# for i in range(n) :
#     for j in range(i+1, n) :
#         for k in range(j+1, n) :
#             if a[i] + a[j] + a[k] > m :
#                 continue
#             else :
#                 sum_3.append(a[i] + a[j] + a[k])
# print(max(sum_3))

# # 풀이 이후 찾아본 방법 : 순열 조합 라이브러리 itertools 모듈의 combinations 함수 사용.
# import sys
# from itertools import combinations
#
# n, m = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split(' ')))
# sum_3 = []
#
# for sum_num in combinations(a, 3) :
#     if int(sum(sum_num)) > m :
#         continue
#     else:
#         sum_3.append(sum(sum_num))
# print(max(sum_3))

# 7568

# # 접근 방법 : 몸무게랑 키 각각으로 순위를 매긴 다음, 그 중에 더 높은 숫자가 본인의 덩치 등수.
# import sys
#
# n = int(sys.stdin.readline())
# n_list=[]
# for i in range(n) :
#     x, y = map(int, sys.stdin.readline().split())
#     n_list.append((x,y))
#
# for j in range(n) :
#     rank = 1
#     for k in range(n) :
#         if n_list[j][0] != n_list[k][0] and n_list[j][1] != n_list[k][1]:
#             if n_list[j][0] < n_list[k][0] and n_list[j][1] < n_list[k][1]:
#                    rank = rank + 1
#     print(rank)

# # 1018
# # 접근방법 : 시작점이 b인 경우, w인 경우로 나눠서 둘중에 더 적게 칠하는 개수를 세서 출력
# # 모르겠어서 코드 가져와서 봄
# n,m = map(int, input().split())
# original = []
# count = []
#
# for _ in range(n):
#     original.append(input())
#
# for a in range(n-7):
#     for b in range(m-7):
#         index1 = 0
#         index2 = 0
#         for i in range(a, a+8):
#             for j in range(b, b+8):
#                 if (i+j) % 2 == 0:
#                     if original[i][j] != 'W':
#                         index1 += 1
#                     if original[i][j] != 'B':
#                         index2 += 1
#                 else:
#                     if original[i][j] != 'B':
#                         index1 += 1
#                     if original[i][j] != 'W':
#                         index2 += 1
#         count.append(min(index1, index2))
#
# print(min(count))

# 1436
# 접근 방법 : 숫자를 쭉 증가시키다가 666이 나오면 카운트를 올려서 그때의 숫자를 출력
#
# import sys
#
# n = int(sys.stdin.readline())
# count = 0
# num = 655
# while True :
#     num += 1
#     if "666" in str(num) :
#         count += 1
#     if count == n :
#         break
#
# print(num)