import smbus

class matrix():
	def __init__(self):
		#Initialise matrix
		self.addr = 0x20
		self.dirA = 0x00
		self.dirB = 0x01
		self.portA = 0x12
		self.portB = 0x13
		self.bus = smbus.SMBus(1)
		self.cols = 0x00
		self.rows = 0xFF
		#set lines for output
		self.bus.write_byte_data(self.addr,self.dirA,0x00)
		self.bus.write_byte_data(self.addr,self.dirB,0x00)
		#clear display
		self.bus.write_byte_data(self.addr,self.portA,self.cols)
		self.bus.write_byte_data(self.addr,self.portB, self.rows)

	def drawpixel(self, x, y):
		
		#x, y = value between 0 and 7 (inclusive)
		if (x < 0) or (x > 7):
			raise Exception("X pixel value needs to be between 0 and 7")
		if (y < 0) or (y > 7):
			raise Exception("Y pixel value needs to be between 0 and 7")
		#Deal with x co-ord
		x_colcmd = 0x01<<x
		new_cols = self.cols | x_colcmd
		self.cols = new_cols
		
		#Deal with y co-ord
		y_rowcmd = 0x01<<y
		new_rows = self.rows & ~y_rowcmd
		self.rows = new_rows
		
		#print hex(self.cols), hex(self.rows)
		#print hex(new_cols), hex(new_rows)
		self.bus.write_byte_data(self.addr, self.portA, self.cols)
		self.bus.write_byte_data(self.addr, self.portB, self.rows)
	
	def erasepixel(self, x,y):
		if (x < 0) or (x > 7):
			raise Exception("X pixel value needs to be between 0 and 7")
		if (y < 0) or (y > 7):
			raise Exception("Y pixel value needs to be between 0 and 7")
		
		#Deal with x co-ord
		x_colcmd = 0x01<<x
		new_cols = self.cols & ~x_colcmd
		self.cols = new_cols
		
		#Deal with y co-ord
		y_rowcmd = 0x01<<y
		new_rows = self.rows | y_rowcmd
		self.rows = new_rows
		
		#print hex(self.cols), hex(self.rows)
		#print hex(new_cols), hex(new_rows)
		self.bus.write_byte_data(self.addr, self.portA, self.cols)
		self.bus.write_byte_data(self.addr, self.portB, self.rows)
		
	

