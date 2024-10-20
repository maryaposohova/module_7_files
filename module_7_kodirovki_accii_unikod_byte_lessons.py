# преобразование символов в ASCII
a = "hello"
chars = []
for i in a:
    chars.append(ord(i))
#  обратное  преобразование ASCII всимволы
s = ''
for i in chars:
    s +=chr(i)
print(chars)
print(s)
#
# for i in range(128): # выйдут все символы Б которым соответствуют числа от 0 до 127
#     print(chr(i))
#
print(hex(ord('h')))
bb = b"\x68"
print(type(bb))
print(bb.decode())
print(hex(123))
bb1 = b"\x7b"
print(bb1)
print(bb1.decode())
