import math
def decToBin(number):
     #convert decimal to binary using multiplication-remainder method
     bin_rep = ""
     prev_num = number
     while (prev_num >= 1):
          calculation = divmod(prev_num, 2)
          bin_rep = str(calculation[1]) + bin_rep
          prev_num = calculation[0]
     return str(bin_rep)

def binToDec(number):
     #convert binary to decimal using sum of powers of two method
     str_rep = str(number)
     result = 0
     for i in range(0, len(str_rep)):
          result += int(str_rep[len(str_rep) - (i +1)]) * int(math.pow(2, i))
     return result
     
     
#Here are some generalized converting functions. The math behind the functions 
#and the algorithm allow for generalized conversion functions

def baseToDec(number, base):
     #convert base to decimal using sum of powers method
     str_rep = str(number)
     result = 0
     for i in range(0, len(str_rep)):
          result += int(str_rep[len(str_rep) - (i +1)]) * int(math.pow(base, i))
     return result
     
     #there is a weakness to this code. That is that numbers like hexadecimal
     #which use numbers like 0xAFF72E, are unrecongnized by "int" 
     #such types of numbers, need their base values predefined.