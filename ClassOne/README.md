# Leet Code
## Class One

### Array
Array is a data structure that contains a group of elements. Typically these elements are all of the same data type, such as an integer or string.
In python, A list is a data structure in Python that is a mutable, or changeable, **ordered sequence of elements**.
What is **ordered sequence**?
In Python, sequence is the generic term for an ordered set. There are several types of sequences in Python, the following three are the most important.
- Lists are the most versatile sequence type
- Tuples are like lists, but they are immutable
- Strings are a special type of sequence that can only store characters

###  Define a List
```sh
 empty_list = []
 with_value_list = [1,2,3,4]
```
### Append value in List:
```sh
empty_list.append(3)
empty_list.append(4)
empty_list.append(5)
empty_list.append(6)
empty_list.append(7)
empty_list.append(8)
```
### Pop value from List:
```sh
empty_list.pop()
empty_list.pop()
empty_list.pop()
```
### Pop value from List:
```sh
print(empty_list)
print(with_value_list)
```
### Length of a List: 
```sh
Print(len(with_value_list))
```
**Time complexity** is the amount of time taken by an algorithm to run, as a function of the length of the input. It measures the time taken to execute each statement of code in an algorithm.
Space and Time define any physical object in the Universe. Similarly, Space and Time complexity can define the effectiveness of an algorithm
**Time complexity** is given by time as a function of length of input. And, there exists a relation between the input data size (n) and number of operations performed (N) with respect to time.
Let's start with a simple example. Suppose you are given an array A and an integer x and you have to find if exists in array.
Simple solution to this problem is traverse the whole array and check if the any element is equal to x.
```sh
data = [1,4,5,3,5,2,6,7,9,10]
target = 10
for element in A:
	if element == target:
		print("Found", target)
```
![Alt text](relative/path/to/img.jpg?raw=true "for loop")
```sh
a = [1,8,13,5,4]
find = 5
start = 0
end = len(a)
while start < end:
    if a[start] == find:
        print("Found")
    start +=1
```
![Alt text](relative/path/to/img.jpg?raw=true "whileloop")

Each of the operation in computer take approximately constant time. Let each operation takes c time. The number of lines of code executed is actually depends on the value of x. During analyses of algorithm, mostly we will consider worst case scenario ,when x is not present in the array . In the worst case, the if condition will run N times where is the length of the array A. So in the worst case, total execution time will be **O[n]** where O is the **order of growth** and n is the length of input. It is also called as **Big O Notation**.

As we can see that the total time depends on the length of the array A . If the length of the array will increase the time of execution will also increase.

**Order of growth** is how the time of execution depends on the **length of the input**. In the above example, we can clearly see that the time of execution is linearly depends on the length of the array. **Order of growth** will help us to compute the running time with ease. We will ignore the lower order terms, since the lower order terms are relatively insignificant for large input. 

Thus , the time complexity of an algorithm is denoted by the combination of all O[n] assigned for each line of function
There are different types of time complexities used, let’s see one by one:

- **Constant time – O (1)**
- **Linear time – O (n)**
- **Logarithmic time – O (log n)**
- **Quadratic time – O (n^2)**
- **Cubic time – O (n^3)**

![Alt text](relative/path/to/img.jpg?raw=true "time complexity")
![Alt text](relative/path/to/img.jpg?raw=true "time complexity")
## Some Array Problem
- Reverse Array
```sh
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
```







