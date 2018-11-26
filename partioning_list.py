#Getting user input for values in list
l=list(map(int,input().split(' ')))
def add_list(l):
    x=0
    for i in l:
        x+=i
    return x
for i in range(1,len(l)):
    #checking whether sum of sub lists are equal.
    if add_list(l[:i])==add_list(l[i:]):
        print("list can be partitioning with: ",(l[:i],l[i:]))
        break
        
"""
Worst case order of algorithm will be "O(n**2)".
1: Best case execution order O(n)
If first element will be sum of rest of elements in list.
Example:- 
l=[12,1,2,3,4,2]
Here order will be O(n).
Because inner loop add_list() will take O(n) order to add all elements of list.
But outer loop will execute only once.

2: Worst case execution order O(n**2)
If last element will be sum of all elements in list.
Example:-
l=[1,2,3,4,2,12]
Here order will be O(n**2)
Because inner loop add_list() will take O(n) order and outer loop also take O(n) order to execute.
So combined order will be O(n**2).
"""
