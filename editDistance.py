"""
Class:
    CSE 331
Project:
    Edit Distance
Version:
    0.2
Authors:
    Malcolm Fraser
    Gregory Langlois
Description:
    The program will read a file & parse it into four 
    parts & return a list containing them. Then it will 
    create two variables named x and y that contain the strings.
    Then a 2d list is created from the two strings, named matrix.
    The matrix and two strings are passed to the edit distance 
    function. There the two strings are used to populate the matrix,
    @ every index a third list is stored with the min cost value &
    operation that is performed. Once the matrix is full, it is returned
    and then pass to the printdistance function which walks through the
    matrix tacking the min cost path and fills a list, from there it is
    then printed out in order.
"""

def editdistance(matrix,x,y):
	for i in range(len(y) + 1):
		for j in range(len(x) + 1):
			mincost = 999999999999999999
			opcost = ""
			val = 0
			if i == 0 and j == 0:
				matrix[i][j] = [0,'initial',0]
				continue
			if i > 0 and j > 0 and x[j-1] == y[i-1]:
				c = matrix[i-1][j-1][0] + 0
				if c < mincost:
					mincost = c
					opcost = "right"
					val = 0
			if i > 0 and j > 0:
				c = matrix[i-1][j-1][0] + 4
				if c < mincost:
					mincost = c
					opcost = "replace"
					val = 4
			if i > 0 :
				c =  matrix[i-1][j][0] + 3
				if c < mincost:
					mincost = c
					opcost = "insert"
					val = 3
			if j > 0:
				c = matrix[i][j-1][0]+2
				if c < mincost:
					mincost = c
					opcost = "delete"
					val = 2
			matrix[i][j] = [mincost,opcost,val]
	return matrix


def pathprint(x,y,matrix):
	path = []
	i = len(y)
	j = len(x)

	path.insert(0,[0,'initial',0])
	while i != 0 or j != 0:
		opr = matrix[i][j][1]
		path.insert(0,opr)
		if opr == "insert":
			i = i - 1
			j = j - 0
		if opr == "replace":
			i = i - 1
			j = j - 1
		if opr == "delete":
			i = i - 0
			j = j - 1
		if opr == "right":
			i = i - 1
			j = j - 1
		if opr == "initial":
			i = i - 0
			j = j - 0

	print("%8s | %2s | %4s | %2s" %("Oper","c","Total","z"))
	for k in range(len(path)):
		oper = matrix[i][j][1]
		c = matrix[i][j][2]
		cst = matrix[i][j][0]
		print("%8s | %2s | %5s | %2s" %(oper,c,cst,y[0:i]+"*"+x[j:]))

		if path[k] == "insert":
			i = i + 1
			j = j + 0
		if path[k] == "replace":
			i = i + 1
			j = j + 1
		if path[k] == "delete":
			i = i + 0
			j = j + 1
		if path[k] == "right":
			i = i + 1
			j = j + 1
		if path[k] == "initial":
			i = i + 0
			j = j + 0

def build_matrix(x,y):
	m = []
	n = []
	n.append([0,'',0])
	for i in range(len(x)):
		n.append([0,'',0])
	m.append(n)
	for i in range(len(y)):
		 o = []
		 o.append([0,'',0])
		 for j in range(len(x)):
		 	o.append([0,'',0])
		 m.append(o)
	return m

def file_reader(input):
	infile = open(input,'r')
	lines = infile.readlines()
	infile.close()
	return lines


def edit_distance(x):
	x = x.strip('\n')
	return x
	


def main():
	
	lines = file_reader('input3.txt')
	x = edit_distance(lines[1])
	y = edit_distance(lines[3])
	#x = "electrical engineering"
	#y = "computer science"
	#x = "C is a relatively \"low level\" language."
	#y = "Java is an object-oriented language."
	matrix = build_matrix(x,y)
	matrix = editdistance(matrix,x,y)
	pathprint(x,y,matrix)

main()