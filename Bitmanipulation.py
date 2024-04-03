#Convert a number to binary and then count the set bits and form a
#minimized number where the set bits are in consective order in binary 

n=10
binary=bin(n)[2:]
count_set_bits=binary.count('1')
result=(1 << count_set_bits) - 1
print(result)