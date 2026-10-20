a = [12,13,14,15,16,34.5]


# #1st way using index

# for i in range(len(a)):
#     print(a[i])

# #2nd way directly on values

# for i in a:
#     print(i)

# l = [-45,67,12,-68,-69,34]

# print("positive elements are ")
# for i in l:
#     if i >= 0:
#         print(i)
# print("negitive elements are")

# for i in l:
#     if i < 0:
#         print(i)

# l = [12,435,67,89,23,25,69]

# sum = 0

# for i in l:
#     sum = sum + i

# print(sum/len(l))





# l = [12,567,43,235,347,568,45,7]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")


# l = [12,16,13,19,17]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i


# print(sec_largest, largest)



# a = [12,13,18,15,16]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")

