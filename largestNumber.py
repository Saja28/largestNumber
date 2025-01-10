# Write a Python program to find the largest number in a list.
a= [66,4,34,24,1,125,65,39]
if a[0] < a[1] :
    large_Num = a[1]
else:
    large_Num = a[0]
count= 2
while count< len(a)-1:
    count+=1
    if a[count] < large_Num :
        largeNum = large_Num
    else:
        large_Num = a[count]
print(large_Num)
    
    
    
        
