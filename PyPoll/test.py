data = [1,2,3,4,5,6,7]
votes = 0
arr = []
for item in data:
    votes = item + 1
    arr.append({'votes': votes})

print(f"My data: {data}")
print(f"My appended results: {arr}")
