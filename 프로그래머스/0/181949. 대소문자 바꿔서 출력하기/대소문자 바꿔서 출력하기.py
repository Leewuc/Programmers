str = input()
ans = ""
for i in str:
    if i.isupper() == True:
        ans += i.lower()
    else:
        ans += i.upper()
print(ans)