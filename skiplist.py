import random

class BodyNode(object):
    '''
    A class which contains methods for a Body Node Object.
    '''
    
    def __init__(self, data, next_link, bot_link):
        '''
        (Object) --> NoneType
        
        Initiation method for a body node. Contains a value (data), a next_link 
        which is just a link to the next node horizontally and a link to the node
        directly below it containing the same value. No return value.
        '''
        self.data = data
        self.next_link = next_link
        self.bot_link = bot_link
    
    
    def compare_nextval(self, value):
        '''
        (object, object) --> Bool
        
        A function that checks if the next horizontal value to the node contains
        a greater than any specified value. Returns True if and only if the value
        given is greater than the value of the next node.
        '''
        return ((self.next_link.data) < value)
    


class HeadNode(BodyNode):
    '''
    A class which contains methods for a Head Node Object.
    '''
    
    def __init__(self, next_link, bot_link):
        '''
        (object, object, object) --> NoneType
        
        Initiation method for a head node. Takes in a  next_link which is a 
        pointer to the next object horizontally in the linked list. The function
        also takes in a bot_link which is a pointer to the next HeadNode below
        itself. Returns None.
        '''
        BodyNode.__init__(self, None, next_link, bot_link)
    
    
    def is_last(self):
        '''
        (object) --> Bool
        
        Checks if there is a node below the current node. Returns True if and 
        only if there is a node below.
        '''
        
        return (not(self.bot_link == None))
        
        
        
class TailNode(HeadNode):
    '''
    A class which contains methods for a Tail Node object.
    '''

    def __init__(self, bot_link):
        '''
        (object, object) --> NoneType
        
        Initiation method for a Tail Node. Given a bot_link which is a pointer
        supposed to point to an object below it, creates a new Node with only
        a single downwards pointer
        '''
        HeadNode.__init__(self, None, bot_link)
    
    
    
