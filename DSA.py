# firstly we learn about the arrays
# adding elements to an array
""""
n = [22, 44, 5,]
n.append(46)
n.insert(1, 77)

#removing elements from an array
n.remove(5)
n.pop()
# finding sum of arrays

n = [22, 44, 5, 46, 77]
total = 0
for i in n:
    total += i
    print("sum=", total)
#fiding largest num'
n = [22, 44, 5, 46, 77]
max_value = n[0]
for i in n:
    if i>max_value:
        max_value = i
print("largest =", max_value)

h = [22, 44, 5, 46, 999]
min_value = h[0]
for i in h:
    if i<min_value:
        min_value = i
print("smallest =", min_value)

n = [22, 44, 5, 46, 77]
n.sort()
print("sorted array =", n)

n = [22, 44, 5, 46, 77]
n.reverse()
print("reversed array:", n)

n = [22, 44, 5, 46, 77]

even = 0
odd = 0
for i in n:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("even count =", even)
print("odd count =", odd)

n = [22, 44, 5, 46, 77]

even_sum = 0
odd_sum = 0
for i in n:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("even sum =", even_sum)
print("odd sum =", odd_sum)

n = [22, 44, 5, 46, 77]
count = 0
for i in n:
    count += 1
print("number of elements =", count)

n = [22, 44, 5, 46, 77]
average = 0
total = 0
for i in n:
    total += i
average = total / len(n)
print("average =", average)

n = [22, 44, 5, 46, 77]
n.clear()
print("cleared array =", n)

n = [22, 44, 5, 46, 77]
n2 = n.copy()
print("copied array =", n2)

n = [22, 44, 5, 46, 77]
n3 = n.count(44)
print("count of 44 =", n3)

n = [22, 44, 5, 46, 77]
even_difference = []
odd_difference = []
for i in n:
    if i % 2 == 0:
        even_difference.append(i)
    else:
        odd_difference.append(i)
print("even difference =", even_difference)
print("odd difference =", odd_difference)

n = [22, 44, 5, 46, 77]
even_subtract = 0
odd_subtract = 0
for i in n:
    if i % 2 == 0:
        even_subtract -= i
    else:
        odd_subtract -= i
print("even subtract =", even_subtract)
print("odd subtract =", odd_subtract)

# squares
n = [22, 44, 5, 46, 77]
squares = []
for i in n:
    squares.append(i ** 2)
print("squares =", squares)


n = [22, 44, 5, 46, 77]
first = second = float('-inf')
for i in n:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i
print("second largest =", second)

n = [22, 44, 5, 46, 77]
first = second = third = float('-inf')
for i in n:
    if i > first:
        third = second
        second = first
        first = i
    elif i > second and i != first:
        third = second
        second = i
    elif i > third and i != second and i != first:
        third = i
print("third largest =", third)


arr = [1, 2, 4, 5, 6,]
n = 5
expeceted_sum = n * (n + 1) // 2
actual_sum = sum(arr)
missing_number = expeceted_sum - actual_sum
print("missing number is:", missing_number)


# check an array is sorted or not
arr = [1, 2, 4, 5, 6,]
sorted_flag = True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        sorted_flag = False
        break
if sorted_flag:
    print("array is sorted")
else:
    print("array is NOT sorted")
    

    #zeros all to end
arr = [0, 1, 0, 3, 12]
non_zero_index = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[non_zero_index] = arr[i]
        non_zero_index += 1
for i in range(non_zero_index, len(arr)):
    arr[i] = 0
print("array after moving zeros to end:", arr)
#easy way is
arr = [0, 1, 0, 3, 12]
result = []
for i in arr:
    if i != 0:
        result.append(i)
zeros = [0] * (len(arr) - len(result))
final = result + zeros

print("after moving zeros:", final )

n = final
print(n)

B = n[::-1]
print("reversed array:", B)


st="coding is fun coder"
count = {}
for i in range(len(st)):
    if (st[i] in count):
        count[st[i]] += 1
    else:
        count[st[i]] = 1
print(count)
"""
class solution:
    def findsum(self,A,N):
        if N == 1:
             return A[0]
    if A[0]>A[1]:
        maximum = A[0]
        minimum = A[1]
    else:
        maximum = A[1]
        minimum = A[0]
    for i in range(2,N):
        if A[i]>maximum:
            maximum = A[i]
        elif A[i]<minimum:
                minimum = A[i]
    return maximum + minimum
