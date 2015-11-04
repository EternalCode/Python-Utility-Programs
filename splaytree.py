"""
A SplayTree class that uses a standard binary tree as a base. Values contained
in the tree are not required to be unique. In addition uses SplayTree operations
such as zig, zag, zig-zig, zag-zag, zig-zag, zag-zig
"""

class BTNode(object):
    '''
    BTNode class for nodes in a tree
    '''
    
    def __init__(self, data, prev = None, left = None, right = None):
        '''
        (BTNode obj, obj, obj, obj, obj) --> NoneType
        
        Initiation method for a BTNode object, takes in a data to be the value
        for the node, with pointers prev, left and right to indicate position.
        Return None.
        '''
        #set constant properties to keep track of node's position
        #and value
        self.data = data
        self.previous = prev
        self.left = left
        self.right = right
        
        
    def __str__(self):
        '''
        (BTNode obj) --> Str
        
        String method for a BTNode. Returns a string of the value of the node.
        '''
        #return the node's data as a string
        return (str(self.data))
    


class SplayTree(object):
    '''
    A SplayTree class containing normal BinaryTree functions with special splaying
    effects such as zig, zag, zig-zig, zig-zag, zag-zig, zag-zag
    '''
    
    def __init__(self, root = None):
        '''
        (SplayTree Obj, Obj) --> NoneType
        
        Creates an empty Binary search tree by default, if a paramater is passed
        in, it creates a Splay tree with a single root node. Return None.
        '''
        #set constants
        self.root = root
        #depth is used to calculate maximum number of node of a certain type
        self.depth = 0
        #maxm is the current maximum value in the tree
        self.maxm = root
        #minm is the current minimum value in the tree
        self.mim = root
        #list for of the tree(ordered)
        self.list_form = []
        
    
    def insert(self, data):
        '''
        (SPTree obj, obj)
        
        Inserts into a splaytree indicated by self the value data in the appropriate
        spot using BinaryTree logic. Return None.
        '''
        #updated a list version of the splay tree
        self.list_form.append(data)
        #if there is no root, just make this node the root
        if self.root == None:
            #there is no need to splay the root
            self.root = BTNode(data)
            self.maxm = self.root
            self.minm = self.root
        #call helper function if root exists
        else:
            self._insert_helper(self.root,data)
            if (self.maxm.data < self.root.data):
                self.maxm = self.root
            if (self.minm.data > self.root.data):
                self.minm = self.root
        
    
    def _insert_helper(self, root, data):
        '''
        (SPTree obj, obj, obj) --> NoneType
        
        Modify the SplayTree given by self directly to have a value (data) inserted
        into the appropriate spot using binary tree logic given the root node.
        Return None.
        '''
        #if the root is less than or equal to the current value to be inserted
        #insert to the right
        if (root.data <= data):
            #if the root;s child is non-empty, keep going right
            if (root.right != None):
                #call recursively for next right child
                self._insert_helper(root.right, data)
            else:
                #current root has no right child, insert value here
                new_node = BTNode(data, root)
                root.right = new_node
                #splay the node that was inserted
                self.splay(new_node)
        #if root is greater than node to be inserted, insert to the left
        if (root.data > data):
            #call recursively if root is greater than data
            if (root.left != None):
                self._insert_helper(root.left, data)
            else:
                #if root has no left child, place this node as it's left
                new_node = BTNode(data, root)
                root.left = new_node
                self.splay(new_node)
               
    
    def __str__(self):
        '''
        (SPTree Obj)--> str
        
        String method for a SplayTree, return a string representation of the 
        splay tree vertically where the right subtree is on top, followed by 
        the root and the left subtree.
        '''
        #handle empty case
        if (self.root == None):
            return ("")
        #call helper function on non-empty case
        else:
            return self._str_helper(self.root, "   ")


    def _str_helper(self, root, indentation, ret = ""):
        '''(BSTNode, str) -> str
        
        Return a string representing the tree rooted at this node, with
        the left and right subtrees below and above (respectively) indented
        to look like a tree turned 90 degrees counter-clockwise. 
        '''
        ###
        ###Mostly copied from given BTTree Class in tutorial
        ###
        #if right subtree non-empty add it to string
        if root.right != None:
            ret = self._str_helper((root.right), indentation + "  ")
        #if root non-empty add it to string(always non-empty)
        if root != None:
            ret += indentation + str(root) + "\n"
        #if left subtree non-empty add it to string
        if root.left != None:
            ret += self._str_helper((root.left), indentation + "  ") 
        #return the string
        return ret        


    def search(self, search_value):
        '''
        (SPTree obj, obj) --> Bool
        
        Given a Splaytree object (self) and a value to find, return true
        iff the value exists within the splay tree.
        '''
        #call a helper function passing in the root node
        return self._search_helper(self.root, search_value)
    
    def _search_helper(self, root, search_value):
        '''
        '''
        if (root == None):
            return False
        #The root is the node we are searching for
        if (root.data == search_value):
            #always splay the value we find
            self.splay(root)
            return True
        #if the root is greater than the value we are searching for transverse left
        elif (root.data > search_value) and (root.left != None):
            return self._search_helper(root.left, search_value)
        #if the root is less than the value we are searching for transeverse right
        elif (root.data < search_value) and (root.right != None):
            return self._search_helper(root.right, search_value)
        #if the value we are searching for doesn't exist
        else:
            return False


    def delete(self, del_value):
        '''
        (SPTree obj, obj)--> NoneType
        
        Given a Splaytree object, delete from it a value (del_value) if the
        del_value exists. Return None.
        '''
        #call a deleting helper function
        self._del_helper(self.root, del_value)
            
    
    def _del_helper(self, root, del_value):
        '''
        (SPTree obj, obj, obj) --> NoneType
        
        Given a SplayTree object, delete form it a value (del_value) if the
        del_value exists given where the root of the node is. Return None.
        '''
        #check if value is in the tree
        if (self.search(del_value)):
            #update list version first
            self.list_form.remove(del_value)
            #searching splays the node for us, so we just need to delete the
            #root everytime we are deleting
            if (self.root.left == None) and (self.root.right == None):
                #if left and right child don't exist, then the root is the only
                #node in the tree, delete it
                self.root = None
            if (self.root != None):
                if (self.root.left != None) and (self.root.right == None):
                    #if root's left child exists but not the right child
                    #make the left child the root and update it's previous to none
                    self.root = self.root.left
                    self.root.previous = None
                if (self.root.left == None) and (self.root.right != None):
                    #if only right child exists in the tree, the make the right child
                    #the root, and update it's previous to None
                    self.root = self.root.right
                    self.root.previous = None
                #hard case where both sub trees exist
                if (self.root.right != None) and (self.root.left != None):
                    #make the left child become the right child's first child's left
                    #subtree and update previous
                    #then make the right child be to root and update previous
                    self._transinsert(self.root.right, self.root.left)
                    self.root = self.root.right
                    self.root.previous = None
            #recalculate new maximum if maximum was deleted
            if (del_value == self.maxm.data):
                self.maxm = self._new_max(self.root)
            #recalculate new minimum if it was deleted
            if (del_value == self.minm.data):
                self.minm = self._new_min(self.root)
        else:
            #if the value is not in the tree, do nothing
            return
           
   
    def _new_min(self, root):
        '''
        (SPTree, obj) --> NoneType
        
        Given a SplayTree, find it's minimum node value, and return that node
        '''
        #start at the root
        c_min = root
        while (root!= None and root.left != None):
            #go to the left most node
            if (root.left.data <= c_min.data):
                #update c_min
                c_min = root.left
            #move on to te next node
            root = root.left
        return c_min
        
   
    def _new_max(self, root):
        '''
        (SPTree, obj) --> NoneType
        
        Given a SplayTree, find it's maximum node value, and return that node
        '''
        #start at the root
        c_max = root
        while (root != None and root.right!= None):
            #go to the right most node
            if (root.right.data >= c_max.data):
                #update c_max if node is equal to or greater
                c_max = root.right
            #move on to next node
            root = root.right
        #return the max node
        return c_max
        
      
    def _transinsert(self, root, left_child):
        '''
        (SPTree, obj, obj) --> NoneType
        
        Given a SplayTree, insert a left_child to the left most node of the
        SplayTree's given root node. Return None.
        '''
        #make sure the left child is not None, if it is do nothing
        if (left_child != None):
            #if the current node is none, insert the child there
            if (root == None):
                root = left_child
            elif root.left == None:
                #if the root's left is none, insert the child there and update
                #previous for the child
                root.left = left_child
                left_child.previous = root
            else:
                #recursively call this function for the next left child
                self._transinsert(root.left, left_child)
    
    
    def splay(self, node):
        '''
        (SPTree, obj) --> NoneType
        
        Core function. Given a Splaytree and a node, splay that node using the 
        appropriate procedure (zig, zag, zig-zig, zag-zag, zig-zag, zag-zig) until
        the given node becomes the root node. Return None.
        '''
        #check if the parent node is a root or not
        if (node.previous == None) or (node == None):
            #if it is, we are done splaying update node to be root and update prev
            self.root = node
            self.root.previous = None
        #if node is not the root and node's parent is the root
        elif (node.previous != None) and(node.previous.previous == None):
            #call zig or zag depending on the node's position
            if (node.previous.data)>(node.data):
                self.zig(node)
            else:
                self.zag(node)
        #node's parent is not the root nor is the node
        else:
            #call a helper function to check node's position relative to other 
            #nodes and store it in a variable temp
            temp = self._parent_status(node)
            #if temp is 1, then node is a right-right relation
            if (temp == 1):
                #call zag-zag on the node (zig-zig-right)
                self.zig_zig_right(node)
            #if temp is 2, then node is a left-left relation
            elif (temp == 2):
                #call zig-zig on the node
                self.zig_zig(node)
            #if temp is 3, then the node is a left-right relation
            elif (temp == 3):
                #call zig-zag on the node
                self.zig_zag(node)
            else:
                #node must be a right-left relation, call zag-zig on it(zig-zag-left)
                self.zig_zag_left(node)
            #call the function on the node again (will be done until it's the root
            self.splay(node)

    
    def zig(self, node):
        '''
        (SPTree, Obj) --> NoneType
        
        Use SplayTree zig operation on the given node which is a left child
        of a parent node who is the root. Return None.
        '''
        #Normal zig operation procedure, but update previous property
        node.previous.left = node.right
        if (node.right != None):
            node.right.previous = node.previous
        node.previous.previous = node
        node.right = node.previous
        node.previous = None
        #make the node into the new root
        self.root = node
    
    
    def zag(self, node):
        '''
        (SPTree, Obj) --> NoneType
        
        Use SplayTree zag operation on the given node which is a right child
        of a parent node who is the root. Return None.
        '''
        #Normal zag operation procedure, opposite of zig, but update previous
        #property of all nodes involved
        node.previous.right = node.left
        if (node.left != None):
            node.left.previous = node.previous
        node.previous.previous = node
        node.left = node.previous
        node.previous = None
        #make the node into the new root
        self.root = node
        
        
    def zig_zig(self, node):
        '''
        (SPTree, Obj) --> NoneType
        
        Use SplayTree zig-zig operation on the given node which is a left child
        of a parent node who is a left child of a grandparent node. Return None.
        '''
        #Standard zig-zig operations, updating previous property of nodes involved
        node.previous.left = node.right
        if (node.right != None):
            node.right.previous = node.previous
        node.right = node.previous
        node.previous.previous.left = node.previous.right
        if node.previous.right != None:
            node.previous.right.previous = node.previous.previous
        node.previous.right = node.previous.previous
        if ((node.previous.previous) != None):
            node.previous = node.previous.previous.previous
        node.right.right.previous = node.right
        node.right.previous = node
        #update node's grandparent's parent to point at this node
        #depending on grandparent's value
        if (node.previous != None):
            if (node.previous.data > node.data):
                node.previous.left = node
            else:
                node.previous.right = node
    
    
    def zig_zig_right(self, node):
        '''
        (SPTree, Obj) --> NoneType
        
        Use SplayTree, zag-zag operation on the given node which is a right child
        of a parent node who is a right child of a grandparent node. Return None.
        '''
        #Standard zag-zag operation, but updating previous of all nodes involved
        #almost the opposite of zig-zig with a few minor changes
        node.previous.right = node.left
        if (node.left != None):
            node.left.previous = node.previous
        node.left = node.previous
        node.previous.previous.right = node.previous.left
        if(node.previous.left != None):
            node.previous.left.previous = node.previous.previous
        node.previous.left = node.previous.previous
        node.previous = node.previous.previous.previous
        node.left.left.previous = node.left
        node.left.previous = node
        #update grandparent's previous to point to this node depending on
        #the grandparent's value
        if (node.previous != None):
            if (node.previous.data > node.data):
                node.previous.left = node
            else:
                node.previous.right = node
    
    
    def zig_zag(self, node):
        '''
        (SPTree, Obj) --> NoneType
        
        Use SplayTree, zig-zag operation on the given node which is a left child
        of a parent node who is the right child of a grandparent node. Return None.
        '''
        #standard zig-zag operation, but updating previous of all nodes involved
        if (node.left != None):
            node.left.previous = node.previous
        node.previous.right = node.left
        if (node.right != None):
            node.right.previous = node.previous.previous
        node.previous.previous.left = node.right
        node.left = node.previous
        node.right = node.previous.previous
        node.left.previous = node
        node.previous = node.right.previous
        node.right.previous = node
        #update the grandparent's previous to point to this node depending on
        #the grandparent's value
        if (node.previous != None):
            if (node.previous.data > node.data):
                node.previous.left = node
            else:
                node.previous.right = node
    
    
    def zig_zag_left(self, node):
        '''
        (SPTree, Obj) --> NoneType
        
        Use SplayTree, zag-zig operation on the given node which is a right child
        of a parent node who is the left child of a grandparent node. Return None.
        '''
        #Standard zag-zig operation, but updating previous of all nodes involvd
        if node.right != None:
            node.right.previous = node.previous
        node.previous.left = node.right
        if node.left != None:
            node.left.previous = node.previous.previous
        node.previous.previous.right = node.left
        node.right = node.previous
        node.left = node.previous.previous
        node.right.previous = node
        node.previous = node.left.previous
        node.left.previous = node 
        #update the grandparent's revious to point to this node depending on
        #the grandparent's value
        if (node.previous != None):
            if (node.previous.data > node.data):
                node.previous.left = node
            else:
                node.previous.right = node
        
  
    
    def _parent_status(self, node):
        '''
        (SPTree, Obj) --> NoneType
        
        Given a standard SplayTree, determine the node's position relative to
        other nodes in the tree. Return None.
        '''
        #check if node is right child or left child
        if (node.data >= node.previous.data):
            if (node.previous.data >= node.previous.previous.data):
                #if both grandchild and child are right childre
                #return integer 1
                return(1)
            else:
                #if grandchild is a right child of a parent who is a
                #left child return integer 3
                return (3)
        elif (node.data < node.previous.data):
            if (node.previous.data <= node.previous.previous.data):
                #if both grandchild and child are left children
                #return integer 2
                return(2)
            else:
                #if grandchild is a left child of a parent who is a
                #right child return integer 4
                return (4)

    def count(self, data):
        '''
        (SPTree, obj) --> int
        
        Given a SplayTree, calculate the number of nodes which share the value 
        data in them. Return an integer containing the number of nodes in self
        which have a value data.
        '''
        #check if the node is in the tree
        if not(self.search(data)):
            #if it's not exit early and return 0
            #search splays for us, so no need to splay
            return 0
        node = self.root
        #set node depth to be 0
        self.depth = 0
        #call helper function to calculate identical children in subtrees
        self.depth =  self._h_count(self.root, data, self.depth)
        #take into account the root being the value we are looking for
        if node.data == data:
            self.depth += 1
        #return the number of occurences
        return self.depth
        
    def _h_count(self, node, data, depth):
        '''
        (SPTree, obj, obj, int) --> int
        
        Helper function of count. Takes in same parameters as count, except
        with a counter (depth) and a pointer to a node (node). Returns the 
        number of occurences of node in the tree (excluding the root).
        '''
        #if the node has a right child check that child first
        if node.right != None:
            #if the right child has the value we are looking for update a counter
            if node.right.data == data:
                self.depth += 1
            #recursively call the next right child
            self._h_count(node.right, data,self.depth)
        #if the node has a left child check it's value
        if node.left != None:
            #if the left child has the value we are looking for update a counter
            if node.left.data == data:
                self.depth += 1
            #recursively call the next left child
            self._h_count(node.left, data, self.depth)
        #return number of occurences of data in the subtrees
        return self.depth
    
    
    def max(self):
        '''
        (SPTree) --> obj
        
        Given a SplayTree, return it's maximum value. Splay the maximum value.
        '''
        #If splaytree's max node is not none, splay it
        if self.maxm != None:
            self.splay(self.maxm)
            return (self.maxm.data)
        #return the max node in the tree
        return (None)
    
    def min(self):
        '''
        (SPTree) --> obj
        
        Given a SplayTree, return it's maximum value. Splay the maximum value.
        '''
        #If splaytree's min node is not none, splay it
        if self.minm != None:
            self.splay(self.minm)
            return (self.minm.data)
        #return the min node in the tree
        return (None)
    
    def transverse(self):
        '''
        (SPTree) --> obj
        
        Given a SplayTree, return a list of it's node values in sorted order.
        '''
        self.list_form.sort()
        return self.list_form
        
