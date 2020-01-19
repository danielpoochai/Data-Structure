import time

#counting sort
def quickSort(arr):
	smaller = []
	bigger = []
	keylist = []

	if len(arr) <= 1:
		return arr

	else: 
		key = arr[0].y
		for i in arr:
			if i.y < key:
				smaller.append(i)
			elif i.y > key: 
				bigger.append(i)
			else:
				keylist.append(i)

		smaller = quickSort(smaller)
		bigger = quickSort(bigger)
		return smaller + keylist + bigger



def countingSort(arr, exp1):
	n = len(arr)

	output = [0] * n

	count = [0] * 10

	for i in range(0, n):
		index = (arr[i].y//exp1)
		count[ (index)%10 ] += 1

	for i in range(1, 10):
		count[i] += count[i-1]

	i =  n-1
	while i>=0:
		index = (arr[i].y//exp1)
		output[count[(index)%10] - 1] = arr[i]
		count[ (index) % 10] -= 1
		i -= 1

	i = 0

	for i in range(0, len(arr)):
		arr[i] = output[i]

def radixSort(arr, max_level):

	exp = 1
	while max_level/exp > 0:
		countingSort(arr, exp)
		exp *= 10

def Parenthesis_Rep(node, p_rep):
	p_rep.append(node.data)

	if node.left:
		p_rep.append("(")
		Parenthesis_Rep(node.left, p_rep)

	else: 
		if node.right:
			p_rep.append("(")
			p_rep.append("-")

	if node.right:
		Parenthesis_Rep(node.right, p_rep)
		p_rep.append(")")

	else:
		if node.left:
			p_rep.append("-")
			p_rep.append(")")

	return p_rep

def construct_level(node, level):
	if node:
		node.y = level

		if node.left:
			construct_level(node.left, level+1)

		if node.right:
			construct_level(node.right, level+1)


#for Binary-Tree
class Node:
	def __init__(self, data, parent):
		self.left = None
		self.right = None
		self.parent = parent
		self.data = data
		self.x = 0
		self.y = 0


	def insert(self, data, level = 0):
		if self.data>0:
			if data < self.data:
				if self.left is None:
					self.left = Node(data, self)
					self.left.y = level + 1
					return self.left
				else:
					return self.left.insert(data, level+1)

			elif data > self.data:
				if self.right is None:
					self.right = Node(data, self)
					self.right.y = level + 1
					return self.right
				else:
					return self.right.insert(data, level+1)
		else:
			self.data = data
			self.y = level
			return self

	def InOrder_Traverse(self, seq):
		if self.left:
			self.left.InOrder_Traverse(seq)
		
		# length = len(seq)

		# if length!=0:
		# 	if seq[length-1].data//10 > 0: 
		# 		if seq[length-1].data//100 > 0: #front is 3 digit
		# 			self.x = len(seq) + 1 
		# 		else: #front is 2 digit
		# 			self.x = len(seq) + 2
		# 	else:
		# 		self.x = len(seq) + 3

		self.x = len(seq)
		seq.append(self)

		if self.right:
			self.right.InOrder_Traverse(seq)


		return seq
		
#for Splay-Tree
class SplayTree:
	def __init__(self):
		self.root = None
		self.height_valid = False

	def insert(self, data):
		if not self.root:
			node = self.root = Node(data, None)
		else:
			node = self.root.insert(data)

		self.splay(node)

	def splay(self, node):
		while node != self.root:
			self.move_up(node)

	def move_up(self, node):
		if node == self.root:
			return
		elif node.parent == self.root:
			if node.parent.left == node: #l case
				if node.right:
					node.right.parent = self.root
				self.root.left = node.right
				node.right = self.root
				self.root.parent = node
				node.parent = None
				self.root = node

			else: #right casej 
				if node.left:
					node.left.parent = self.root
				self.root.right = node.left
				node.left = self.root
				self.root.parent = node 
				node.parent = None
				self.root = node
		else:
			p = node.parent
			gp = node.parent.parent

			if node.parent.left == node:
				if gp.left == p: #LL
					if node.right:
						node.right.parent = p 
					p.left = node.right

					if p.right:
						p.right.parent = gp
					gp.left = p.right
					node.right = p
					p.parent = node
					node.parent = gp.parent

					if not gp.parent:
						self.root = node
					else:
						if gp.parent.left == gp:
							gp.parent.left = node
						else:
							gp.parent.right = node
					p.right = gp
					gp.parent = p 
				else: #RL
					if node.right:
						node.right.parent = p 
					p.left = node.right
					if node.left:
						node.left.parent = gp
					gp.right = node.left
					p.parent = node
					node.right = p
					node.parent = gp.parent

					if not gp.parent:
						self.root = node
					else:
						if gp.parent.left == gp:
							gp.parent.left = node
						else:
							gp.parent.right = node
					node.left = gp
					gp.parent = node
			else:
				if node.parent.parent.left == node.parent: #LR
					if node.left:
						node.left.parent = p
					p.right = node.left
					if node.right:
						node.right.parent = gp
					gp.left = node.right
					p.parent = node
					node.left = p
					node.parent = gp.parent

					if not gp.parent:
						self.root = node
					else:
						if gp.parent.left == gp:
							gp.parent.left = node
						else:
							gp.parent.right = node
					node.right = gp
					gp.parent = node

				else: #RR
					if node.left:
						node.left.parent = p
					p.right = node.left

					if p.left:
						p.left.parent = gp
					gp.right = p.left
					node.left = p
					p.parent = node
					node.parent = gp.parent
					if not gp.parent:
						self.root = node
					else:
						if gp.parent.left == gp:
							gp.parent.left = node
						else:
							gp.parent.right = node
					p.left = gp
					gp.parent = p 

t1 = time.time()
time.sleep(0)

fp = open("input.txt", "r", encoding="utf-8")

BTree = open("BTree.txt", "w")
BTree_PRep = open("BTree_PRep.txt", "w")
BTree_bound = open("BTree_boundary.txt", "w") 

STree = open("STree.txt", "w")
STree_PRep = open("STree_PRep.txt", "w")
STree_bound = open("STree_boundary.txt", "w")


line = fp.readline()

while line:
	#split the space
	str_tmp = line.split()

	#construct BTree && splayTree
	root = Node(0, None)
	splaytree = SplayTree()

	for data in str_tmp:
		root.insert(int(data), 0)
		splaytree.insert(int(data))

	construct_level(splaytree.root, 0)

	seq = []
	p_rep = []
	max_level = 0 
	max_width = 0

	splay_seq = []
	sp_rep = []
	smax_level = 0 
	smax_width = 0

	#set node.x coordinate
	root.InOrder_Traverse(seq)
	splaytree.root.InOrder_Traverse(splay_seq)

	#sort nodes by level (node.y)
	for node in seq :
		if node.y > max_level: max_level = node.y
		if node.x > max_width: max_width = node.x

	#quickSort(seq)
	#radixSort(seq, max_level)

	for node in splay_seq:
		if node.y > smax_level: smax_level = node.y
		if node.x > smax_width: smax_width = node.x

	#quickSort(seq)
	#radixSort(splay_seq, smax_level)


	table = [[0 for i in range(max_width+1)] for j in range(max_level+1)] 
	s_table = [[0 for i in range(smax_width+1)] for j in range(smax_level+1)]

	for node in seq:
		table[node.y][node.x] = node.data

	for y_idx in range(max_level+1):
		for x_idx in range(max_width+1):
			if table[y_idx][x_idx] > 0:
				for idx in reversed(range(x_idx)):
					if table[y_idx][idx] > 0:
						break
					else:
						table[y_idx][idx] = -1

	

	for node in splay_seq:
		s_table[node.y][node.x] = node.data
		# print(node.data, node.x, node.y)

	for y_idx in range(smax_level+1):
		for x_idx in range(smax_width+1):
			if s_table[y_idx][x_idx] > 0:
				for idx in reversed(range(x_idx)):
					if s_table[y_idx][idx] > 0:
						break
					else:
						s_table[y_idx][idx] = -1 

	#write BTree.txt
	for i in range(max_level+1):
		for j in range(max_width):
			data = table[i][j] 
			if data > 0:
				if table[i][j+1] != 0: #not to change line yet
					if data//10 > 0: #more than two digits
						if data//100 > 0: #data is three digit
							BTree.write(str(table[i][j]))
						else: #data is two digit
							BTree.write(str(table[i][j]))
							BTree.write("\u00a0")
					else:#one digits
						BTree.write(str(table[i][j]))
						BTree.write("\u00a0")
						BTree.write("\u00a0")
				else: #change line
					BTree.write(str(table[i][j]))
					break
			elif data == -1: 
				BTree.write("\u00a0")
				BTree.write("\u00a0")
				BTree.write("\u00a0")

		if table[i][j+1] != 0:
			BTree.write(str(table[i][j+1]))
		
		BTree.write("\r\n")

	#Write STree.txt
	for i in range(smax_level+1):
		for j in range(max_width):
			data = s_table[i][j] 
			if data > 0:
				if s_table[i][j+1] != 0: #not to change line yet
					if data//10 > 0: #more than two digits
						if data//100 > 0: #data is three digit
							STree.write(str(s_table[i][j]))
						else: #data is two digit
							STree.write(str(s_table[i][j]))
							STree.write("\u00a0")
					else:#one digits
						STree.write(str(s_table[i][j]))
						STree.write("\u00a0")
						STree.write("\u00a0")
				else: #change line
					STree.write(str(s_table[i][j]))
					break
			elif data == -1: 
				STree.write("\u00a0")
				STree.write("\u00a0")
				STree.write("\u00a0")

		if s_table[i][j+1] != 0:
			STree.write(str(s_table[i][j+1]))

		STree.write("\n")
	
	#write BTree_PRep.txt
	P_rep = Parenthesis_Rep(root, p_rep)
	front = False #check pre_out is number, "-" or not
	rp_front = False
	for out in P_rep:
		if out == "(" or out == ")":
			BTree_PRep.write(out)
			front = False
			if out == ")":
				rp_front = True
			else:
				rp_front = False
		else:
			if front or rp_front:
				BTree_PRep.write("\u00a0")
			BTree_PRep.write(str(out))
			front = True
	BTree_PRep.write("\n")

	#write STree_PRep.txt
	SP_rep = Parenthesis_Rep(splaytree.root, sp_rep)
	sfront = False
	srp_front = False
	for out in SP_rep:
		if out == "(" or out == ")":
			STree_PRep.write(out)
			sfront = False
			if (out == ")"):
				srp_front = True
			else:
				srp_front = False
		else:
			if sfront or srp_front:
				STree_PRep.write("\u00a0")
			STree_PRep.write(str(out))
			sfront = True
	STree_PRep.write("\n")

	#write BTree_boundary.txt
	for i in range(max_level+1):
		for j in range(max_width+1):
			if(table[i][j] > 0):
				BTree_bound.write(str(table[i][j]))
				break
		if i != max_level:
			BTree_bound.write("\u00a0")
	BTree_bound.write('\n')

	#write STree_boundary.txt
	for i in range(smax_level+1):
		for j in range(smax_width+1):
			if (s_table[i][j] > 0):
				STree_bound.write(str(s_table[i][j]))
				break
		if i != smax_level:
			STree_bound.write("\u00a0")
	STree_bound.write('\n')

	
	#read the next tree	
	line = fp.readline()



fp.close()
BTree.close()
BTree_PRep.close()
BTree_bound.close()
STree.close()
STree_PRep.close()
STree_bound.close()
t2  = time.time()

print(str(t2-t1))


