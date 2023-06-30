from Encoder import *
from Decoder import *
# from Utils import *

# # ascii_dict = {
# #     'A' : 0,
# #     'B' : 1,
# #     'C' : 2,
# #     'D' : 3,
# #     'R' : 4
# # }

ascii_count = 256
ascii_range = range(0, ascii_count)
ascii_list = [chr(i) for i in ascii_range]
# # ascii_list = ['A', 'C', 'H', 'S']

# # for i in ascii_count:
# #     ascii_list.append(chr(i))

# # print(ascii_dict.keys())
# # print(ascii_dict['a'])

# # a = []
# # a.append(1)
# # print(a)

# # for i in range (0, 128):
# #     print(i)
# #     print(ascii_list[i])

# a = input()
# enc = encode(a, ascii_list)
# print(enc)
# # nenc = [Utils.decimalToBinary(i) for i in enc]
# # print(nenc)

# # b = [Utils.binaryToDecimal(x) for x in nenc]
# # b = []
# # dec = decode(b, ascii_list)
# # print(dec)

# y = input()
# a = bwtEncode(y)
# b = bwtDecode(a)
# print("BWT encode=", a)
# print("BWT decode=", b)
# c = encode(y, ascii_list)
# d = encode(a, ascii_list)
# print(len(c), "vs", len(d))


# print(c)
# print(d)

# print(decode(c, ascii_list))
# print(bwtDecode(decode(d, ascii_list)))

# mtf = mtfEncode(ipt, ascii_list)
# mtfdec = mtfDecode(mtf, ascii_list)

# print(ascii_list)
# print(mtf)
# print(mtfdec)

# a = encode(ipt, ascii_list)
# b = mtfLZWEncode(mtf, ascii_list)

# print(a)
# print(b)

# print("Ori =", len(a), " vs", "Plus =", len(b))

# # print(ascii_list[48])
# c = decode(a, ascii_list)
# d = decode(b, ascii_list)
# d = mtfDecode(d, ascii_list)

# print(c)
# print(d)

y = input()
g = bwtEncode(y)
print(g)

a = rleEncode(g)
# print(a)
lz = encode(a, ascii_list)
# h = encode(a, ascii_list)
# print(h)
dz = decode(lz, ascii_list)
b = rleDecode(dz)
# print(b)

c = bwtDecode(b)
print(c)