class bloom_filter:
     '''
     Bloom Filter class, creates bloom_filter objects which help keep track of
     inserted values using hash function: h4 = [h1 - 2 * h2 + h4]%field_length
     '''
     
     def __init__(self, bits):
          '''(Bloom Filter Obj, int) --> NoneType
          Initiates a Bloom Filter Object. The length of
          the Bloom Filter's bit field is defined by paramater bits.
          If bits is a fractional, it will be rounded down.
          '''
          self.bits = ""
          self.bits += ('0')*int(bits)
          self.length = len(self.bits)-1


     def check(self, val):
          '''(Bloom Filter Obj, Obj) --> bool
          Check's the Bloom Filter object for a value(val). If the value
          may be inserted previously return True, else return False. False
          implies either val was definitely not inserted or the bit string is 
          length zero.
          '''
          #incase 0 bit field size always return false
          if ((self.length < 0)):
               return False
          #get hash value of val
          h4 = ((self._div_remainder(self._num(val),5) - 2 * 
                 self._mid_sqr(self._num(val)) + 
                 self._fold_hash(self._num(val)))%self.length)
          #check return bit is on at hash(val)
          if (int(self.bits[h4]) == 0):
               return False
          else:
               return True
          
          
     def _div_remainder(self, value, mod):
          '''(Bloom Filter Obj, int, number) --> int
          Division remainder hashing function to hash an int (value),
          using a mod specified (mod). Returns the result of value%mod
          '''
          return (value%mod)
     
     
     def _mid_sqr(self, value):
          '''(Bloom Filter Obj, number) --> int
          Middle square hashing function applied to an int (value).
          Returns the 2 middle numbers if the number is even length, else
          returns the middle number.          
          '''
          #middle square
          value *= value
          temp = str(value)
          if len(temp)%2 == 0:
               #even case
               return (int(temp[len(temp)//2-1:len(temp)//2+1]))
          else:
               #odd case
               return (int(temp[len(temp)//2]))
          
          
     def _fold_hash(self, value):
          '''(Bloom Filter Obj, number) --> int
          Applies a customized version of the Fold hashing function to a number
          (value). The result is returned.
          '''
          #folding method
          #turn into 4 digit number
          while (len(str(value)) != 4):
               if len(str(value)) < 4:
                    value *= value
                    value += 2
               if len(str(value)) > 4:
                    value *= 0.5
                    value = int(value)
          #apply fold
          temp = str(value)
          return (int(temp[:2])) + (int(temp[:2]))
         
         
     def _num(self, value):
          '''(Bloom Filter Obj, Obj) --> int
          Takes some object with an str function, and converts it into an
          integer. The integer representation of the object is returned
          '''
          if str(value).isnumeric():
               return int(value)
          else:
               #convert the string or whatever into an integer
               to_return = 0
               dict_alpha = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, 
                             "H":8, "I":9, "J":10,"K":11,"L":12,"M":13,"N":14,
                             "O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,
                             "V":22,"W":23,"X":24,"Y":25,"Z":26}
               for element in (str(value).upper()):
                    #if value is not alphabetical, just put in 27
                    if dict_alpha.__contains__(element):
                         to_return += dict_alpha[element]
                    else:
                         to_return += 27
               return to_return
                    
                    
     def ins(self, val):
          '''(Bloom Filter Obj, Obj) --> NoneType
          Hashes an object (val) onto the Bloom Filter bit field.
          The Hashed bit it turned from 0 to 1, or is unchanged.
          '''
          #get hash value of val
          h4 = ((self._div_remainder(self._num(val),5) - 2 * 
                 self._mid_sqr(self._num(val)) + 
                 self._fold_hash(self._num(val)))%self.length)
          #modify bit field to have the index h4 turned on
          new_b_string = ""
          for i in range(0, len(self.bits)):
               if i == h4:
                    new_b_string += "1"
               else:
                    new_b_string += self.bits[i]
          self.bits = new_b_string
     
     
     def status(self):
          '''(Bloom Filter Obj) --> str
          Returns a status message of the Bloom Filter's current state.
          '''
          #get indicies where bits are turned on
          on_bits = ""
          for index in range(0, len(self.bits)):
               if self.bits[index] == '1':
                    on_bits += ((str(index+1) + " "))
          #give report of Bloom Filter object
          return ("The BloomFilter consists of " + str(self.length +1) + " bits"
                    + "\nWith current state: " + self.bits + "\n"
                    + "The bits that are on include: " + on_bits)