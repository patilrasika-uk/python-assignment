#--------------loops value---------------------------
m =int(input("enter any number:"))

isprime = True

if m<=1:
    isprime = False
else :
    for x in range (2,m):
        if m%x==0:
            isprime = False
        break
if isprime== True:
    print ("prime number")
else:
    print ("not prime number")


print ("pattern")

rows =int(input("enter any number:"))
for x in range (rows+1):
    for z in range (x):
        print ("* ",end="")
    print ()


rows1 =int(input("enter any number:"))
for y in range (rows1 ,0,-1):
    for k in range (y):
        print ("* ",end="")
    print ()
marks1 = [78,45,90,34,88,76,35]
pas = 0
fail = 0
highest = 0
for x in marks1:
     if x >= 40:
         pas+=x
     else:
         fail+=x
     if x>highest:
         highest =x
print (pas)
print (fail)
print (highest)
total = 0
for x in marks1:
    total +=x
average=total/len(marks1)    
print (total)
print (average)

#------------------------exam question------------------    
    
#----------------1sum of elements---------------

mum = [54,65,3,2,95,65,3,46,4,6,2,6]
total = 0
for x in mum:
    total +=x
print (total)


#--------------2find the maximum element-------------
list = [256,665,85,98,364,523,26,456]
max = 0
for x in list:
    if x>max:
        max = x
print (max)

#-----------3extract even numbers-----

list1 = [2,3,4,5,6,7,8,9]
even = []
for x in list1:
    if x%2 ==0:
        even.append (x)
print (even)

#----------4odd numbers-----------------
list2 = [2,3,4,5,6,7,8,9]
odd = []
for x in list2:
    if x%2 !=0:
        odd.append (x)
print (odd)
''
#----------5revers-------
list2 = [1,2,3,4,5]
revers = []
for x in range (len(list2)-1, -1, -1):
    revers.append (x)
print (revers)


#------7-find duplicate elements----------
my_list = [1,2,5,5,4,8,2,4,5,2]
find_dup = []
for x in range (len(my_list)):
    for y in range (x+1,len(my_list)):
        if my_list[x] == my_list[y] and my_list[x] not in find_dup:
            find_dup.append (my_list[x])
            break
print ("find duplicate: ",find_dup)


#--------8--remove duplicate---------
ras = [1,2,3,4,5,3,6,1,8,9]
remove =[]
for x in ras:
    if x not in remove:
        remove.append (x)
print ("remove duplicate",remove)
    
#------15-remove zero--------
num = [1,0,3,5,0,6,9,0,5]
zero = []
for x in num:
    if x !=0:
        zero.append (x)
print (zero)

#------17-students marks---------

marks = [78,45,90,34,88,76,35]

pas = 0
fail = 0
highest = 0

for x in marks:
    if x >= 40:
        pas+=1
    else:
        fail += 1
        
    if x>highest:
        highest = x
    

total=sum (marks)
average=total/len(marks)
print (total)
print (average)
print (highest)
print (fail)
print (pas)





#-------18-shopping card-----------
prices = [156,329,391,200,354,545,20]
total = 0
for x in prices:
    total +=x
print (total)

max = 0
for x in prices:
    if x>max:
        max =x
print ("expensive",max)

min = 800
for x in prices:
    if x <min:
        min =x
print ("cheapest",min)

count = []
for x in prices:
    if x>200:
        count.append (x)
print (len(count))

#------7-find duplicate elements----------
my_list = [1,2,5,5,4,8,2,4,5,2]
find_dup = []
for x in range (len(my_list)):
    for y in range (x+1,len(my_list)):
        if my_list[x] == my_list[y] and my_list[x] not in find_dup:
            find_dup.append (my_list[x])
            break
print ("find duplicate: ",find_dup)
#--------8--remove duplicate---------
ras = [1,2,3,4,5,3,6,1,8,9]
remove =[]
for x in ras:
    if x not in remove:
        remove.append (x)
print ("remove duplicate",remove)

#-------count frequency --------------



#---------check if list is palidrome---------





#




































     



   
