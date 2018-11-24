#Getting user input for values in list
l=list(map(int,input().split(' ')))
for i in range(1,len(l)):
    #checking whether sum of sub lists are equal.
    if sum(l[:i])==sum(l[i:]):
        print("list can be partitioning with: ",(l[:i],l[i:]))
