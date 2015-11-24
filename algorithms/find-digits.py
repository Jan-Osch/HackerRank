def getDigits(number):
    stringified = str(number)
    return len([int(stringified[i]) for i in range(len(stringified)) if
                stringified[i] != '0' and number % int(stringified[i]) == 0])


def getConcatenatedLength(text):
    words = text.split(' ')
    return ''.join([str(len(word)) for word in words])


from math import sqrt, ceil, floor


def computeNumberOfSquareIntegers(a, b):
    down = ceil(sqrt(a))
    up = floor(sqrt(b))
    return up - down + 1


def findOccurances(row, pattern):
    result = []
    start = 0
    position = row.find(pattern, start)
    while position >= 0:
        result.append(position)
        start = position + 1
        position = row.find(pattern, start)
    return set(result)


def parseMatrix(matrixSize, pattern, patternSize):
    result = True
    indexMatrix = 0
    index = 0
    current = False
    previous = False
    skip = False
    while indexMatrix < matrixSize:
        row = input()

        if not skip:
            current = findOccurances(row, pattern[index])

            if previous:
                previous = current.intersection(previous)
                if len(previous) > 0:
                    index += 1
                    if index == patternSize:
                        skip = True
                else:
                    index = 0
                    previous = False
                    if matrixSize - (indexMatrix + 2) < patternSize:
                        skip = True
                        result = False
            elif len(current) > 0:
                previous = current
                index += 1
                if index == patternSize:
                    skip = True
        indexMatrix += 1
    return result
