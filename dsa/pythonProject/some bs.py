# n = int(input())
# grid = [["0"] * n for _ in range(n)]
#
# for i in range(n):
#     row = input().strip()
#     j = 0
#     for ch in row:
#         grid[i][j] = ch
#         j += 1
#
# word = input().strip()
# m = len(word)
#
# if m == 0:
#     print(0)
#     exit()
#
# res = 0
#
# if m == 1:
#     # Handle single-character case
#     count = 0
#     for r in range(n):
#         for c in range(n):
#             if grid[r][c] == word[0]:
#                 count += 1
#     # Check palindrome and double if needed
#     if word == word[::-1]:
#         count *= 2
#     print(count)
#     exit()
#
# # Define direction functions
# def goleft(r, c, i):
#     if i == m:
#         return 1
#     if c - 1 >= 0 and grid[r][c - 1] == word[i]:
#         return goleft(r, c - 1, i + 1)
#     return 0
#
# def goright(r, c, i):
#     if i == m:
#         return 1
#     if c + 1 < n and grid[r][c + 1] == word[i]:
#         return goright(r, c + 1, i + 1)
#     return 0
#
# def godown(r, c, i):
#     if i == m:
#         return 1
#     if r + 1 < n and grid[r + 1][c] == word[i]:
#         return godown(r + 1, c, i + 1)
#     return 0
#
# def goup(r, c, i):
#     if i == m:
#         return 1
#     if r - 1 >= 0 and grid[r - 1][c] == word[i]:
#         return goup(r - 1, c, i + 1)
#     return 0
#
# def godiagonaldown(r, c, i):
#     if i == m:
#         return 1
#     if r + 1 < n and c + 1 < n and grid[r + 1][c + 1] == word[i]:
#         return godiagonaldown(r + 1, c + 1, i + 1)
#     return 0
#
# def godiagonalup(r, c, i):
#     if i == m:
#         return 1
#     if r - 1 >= 0 and c + 1 < n and grid[r - 1][c + 1] == word[i]:
#         return godiagonalup(r - 1, c + 1, i + 1)
#     return 0
#
# def godiagonalleft(r, c, i):
#     if i == m:
#         return 1
#     if r - 1 >= 0 and c - 1 >= 0 and grid[r - 1][c - 1] == word[i]:
#         return godiagonalleft(r - 1, c - 1, i + 1)
#     return 0
#
# def godiagonalright(r, c, i):
#     if i == m:
#         return 1
#     if r + 1 < n and c - 1 >= 0 and grid[r + 1][c - 1] == word[i]:
#         return godiagonalright(r + 1, c - 1, i + 1)
#     return 0
#
# # Check each cell for the starting character and explore all directions
# for r in range(n):
#     for c in range(n):
#         if grid[r][c] == word[0]:
#             res += goleft(r, c, 1)
#             res += goright(r, c, 1)
#             res += godown(r, c, 1)
#             res += goup(r, c, 1)
#             res += godiagonaldown(r, c, 1)
#             res += godiagonalup(r, c, 1)
#             res += godiagonalleft(r, c, 1)
#             res += godiagonalright(r, c, 1)
#
# # Check if the word is a palindrome and double the count
# if word == word[::-1]:
#     res *= 2
#
# print(res)