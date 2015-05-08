"""
A Multiset(ADT) class that works from a SkipList.
Also contains exceptions.

Author: Dilshan Gunasekera & Tianhe Hou
UtorID: gunasek4 & houtainh
Student #: 999891149 & 998241399
"""

import splaytree


class IncompatibleTypeException(Exception):
    '''
    An Exception raised when attempting to insert into a skip list object
    a data type that is already not in the skip list
    '''

    def __str__(self):
        '''
        Returns a string to safegaurd abstraction
        '''
        return ("That Multiset already contains a different data type," +
                " you can only insert like data types")



class RemoveFromEmptySet(Exception):
    '''
    If you try removing from empty skiplist, skiplist.py does nothing. But to
    inform the user, this exception exists
    '''

    def __str__(self):
        '''
        Returns a string to tell the user they are doing something illogical
        '''
        return ("Cannot remove item from empty Multiset")



class ComparisonFailure(Exception):
    '''
    An exception raised when attempting to compare Multiset with something that
    is not a multiset
    '''

    def __str__(self):
        '''
        Returns a string to safeguard abstraction
        '''
        return ("Can't compare a Multiset to something that is not a Multiset")




class Multiset(splaytree.SplayTree):
    
    
    
    def __init__(self):
        '''
        (Multiset obj) --> NoneType
        
        initiation method of a multiset object
        '''
        splaytree.SplayTree.__init__(self)
        
    
    
    def __contains__(self, element):
        '''
        (Multiset obj, object) --> bool
        
        Given an arbitrary value, return True if and only if the element is 
        contained in the multiset.
        '''
        return splaytree.SplayTree.search(self, element)

    
    def count(self, element):
        '''
        (Multiset obj, value) --> int
        
        Given a multiset, and an arbitrary value (element), return the number
        of occurences of the element in the multiset
        '''
        return splaytree.SplayTree.count(self, element)
            
            
    def insert(self, element):
        '''
        (Multiset obj, value) --> NoneType
        
        Given a value, element, appends it into the multiset. Returns nothing.
        '''
        splaytree.SplayTree.insert(self, element)

        
    def remove(self, element):
        '''
        (Multiset obj, value) --> NoneType
        
        Given an element, remove one occurance of it from the list.
        Returns None.
        '''
        if len(self) == 0:
            raise RemoveFromEmptySet(": Cannot remove from empty Multiset")
        splaytree.SplayTree.delete(self,element)
    
    def clear(self):
        '''
        (Multiset obj) --> NoneType
        
        Given a multiset object, remove all it's elements. Return None.
        '''
        splaytree.SplayTree.__init__(self)
        
        
    def __len__(self):
        '''
        (Multiset obj) --> int
        
        Given a multiset object, return the number of elements it contains
        '''
        return len(splaytree.SplayTree.transverse(self))
    
    def __repr__(self):
        '''
        (Multiset obj) --> str
        
        Given a multiset object, return a string representation of it.
        '''
        return ("MultiSet" + str(splaytree.SplayTree.transverse(self))) 
    
    def __str__(self):
        '''
        (Multiset obj) --> str
        
        Return a string representation of the multiset.
        '''
        return self.__repr__()
    
    def __eq__(self, other):
        '''
        (Multiset obj, Multiset obj) --> bool
        
        Given another multiset (other), determine if it's equal to the current
        multiset in question. Return True if and only if it is.
        '''
        #raise exception if bad input
        if (type(self) != type(other)):
            raise ComparisonFailure(": Cannot compare unlike data types")
        return (splaytree.SplayTree.transverse(self) == splaytree.SplayTree.transverse(other))
    
    def __le__(self, other):
        '''
        (Multiset obj, Multiset obj) --> bool
    
        Given two multisets (self and other), determine if self is less than or
        equal to other. Return True iff self is a subset of other
        '''
        #raise exception if bad input
        if (type(self) != type(other)):
            raise ComparisonFailure(": Cannot compare unlike data types")        
        #check if self and other have the same amount of elements and they are the same
        if (self == other):
            return True
        #check if self is a subset of other (self is non-empty)
        elif (self._subset(other)):
            return True
        #self is greater than other
        else:
            return False

        
    def _subset(self, other):
        '''
        (Multiset obj, Multiset obj) --> bool
        
        Given two Multisets, return true iff the first multiset(self) is a 
        subset of the second(other)
        '''
        #transverse returns ordered list of both sets
        first = splaytree.SplayTree.transverse(self)
        second = splaytree.SplayTree.transverse(other)
        third = Multiset()
        for element in second:
            third.insert(element)
        #if the first set is bigger, not a subset
        if len(first) > len(second):
            return False
        for element in first:
            #check if every element in first is in second
            if (element in third):
                third.remove(element)
            #if second doesn't contain an element in first, not a subset
            else:
                return False
        return True
            

    def __sub__(self, other):
        '''
        (Multiset obj, Multiset obj) --> object
        
        Given two multisets, self and other, return a multiset which is the 
        difference of the two.
        '''
        #raise exception if bad input
        if (type(self) != type(other)):
            raise ComparisonFailure(": Cannot compare unlike data types")
        #get list version of both sets
        first = splaytree.SplayTree.transverse(self)
        second = splaytree.SplayTree.transverse(other)
        #populate third set to have all of first set
        third = Multiset()
        for element in first:
            third.insert(element)        
        #loop through the list version of the second
        for element in second:
            if element in third:
                #remove any occurances of second in first
                third.remove(element)
        #return the multiset
        return third
            
        
                
    def __isub__(self, other):
        '''
        (Multiset obj, Multiset obj) --> object
        
        Takes in two multiset objects (self, other), and updates the self to be
        the difference between itself and other. There is no return value
        '''
        #raise exception if bad input
        if (type(self) != type(other)):
            raise ComparisonFailure(": Cannot compare unlike data types") 
        #make self be equal to the substraction operation
        self = self - other
        return self
        
    def __add__(self, other):
        '''
        (Multiset obj, Multiset obj) --> Object
            
        Takes in two multiset objects, self and other, and returns a third multiset
        which contains the union of self and other.
        '''
        #raise exception if bad input
        if (type(self) != type(other)):
            raise ComparisonFailure(": Cannot compare unlike data types") 
        #get list versions of each tree
        first = splaytree.SplayTree.transverse(self)
        second = splaytree.SplayTree.transverse(other)
        #add them together
        final = first + second
        #set up a new multiset to return
        ret_val = Multiset()
        #for every element in the final list, insert them into the new multiset
        for element in final:
            ret_val.insert(element)
        #return the new set
        return ret_val

    def __iadd__(self, other):
        '''
        (Multiset obj, Multiset obj) --> Multiset obj
        
        Takes in two multiset objects as paramaters (self and other), and updates 
        the multiset self, to be the union of the two sets. Returns NoneType.
        '''
        #raise exception if bad input
        if (type(self) != type(other)):
            raise ComparisonFailure(": Cannot compare unlike data types")         
        self = self + other
        return self

    def __and__(self, other):
        '''
        (Multiset obj, Multiset obj) --> Multiset obj
        
        Takes multiset in two objects as paramaters (self and other), and returns
        a third multiset which contains the intersection of both self and other.
        '''
        #raise exception if bad input
        if (type(self) != type(other)):
            raise ComparisonFailure(": Cannot compare unlike data types") 
        #get list versions
        first = splaytree.SplayTree.transverse(self)
        second = splaytree.SplayTree.transverse(other)
        #make third set and populate it with second's elements
        third = Multiset()
        for element in second:
            third.insert(element)
        #make an empty multiset to be returned
        final = Multiset()
        for element in first:
            #put shared elements in the multiset
            if element in third:
                final.insert(element)
                #remove from the third list
                third.remove(element)
        return final

    
    def __iand__(self, other):
        '''
        (Multiset obj, Multiset obj) --> Multiset obj
        
        Takes two multiset objects as paramaters, (self and other), and updates 
        self to be equal to the intersection of itself and other. No return value
        '''
        #raise exception if bad input
        if (type(self) != type(other)):
            raise ComparisonFailure(": Cannot compare unlike data types")         
        self = self.__and__(other)
        return self
        
    def isdisjoint(self, other):
        '''
        (Multiset obj, Multiset obj) --> Bool
        
        Takes two multiset objects (self and other) as paramaters, and returns True
        if and only if there are no shared values between its two paramaters.
        '''
        #raise exception if bad input
        if (type(self) != type(other)):
            raise ComparisonFailure(": Cannot compare unlike data types")
        #make empty set for comparisons
        temp = Multiset()
        #special case where both sets are empty
        if ((self.__eq__(temp)) and (other.__eq__(temp))):
            return True
        #make a checking variable be the interseciton between the sets
        check = self.__and__(other)
        #return true iff the intersection is empty
        if check.__eq__(temp):
            return True
        else:
            return False

            
            
                
            
    
