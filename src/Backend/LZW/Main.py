from Encoder import *
from Decoder import *
from Utils import *

# ascii_dict = {
#     'A' : 0,
#     'B' : 1,
#     'C' : 2,
#     'D' : 3,
#     'R' : 4
# }

ascii_count = 256
ascii_range = range(0, ascii_count)
ascii_list = [chr(i) for i in ascii_range]
# ascii_list = ['A', 'C', 'H', 'S']

# for i in ascii_count:
#     ascii_list.append(chr(i))

# print(ascii_dict.keys())
# print(ascii_dict['a'])

# a = []
# a.append(1)
# print(a)

# for i in range (0, 128):
#     print(i)
#     print(ascii_list[i])

a = input()
enc = encode(a, ascii_list)
print(enc)
# nenc = [Utils.decimalToBinary(i) for i in enc]
# print(nenc)

# b = [Utils.binaryToDecimal(x) for x in nenc]
# b = []
# dec = decode(b, ascii_list)
# print(dec)