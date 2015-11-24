def createRotationMatrix(matrix, startRow, startColumn, endRow, endColumn):
    for x in range(startColumn, endColumn + 1):
        matrix[startRow][x] = 'LE'
        matrix[endRow][x] = 'RI'
    for x in range(startRow, endRow + 1):
        if x != endRow:
            matrix[x][startColumn] = 'DO'
        if x != startRow:
            matrix[x][endColumn] = 'UP'
    startRow += 1
    endRow -= 1
    startColumn += 1
    endColumn -= 1
    if startColumn >= endColumn or startRow >= endRow:
        return matrix
    else:
        return createRotationMatrix(matrix, startRow, startColumn, endRow, endColumn)


def createSizeMatrix(matrix, startRow, startColumn, endRow, endColumn):
    count = (endRow - startRow) * 2 + (endColumn - startColumn) * 2
    for x in range(startColumn, endColumn + 1):
        matrix[startRow][x] = count
        matrix[endRow][x] = count
    for x in range(startRow + 1, endRow):
        matrix[x][startColumn] = count
        matrix[x][endColumn] = count
    startRow += 1
    endRow -= 1
    startColumn += 1
    endColumn -= 1
    if startColumn >= endColumn or startRow >= endRow:
        return matrix
    else:
        return createSizeMatrix(matrix, startRow, startColumn, endRow, endColumn)


def findOptimum(mark, rotationMatrix, row, column, num):
    number = 1
    if mark == 'UP':
        currentRow = row - number
        while currentRow > 0 and rotationMatrix[currentRow][column] == mark and num >= number:
            number *= 2
            currentRow = row - number
        return max(1, number // 2)
    if mark == 'DO':
        currentRow = row + number
        while currentRow < len(rotationMatrix) and rotationMatrix[currentRow][column] == mark and num >= number:
            number *= 2
            currentRow = row + number
        return max(1, number // 2)
    if mark == 'RI':
        currentColumn = column + number
        while currentColumn < len(rotationMatrix[0]) and rotationMatrix[row][currentColumn] == mark and num >= number:
            number *= 2
            currentColumn = column + number
        return max(1, number // 2)
    if mark == 'LE':
        currentColumn = column - number
        while currentColumn > 0 and rotationMatrix[row][currentColumn] == mark and num >= number:
            number *= 2
            currentColumn = column - number
        return max(1, number // 2)


def rotateCell(value, rotationMatrix, outPutMatrix, row, column, number, previous=False):
    if number == 0:
        outPutMatrix[row][column] = value
        return
    mark = rotationMatrix[row][column]
    if mark == 'UP':
        move = (len(rotationMatrix) - 2 * (len(rotationMatrix) - row - 1)) - 1
        if previous and mark != previous and number >= move:
            # print('row: %s column: %s mark: %s move: %s ' %(row,column,mark, move))
            rotateCell(value, rotationMatrix, outPutMatrix, row - move, column, number - move, mark)
        else:
            optimum = findOptimum(mark, rotationMatrix, row, column, number)
            rotateCell(value, rotationMatrix, outPutMatrix, row - optimum, column, number - optimum, mark)
        return
    if mark == 'DO':
        move = (len(rotationMatrix) - 2 * (row)) - 1
        if previous and mark != previous and number >= move:
            # print('row: %s column: %s mark: %s move: %s ' %(row,column,mark, move))
            rotateCell(value, rotationMatrix, outPutMatrix, row + move, column, number - move, mark)
        else:
            optimum = findOptimum(mark, rotationMatrix, row, column, number)
            rotateCell(value, rotationMatrix, outPutMatrix, row + optimum, column, number - optimum, mark)
        return
    if mark == 'RI':
        move = (len(rotationMatrix[0]) - 2 * (column)) - 1
        if previous and mark != previous and number >= move:
            # print('row: %s column: %s mark: %s move: %s ' %(row,column,mark, move))
            rotateCell(value, rotationMatrix, outPutMatrix, row, column + move, number - move, mark)
        else:
            optimum = findOptimum(mark, rotationMatrix, row, column, number)
            rotateCell(value, rotationMatrix, outPutMatrix, row, column + optimum, number - optimum, mark)
        return
    else:
        move = (len(rotationMatrix[0]) - 2 * (len(rotationMatrix[0]) - column - 1)) - 1
        if previous and mark != previous and number >= move:
            # print('row: %s column: %s mark: %s move: %s ' %(row,column,mark, move))
            rotateCell(value, rotationMatrix, outPutMatrix, row, column - move, number - move, mark)
        else:
            optimum = findOptimum(mark, rotationMatrix, row, column, number)
            rotateCell(value, rotationMatrix, outPutMatrix, row, column - optimum, number - optimum, mark)
        return


def rotateMatrix(matrix, rows, columns, number):
    rotationMatrix = createRotationMatrix(createMatrix(rows, columns), 0, 0, rows - 1, columns - 1)
    sizeMatrix = createSizeMatrix(createMatrix(rows, columns), 0, 0, rows - 1, columns - 1)
    result = createMatrix(rows, columns)
    for x in range(rows):
        for y in range(columns):
            remainder = number % sizeMatrix[x][y]
            rotateCell(matrix[x][y], rotationMatrix, result, x, y, remainder)
    return result


def printMatrix(matrix):
    try:
        for row in matrix:
            print(' '.join(row))
    except TypeError:
        for row in matrix:
            print(' '.join([str(x) for x in row]))


def createMatrix(rows, columns):
    result = []
    for _ in range(rows):
        result.append(['em'] * columns)
    return result


def createAndRotate(rows, columns, number):
    m = createMatrix(rows, columns)
    m = createRotationMatrix(m, 0, 0, rows - 1, columns - 1)
    m = rotateMatrix(m, rows, columns, number)
    printMatrix(m)


cr = createAndRotate

# M, N, R = [int(x) for x in input().split(' ')]
# matrix = []
# for _ in range(M):
#     matrix.append([int(x) for x in input().split(' ')])

# result = rotateMatrix(matrix, M, N, R)
# printMatrix(result)
