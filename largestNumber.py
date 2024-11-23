# Write a Python program to find the largest number in a list.
a= [66,4,34,24,1,125,65,39]

if a[0] < a[1] :
    largeNum = a[1]
else:
    largeNum = a[0]

count= 2
while count< len(a)-1:
    count+=1
    if a[count] < largeNum :
        largeNum = largeNum
    else:
        largeNum = a[count]

print(largeNum)
    
    
    
        
