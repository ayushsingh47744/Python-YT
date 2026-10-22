p = open('06_Exception_handling.py','r')  #read mode is default mode
print(p.read())

# for creating use w mode
p = open("superman.txt","w")

#agar us file me kuch likhna he to
p.write("hello i am superman")
p.close()

# append overwrite nhi append krta he
p = open("superman.txt","a")
p.write("\nhello i am superman and i am here to save the world")
