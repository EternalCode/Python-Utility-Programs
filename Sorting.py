def merge_sort(one):
    '''
    Given an unsorted list, osrt it using merge sort
    '''
    #base case: Empty list or list with 1 element, return the list
    if len(one) <= 1:
        return one
    else:
        top = merge_sort(one[:len(one)/2])
        bot = merge_sort(one[len(one)/2:])
        #call the merge helper function to merge two sorted lists
        return merge(top, bot)
        

def merge(one, two):
    '''
    Given two ordered lists, merge them
    '''
    sorted_list = []
    fin_len = len(one) + len(two)
    #loop while the sorted list is not the size of the two lists combined
    while (len(sorted_list) != fin_len):
        #two cases to check first, if two is empty and one is not
        if (!len(one)):
            #if one was empty, then two is non-empty by the while condition
            return (sorted_list + one)
        elif (!len(two)):
            #if two was empty, then one is non-empty by the while condition
            (return sorted_list + two)
        else:
            #check first indicy of one and first indicy of two         
            if (one[0] <= two[0]):
                #if one's first indicy was smaller than or equal to two's
                #remove it and place it into the sorted list
                sorted_list.append(one[0])
                one = one[1:]
            else:
                #otherwise put two's first indicy into the sorted list
                sorted_list.append(two[0])
                two = two[1:]
    #return the sorted list the while loop as been satisfied
    return sorted_list


def selection_sort(one):
    '''
    given an unsorted list, sort it using selection sort algorithm.
    '''
    for j in range(0, len(l)):
        smallest = j
        for i in range(j, len(l)):
            if (l[i] < l[smallest]):
                smallest = i;
        l[j], l[smallest] = l[smallest], l[j]
    return l


def insertion_sort(one):
    '''
    Given a list, sort it using an insertion sort algorithm
    '''
    #loop through the list
    for index in range(0, len(one)):
        #take the element make sure it has a previous
        if (index > 0):
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
            
import heapq as heap
def heap_sort(list):
    '''
    Given a list, use a heap sort algorithm to sort it
    '''
    my_heap = list
    heap.heapify(my_heap)
    return [heap.heappop(my_heap) for i in range(len(my_heap))]


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
        return (quick_sort(less) + pivot + quick_sort(greater))
    
