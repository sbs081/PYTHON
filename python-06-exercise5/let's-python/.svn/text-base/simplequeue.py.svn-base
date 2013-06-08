class queue(object):
	def __init__(self):
		self.datas = []
		self.length = 0
	def insert(self, data):
		self.datas.append(data)
		self.length = len(self.datas)
	def remove(self):
		try:
			return self.datas[0]
		finally:
			del self.datas[0]
			self.length -= 1
	def __len__(self):
		return self.length
	def empty(self):
		return self.length == 0
	def __str__(self):
		return str(self.datas)
	

if __name__ == '__main__':
	q = queue()
	print q.empty()
	for i in range(10):
		q.insert(i)
	print q
	for i in range(5):
		print q.remove()
	print q
	print len(q)