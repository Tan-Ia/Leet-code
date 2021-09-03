# search a value in list
A = [1,4,5,3,5,2,6,7,9,10]

for element in A:
    print(element)
 

target = 10

for element in A:
    if element == target:
        print("Found", target)
a = [1,8,13,5,4]
find = 5
start = 0
end = len(a)
while start < end:
    if a[start] == find:
        print("Found")
    start +=1
