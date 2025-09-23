# demoLoop.py

#while루프
value = 5
while value > 0:
    print(value)
    value -=1

print("---for in 루프 ---")
for item in [1,2,3]:
    print(item)

d = {"apple":100, "banana":200}
for item in d.items():
    print(item)

print("---수열함수---")
print(list(range(1,11)))
print(list(range(2000,2026)))
print(list(range(1,32)))

print("---리스트 컴프리헨션---")
lst = [1,2,3,4,5,6,7,8,9,10]
print([i**2 for i in lst if i>5])
tp = ("apple", "banana")
print([len(i) for i in tp])
d = {100:"apple", 200:"kiwi"}
print([v.upper() for v in d.values()])
