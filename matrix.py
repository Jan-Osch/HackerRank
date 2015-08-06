

def createRotationMarks(matrix, startRow, startColumn, endRow, endColumn):
	#place left in upper row:
	for x in range(startColumn, endColumn+1):
		matrix[startRow][x]='LE'
		matrix[endRow][x]='RI'
	for x in range(startRow, endRow+1):
		if x!=endRow:
			matrix[x][startColumn]='DO'
		if x!=startRow:
			matrix[x][endColumn]='UP'
	startRow+=1
	endRow-=1
	startColumn+=1
	endColumn-=1
	if startColumn>=endColumn or startRow>=endRow:
		return matrix
	else:
		return createRotationMarks(matrix,startRow,startColumn, endRow, endColumn)


def printMatrix(matrix):
	for row in matrix:
		print(" ".join(row))

def createMatrix(rows, columns):
	result = []
	for _ in range(rows):
		result.append(['em']*columns)
	return result
