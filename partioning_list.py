#Getting user input for values in list
l=list(map(int,input().split(' ')))
#creating an empty list to hold partioned sub-lists
new_list=[]
for i in range(1,len(l)):
    #checking whether sum of sub lists are equal.
    if sum(l[:i])==sum(l[i:]):
        #adding a tuple of lists to empty list if list can be partioned
        new_list.append((l[:i],l[i:]))
        print("list can be partitioning with: ",new_list)
