list = []

listMax = int(input("Enter the total number of entities. : "))
print("\n")
for element in range(listMax):
    element= input("\nEnter the entity from your list: ")
    
    flag = 0
    
    for each in list:
        if element == each:
            flag =1
    
    if(flag == 0):
        list.append(element)
        print("Your entity has been updated to the list. Proceed.. ")
    
    else:
        print('Your entity is duplicate. Proceed with next entity.')
        
sort = input('Do you want your list to be sorted? (y/n) : ')

if (sort == 'y' or 'Y'):
	list.sort()
	
print('List without duplicates..: \n')
print(list)
print('\n\nLength:',len(list),"\n")

