list1=[10,20,30]#first method but some different concept
list2=list1
list2.append(40)
print(list1)
print(list2)
#second method but different concept from first method
list3=[10,20,30]
list4=list3.copy()
list4.append(40)
print(list3)
print(list4)
#method third slicing
list5=[1,2,3]
list6=list5[:]
list6.append(4)
print(list5)
print(list6)