def smallest_num_in_list( list ):
    
    min = list[ 0 ]
    for a in list:
        
        if a < min:
            min = a
            list.insert(0, min)
            
    print(list)


print("\nThe smallest element has swaped to the front , but i could not remove previous position ;) ")
smallest_num_in_list([1, 2, -8, 0])