class SkipList():
    '''
    SkipList class created in a manner to mimic functionality and properties of
    the SkipList algorithm by Prof. William Pugh in 1989.
    '''


    def __init__(self):
        '''
        (Object) --> NoneType
        
        Initiation method for a skip list object. Takes in no paramaters except self
        and returns None.
        '''
        self.start = None
        self.end = None
    
    def levels(self):
        '''
        (None) -- Int
        
        A function that is used to output how many numbers in a row, an RNG outputs
        a number less than 0.5 in the interval [0, 0.5]. Returns the number of
        times in a row this happens.
        
        REQ: Import random
        '''
        #make two variables, one to be a counter and one to represent
        #the number outputted by the rng
        current = 0
        counter = 1
        #as long as the generated num < 0.5 loop
        while (current <0.5):
            current = random.random()
            #increment the counter
            counter += 1
        #return the counter (number of levels, min 1 level)
        return counter
            

    def inserter(self, data):
        '''
        (Object, Object) --> NoneType
        
        Inserts a value into the skip list. Takes in a paramater data which is any
        form of data (object, int, str, ..ect) and inserts it into the Skip list
        '''
        ###FUNCTION INCOMPLETE
        ###
        ###Details:
        ###
        ###Function cannot insert into an empty skiplist
        ###
        ###Function cannot insert into level > max level
        ###I.e total levels in skip list is 3. Random says
        ###element '3' goes in level 5, cannot insert.
        ###
        ###Function working for skiplist which already contains levels
        ###and adding element in within the list. Ex:
        ###
        ###
        ###  SKIP LIST:
        ###  0 1-------7 0
        ###  0 1-----6-7 0
        ###  0 1-2---6-7 0
        ###  0 1-2-3-6-7 0
        ###
        ###'0's represent tail and head nodes. Can insert 1 to highest number 
        ###allowed by hardware/software within level 1-4. I.E function can't
        ###create new levels
        #set a variable to point to the start of the list
        node = self.start
        #call the function levels to determine the amount of levels a value will
        #iterate for
        lvl = self.levels()
        #find the total levels in the skiplist currently
        counter = 1
        while node.bot_link != None:
            node = node.bot_link
            #counter is the total levels in the skip list
            counter += 1
        #if there are more existing levels than levels, we insert directly into
        #the current skip list
        if counter >= lvl:
            #reset node to point to start
            node = self.start
            #make loops loop through the skip list bottom up lvl amount of times
            for i in range(0, lvl):
                for x in range(1, counter):
                    node = node.bot_link
                counter -= 1
                #determine what the bot connection would be for the currently
                #being inserted node
                if node.bot_link == None:
                    bot_con = None
                else:
                    temp = _help_search(node, data)
                    bot_con = temp[1]
                #call a _helper function to insert the node into the row
                _help_ins(node, bot_con, data)
                #reset node to be start. For loop will now go 1 row higher than
                #the current row
                node = self.start
    
    
    def _help_ins(node, bot_con, data):
        '''
        (object, object) --> NoneType
        
        Given any non-tail node, inserts a node containing data into a spot 
        between a node less than/equal to data and greater than data. Where the
        node containing data has a bot_link equal to bot_con. Returns None.
        '''
        #check if the next node is a tail node or greater than current node
        if ((node.next_link.data) == None) or ((node.next_link.data) > data):
            #if it is insert a body node between node and next node
            temp = BodyNode(data, node.next_link, bot_con)
            node.next_link = temp
        else:
            #otherwise call the function again expect with the next node
            node = node.next_link
            return _help_ins(node, bot_con, data)

        
    
    def search(self, data):
        '''
        (object, object) --> (Bool, object)
        
        Paramters for search method of a skiplist include an object(self) as 
        well as a value (data). Returns a boolean which is True if and only if
        a BodyNode object contains data as it's value -- if it was true then a
        pointer to the node which it was found in is returned. (If it is false,
        then the closest node is returned).
        '''
        #check if the skip list is empty, if it is data can't be in it
        if (self.start == None):
            return (False, None)
        #create a new start node with all the same properties as the previous
        r_link = self.start.next_link
        b_link = self.start.bot_link
        node = HeadNode(r_link, b_link)
        #call a _helper function to find data for us
        return _help_search(node, data)
        
    def _help_search(node, data):
        '''
        (object, object) --> Bool
        
        A recursive function which is designed to search a skiplist for a certain
        data value at a node. Nodes are unchanged, and returns a bool if and only
        if there exists a node that contains the value determined by data.
        
        Note: Searching for NoneType will always result in False.
        '''
        #check if start nodes are none
        if (node == None):
            return (False, node)
        #base case, if the next node is data return true
        if ((((node.next_link.data) == data)) and (node.next_link.data != None)):
            node = node.next_link
            return (True, node)
        #if the next node is not a tail node and it's less than data
        if (((node.next_link.data) != None) and ((node.next_link.data) <data)):
            #check if the node is the bottom right node in the list
            if ((node.next_link.data) == None):
                if node.bot_link == None:
                    #if it's the bottom right, other nodes have been searched
                    #return false
                    return (False, node)
                else:
                    #if it isn't the bottom right node, but the next node is a tail
                    #then go one level down
                    node = node.bot_link
                    return _help_search(node, data)
            #check if next node is greater than data and not none
            elif (((node.next_link.data) > data) and ((node.next_link.data) != None)):
                #if there is a bot link, then go to it, if not then the data
                #is not present in the skip list
                if node.bot_link != None:
                    node = node.bot_link
                    return _help_search(node, data)
                else:
                    return (False, node)
            #if the next node is less than the data, then make that node the
            #current node and recursively call this function
            else:
                node = node.node_link
                return _help_search(node, data)
        #if the next node is a tail node and there is a bot link, set the node to
        #that bot link and recursively call the function
        elif (((node.next_link.data) == None) and (node.bot_link != None)):
            node = node.bot_link
            return _help_search(node, data)
        #if there is no bot or next link, then the search is over, data not found
        else:
            return (False, node)


    def remover(self, data):
        '''
        (object, object) --> NoneType
        
        Removes an element in the skip list class. Takes in an element value data,
        and deletes it from the skip list (self). No return value.
        '''
        #set node to the the start of the skip list
        node = self.start
        #if no next nodes, end early
        if (node == None):
            return
        #find how many level exist in the skip list and assign it to counter
        counter = 1
        while (node.bot_link != None):
            counter += 1
            node = node.bot_link
        #reset node to be the start of the skip list
        node = self.start
        #call a _helper function the amount of rows in the skip list-1
        for i in range(1, counter):
            _help_remove(data, node)
            #check the next row
            node = node.bot_link
            
            
    def _help_remove(self, data, node):
        '''
        A helper function for the remove method of SkipList object. Takes in a
        value (data) and a node in a specific row (node). If data is contained
        in the same row as node, data is spliced out of the list.
        '''
        #loop so long as tail node not reached
        while ((node.next_link.data) != None):
            #if next node is data, then splice next node out of the skip list
            if ((node.next_link.data) == data):
                temp = node.next_link
                temp = temp.next_link
                node.next_link = temp
        #return back to originally called position
        return
    
    
    def count_len(self):
        '''
        (object) --> Int
        
        Counts the amount of elements in the last row. The all rows above the
        last row are subset of itself. Return the number of nodes in the last row.
        '''
        node = self.start
        #if the node is none the list is empty, break early
        if node == None:
            return 0
        #go to the bottom row
        while not(node.is_last):
            node = node.bot_link
        #increment a counter as long as the next link is not a tail
        counter  = 0
        while ((node.next_link.data) != None):
            node = node.next_link
            counter += 1
        #return the number of elements in the last row
        return counter
    
    def compare_last(self, other):
        '''
        (SkipList Object, SkipList Object) --> Bool
        
        Check if last rows of the skip list are equal. Order does not matter.
        Returns True if last rows are equal
        '''
        #since both are skip lists, both must have a starting value
        node = self.start
        node2 = other.start
        #Break early if starting value are both None, or starting values are not
        #consistently None (one or the other is None)
        if node == None and node2 == None:
            return True
        elif node == None and node2 != None:
            return False
        elif node != None and node2 == None:
            return False
        #if lengths of the last row are unequal, break out early
        if ((node.count_len()) != (node2.count_len())):
            return False
        #last nodes have equal elements
        else:
            subset(node, node2)
    
    
    def subset(node, node2):
        '''
        (HeadNode Object, HeadNode Object) --> Bool
        
        Checks if the row of the HeadNode (node), is a subset of the row of the
        HeadNode (node2). Return True if and only if row of node is a subset of
        row of node2.
        '''
        #check node to be empty
        if node == None:
            return True
        elif ((node != None) and (node2 == None)):
            return False
        #go to the bottom row for first node
        while not(node.is_last):
            node = node.bot_link
        #for each element in the bottom row, search for it in the other
        #skip list
        while ((node.next_link.data) != None):
            #search node data in other row
            val = _help_search(node2, node.data)
            #if the node value was not found, return false
            if val[0] == False:
                return val[0]
            else:
                #move on to the next element in the last row
                node = node.next_link
        return True
    

    def find_val(self, data):
        '''
        (SkipList Object, Object) --> int
        
        Returns the total occurances of data in the skiplist self.
        '''
        node = self.start
        #check if node is empty
        if node == None:
            return 0
        #go to the last row of the skiplist
        while (node.bot_link != None):
            node = node.bot_link
        #set a counter to represent the amout of occurances
        counter = 0
        #loop through the elements in the last row
        while ((node.next_link.data) != None):
            #check if next link is data
            if ((node.next_link.data) == data):
                #increment counter
                counter += 1
        #return the counter
        return counter


    def value_string(self):
        '''
        (SkipList Object) --> str
        
        Given a skip list object, return a string of all the values in it's nodes.
        Repeated values are considered as long as it's uniquely represented.
        String returned in format: "['Value1', 'Value2', ..., 'ValueN']"
        '''
        #go to the last node and print all of the values of that row
        node = self.start
        empty = "["
        #if the multiset is empty, return a string for the special case
        if node == None:
            empty += "]"
            return empty
        #go to the last row of the skiplist
        while (node.bot_link != None):
            node = node.bot_link
        #store into a string each value at the nodes
        while ((node.next_link.data) != None):
            empty += str(node.next_link.data)
            #move on to the next node
            node = node.next_link
            #if the next node is a  tail close the bracket here
            #otherwise add a comma
            if ((node.next_link.data) != None):
                empty += ", "
            else:
                empty += "]"
        #return the conjured string    
        return empty
 
    
    def remove_shared(self, other):
        '''
        (SkipList Object, SkipList Object) --> (SkipList Object)
        
        Take all values in the first SkipList (self), and remove the ones that
        are shared in the second SkipList(other).
        Returns a SkipList object
        '''
        import multiset
        
        node = self.start
        node2 = other.start        
        #create a new skiplist
        temp = multiset.Multiset()
        #exit early in special cases where either node or node2 is None
        if node == None:
            return temp
        elif node2 == None:
            return self
        #move both nodes to the last row
        while (node.bot_link != None):
            node = node.bot_link
        while (node2.bot_link != None):
            node = node.bot_link
        #check row values in first node is contained by second row
        while ((node.next_link.data) != None):
            #count how many of the same value the first skip list contains
            val = (node.next_link.data)
            count = node.find_val(val)
            count2 = node2.find_val(val)
            if (count > count2):
                #insert the data into the skip list
                iterations = (count - count2)
                for i in range(0, interations):
                    temp.inserter(val)
            elif (count == 0):
                #insert the data into the skip list
                temp.inserter(val)
            node = node.next_link
        return (temp)
            
    def combine_list(self, other):
        '''
        (SkipList Object, SkipList Object) --> SkipList Object
        
        Given two SkipLists self and other, return a third SkipList object
        which contains a union of the node values of each SkipList.
        '''
        import multiset
        
        #create new SkipList
        temp = multiset.Multiset()
        #indetify start points
        node =  self.start
        node2 = other.start
        #check nodes empty, break early dependingly
        if ((node and node2)== None):
            return temp
        elif ((node == None) and (node2 != None)):
            temp.start = other.start
            temp.end = other.end
            return temp
        elif ((node2 == None) and (node != None)):
            temp.start = self.start
            temp.end = self.end
            return temp
        #both nodes non-empty
        #move both nodes to the last row
        while (node.bot_link != None):
            node = node.bot_link
        while (node2.bot_link != None):
            node2 = node2.bot_link
        #loop through the first row of the node
        while ((node.next_link.data) != None):
            val = (node.next_link.data)
            #insert first lists values into temp
            temp.inserter(val)
            node = node.next_link
        #loop through the second node's row
        while ((node2.next_link.data) != None):
            val = (node2.next_link.data)
            #insert second list values into temp
            temp.inserter(val)
            node2 = node2.next_link
        return temp
    
    
    def intersection(self, other):
        '''
        (SkipList Object, SkipList Object) --> (SkipList Object)
        
        Given a SkipList (self) and another SkipList object (other), return a
        third SkipList Object that resembles the insersection of self and other.
        '''
        import multiset
        #create an empty skiplist
        temp = multiset.Multiset()
        #record start values of each skiplist
        node = self.start
        node2 = other.start
        #check None cases
        if (node or node2) == None:
            return (temp)
        #move both nodes to the last row
        while (node.bot_link != None):
            node = node.bot_link
        while (node2.bot_link != None):
            node2 = node2.bot_link
        #loop through the values in the row of the first node
        while ((node.next_link.data) != None):
            val = node.next_link.data
            #count the amount of the values which are shared
            count = node.find_val(val)
            count2 = node2.find_val(val)
            if count > count2:
                for i in range(0, count2):
                    temp.inserter(val)
            elif ((count < count2) and (count2 != 0)):
                for i in range(0, count):
                    temp.inserter(val)
        return temp
                
        
        
