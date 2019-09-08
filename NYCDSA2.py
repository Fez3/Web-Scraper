def binarysearch(min, max):
    #version 2
    if min==max:
        print("The number is "+str(min))
        return exit()
    
    print('The number is in the range ('+str(min)+','+str(max)+').')
    mid=int(min+(max-min)/2)

    answer=input("Is the number greater than "+str(mid)+"? Please typ 'y' or 'n'.")
    if answer=='y':
        return binarysearch(mid+1, max)
    elif answer=='n':
        return binarysearch(min, mid)
    else:
        print('error')
        return exit()

validinput=False
while not validinput:
    try:
        min=int(input("Please give a lower bound."))
        try:
            max=int(input("Please give an upper bound."))
            validinput=True
        except:
            print("Invalid upper bound")
    except:
        print("Invalid lower bound")
    


binarysearch(min, max)
exit()




def binarysearch(min, max):

    if min==max:
        print("The number is "+str(min))
        return

    mid=int((max-min)/2)

    print("Is the number greater than "+str(mid)+"?\n Please typ 'y' or 'n'.")
    answer=input()
    if answer=='y':
        return binarysearch(mid, max)
    elif answer=='n':
        return binarysearch(min, mid)

