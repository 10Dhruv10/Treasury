i = 1
count = 0
l = 6
while l != 0:
    l = l >> i
    i += 1
    count += 1

res = 1
for i in range(1, count + 1):
    res = res << i

print(res)