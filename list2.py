list=[]

n=int(input("Enter the length of list :"))

for i in range(0,n):
    element=input("Enter element "+ str(i+1) + ": ")
    list.append(element)
    print("Element appended")

print(list)

index={}
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]==list[j]:
            index[list[i]]=[i,j]

for key,value in index.items():
    print(f"the elements of list that are {key} are at {value}")




