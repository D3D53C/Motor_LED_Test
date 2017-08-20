h = input('Enter hex: ').lstrip('#')
print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))

print("R = {}".format(int(h[0:0+2], 16)))
print("G = {}".format(int(h[2:2+2], 16)))
print("B = {}".format(int(h[4:4+2], 16)))

s1 = set([])
for i in range (3):
  si.add(int(h[i:i+2], 16) for i in (0, 2 ,4)))
print("RGB => {}, {}, {}".format()
