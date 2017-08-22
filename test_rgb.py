from rgb_led import RGB_LED as RGB
rgb = RGB(11,13,15)


h = input('Enter hex: ').lstrip('#')
print(h)
rgb.on(h)
