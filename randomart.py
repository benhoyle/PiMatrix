from matrixcontrol import matrix
import random, time

mat = matrix()
while True:
	#select one of draw or erase
	d_e = random.randint(0,1)
	dur = random.randint(1,10)/10
	x = random.randint(0,7)
	y = random.randint(0,7)
	
	if d_e:
		mat.drawpixel(x,y)
	else:
		mat.erasepixel(x,y)
	
	time.sleep(dur)