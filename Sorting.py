def merge_sort(one):
    '''
    Given an unsorted list, osrt it using merge sort
    '''
    #base case: Empty list or list with 1 element, return the list
    if len(one) == 0:
        return one
    elif len(one) == 1:
        return one
    else:
        #split the list into two smaller lists
        half = len(one)//2
        #recusively call merge sort on each halves for the bigger list
        p1 = merge_sort(one[:half])
        p2 = merge_sort(one[half:])
        #call the merge helper function to merge two sorted lists
        return merge(p1, p2)
        

def merge(one, two):
    '''
    Given two ordered lists, merge them
    '''
    sorted_list = []
    fin_len = len(one) + len(two)
    #loop while the sorted list is not the size of the two lists combined
    while (len(sorted_list) != fin_len):
        #two cases to check first, if two is empty and one is not
        if (len(one) == 0):
            #if one was empty, then two is non-empty by the while condition
            for element in two:
                sorted_list.append(element)
            #break loop early, since we are done
            return sorted_list
        #if one is empty and two is not
        elif (len(two) == 0):
            #if two was empty, then one is non-empty by the while condition
            for element in one:
                sorted_list.append(element)
            #break loop early, since we are done
            return sorted_list            
        else:
            #check first indicy of one and first indicy of two         
            if one[0] <= two[0]:
                #if one's first indicy was smaller than or equal to two's
                #remove it and place it into the sorted list
                sorted_list.append(one[0])
                one.remove(one[0])
            else:
                #otherwise put two's first indicy into the sorted list
                sorted_list.append(two[0])
                two.remove(two[0])
    #return the sorted list the while loop as been satisfied
    return sorted_list


def selection_sort(one):
    '''
    given an unsorted list, sort it using selection sort algorithm.
    '''
    #loop through the list and append the smallest element into another list
    sorted_list = []
    while (len(one) != 0):
        #assume the smallest element is the first element
        current_smallest = one[0]
        #loop through the list
        for element in one:
            #adjust current smallest by comparing with every element in the list
            if element <= current_smallest:
                current_smallest = element
        #once the smallest element is verified put it into the sorted list and
        #remove it from the unsorted list
        one.remove(current_smallest)
        sorted_list.append(current_smallest)
    #return the sorted list
    return sorted_list


def insertion_sort(one):
    '''
    Given a list, sort it using an insertion sort algorithm
    '''
    #loop through the list
    for index in range(0, len(one)):
        #take the element make sure it has a previous
        if index == 0:
            #do nothing
            x = "filler"
        else:
            cl = index -1
            while (one[index] < one[cl]):
                #check the next element down the line if there is one
                if (cl != 0 and (one[cl-1] > one[index])):
                    cl -= 1
                else:
                    #swap cl and one
                    p1 = one[:cl]
                    p1.append(one[index])
                    p1 += one[:index] + one[index +1:]
                    two = p1
                    one[cl], one[index] = one[index], one[cl]
            #if it's not less, then do nothing
    return two
            
            
def heap_sort(list):
    '''
    Given a list, use a heap sort algorithm to sort it
    '''
    my_heap = Heap()
    ret = []
    #insert all elements in the list into the heap
    for element in list:
        my_heap.insert(element)
    #pop all elements from the heap out
    while not(my_heap.is_empty()):
        ret.append(my_heap.remove_top())
    return ret


def quick_sort(one):
    '''
    Given a list, use a quick sort algorithm to sort it
    '''
    if len(one) <= 1:
        return one
    else:
        #take the first element in the list and use it as the fat pivot
        pivot = []
        pivot.append(one[0])
        less = []
        greater = []
        for index in range(1, len(one)):
            if one[index] == pivot[0]:
                pivot.append(one[index])
            elif one[index] < pivot[0]:
                less.append(one[index])
            else:
                greater.append(one[index])
        sec1 = quick_sort(less)
        sec2 = quick_sort(greater)
        return (sec1 + pivot + sec2)