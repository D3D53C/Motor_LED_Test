h = input('Enter hex: ').lstrip('#')
print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))

s1 = [0 ,1 ,2]
s1[0] = int(h[0:0+2], 16))
s1[1] = int(h[2:2+2], 16))
s1[2] = int(h[4:4+2], 16))

print("RGB {0:f}, {1:f}, {2:f}".format(s1[0],s1[1],s1[2]))
