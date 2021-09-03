#reverse with worst case time complexity o(n) space complexity o(n)
#return reverse list 
a = [1,2,3,4]
result = []
start = len(a) -1
end = 0
while start >= end:
    result.append(a[start])
    start -= 1
print(result)
    
    