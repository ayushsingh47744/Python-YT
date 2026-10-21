# if we dont write in curly braces then it will be considered as dictionary and if we write in curly braces then it will be considered as set
# in dictionary we have key and value pair and in set we have only values

# a = {1:"hello", 2:"world", 3:"python"}

# mutabble, key must be unique,value can be duplicate, keys are treated as a index, hetrogeneous

# d = {10:100,20:200,30:300,40:400}
# d[10] = 100 #updating
# d[50] = 500 # creating
# del d[30] # deleting 
# for i in d:
#     print(i, d[i])
# for i in d.keys():
#     print(i)  
# for i in d.values():
#     print(i)


# Methods in dictionary
# d = {10:100,20:200,30:300,40:400}

# shallow copy means a ke andr jo changes kroge vo b ke andr reflect nhi honge
# a = [10,20,30,40]
# b=a.copy()
# b[0] = 100
# print(a)

# deep copy means a ke andr jo changes kroge vo b ke andr reflect honge
# a = [10,20,30,40]
# b=a
# b[0] = 100
# print(a)



# Practice questions on dictionary
# Q1
d1 ={1:10, 2:20, 3:30, 4:40, 5:50}
d2 ={6:60, 7:70, 8:80, 9:90, 10:100}

for i in d2:
    d1[i]=d2[i]

print(d1)

# Q2
d = {1:10, 2:20, 3:30, 4:40, 5:50}
sum=0
for i in d:
    sum += d[i]
print(sum)

# Q3
a = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]
d={}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)

# Q4
d1 ={1:10, 2:20, 3:30, 4:40, 5:50}
d2 ={5:60, 7:70, 8:80, 9:90, 10:100}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)