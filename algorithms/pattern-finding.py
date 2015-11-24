def findOccurances(row, pattern):
    result = []
    start = 0
    position = row.find(pattern, start)
    while position >= 0 :
        result.append(position)
        start = position+1
        position = row.find(pattern, start)
    return set(result)

def containsPattern(matrix, matrixSize, pattern, patternSize):
    result = False
    indexMatrix = 0
    index = 0
    current = False
    previous = False
    while indexMatrix < matrixSize:
        row = matrix[indexMatrix]

        if not result:
            current = findOccurances(row, pattern[index])

            if previous:
                previous = current.intersection(previous)
                if len(previous) > 0:
                    index +=1
                    if index == patternSize:
                        result = True
                else:
                    index = 0
                    previous = False
                    if matrixSize - (indexMatrix+2) < patternSize:
                        result = False
            elif len(current) > 0:
                previous = current
                index +=1

        indexMatrix +=1
    return result


matrix = ['400453592126560',
'114213133098692',
'474386082879648',
'522356951189169',
'887109450487496',
'252802633388782',
'502771484966748',
'075975207693780',
'511799789562806',
'404007454272504',
'549043809916080',
'962410809534811',
'445893523733475',
'768705303214174',
'650629270887160']

pattern = ['99', '99']

print (containsPattern(matrix, 15, pattern, 2))