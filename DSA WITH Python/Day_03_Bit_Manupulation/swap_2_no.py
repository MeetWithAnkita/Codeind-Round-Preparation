a = int(input())
b = int(input())
# in XOR = [a^a = 0 , a^0 =a]
a = a^b
b = a^b 
# b = (a^b)^b = a^0 = a  
a = a^b
# a = (a^b) ^ a = (b^0) = b

print ("a: ",a, " b: ",b)