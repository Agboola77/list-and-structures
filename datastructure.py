

mylist = [1,2,3,4,'a','b']

dupl_list = mylist.copy()
print(mylist[0])
print(mylist[-2])
print(mylist[0:-2])

print(dupl_list)

mylist.remove('a')

print(dupl_list)

for i in range(len(mylist)):
    print(mylist[i])

#Adding to the end
mylist.append('d')    

print(mylist)

#insert to any position using index and what to insertt\
mylist.insert(3,'Alex')
print(mylist)

#removing just the item at back
mylist.pop()
print(mylist)

#removing any given value
mylist.remove(1)
print(mylist)

#reversing the list
mylist_2 = [1,2,3,4,1,3,0,7]
mylist_2.sort(reverse=True)

print(mylist_2)


num_val = int(input('How many values do you want to store?'))

score = []

for i in range(num_val):
    print('score ', (i+1))
    score.append(input('Enter score: '))

for i in range(len(score)):
    print(score[i])

mytuple = (1,2,3,4)
print(mytuple)
