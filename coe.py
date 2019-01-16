from PIL import Image
import sys
if(len(sys.argv) < 3):
	print('输入格式为: python3 coe.py 输入文件名 输出文件名')
	exit()
im = Image.open(sys.argv[1])
pix = im.load()
width, height= im.size
fp = open(sys.argv[2], 'w')
fp.write('memory_initialization_radix = 10;\n')
fp.write('memory_initialization_vector = ')
for y in range(height):
	for x in range(width):
		r, g, b = pix[x, y]
		if x != width - 1 or y != height - 1:
			fp.write(str(r//16+g//16*16+b//16*16*16)+',')
fp.write(str(r//16+g//16*16+b//16*16*16)+';')
fp.close()
print('输出文件: ', sys.argv[2], '...ooook!')
