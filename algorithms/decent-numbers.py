def decentNumber(length):
    if length==0:
        return ''
    if length>=3:
        number = length//3
        while number >0:
            remainder = decentNumber(length-number*3)
            if remainder != '-1':
                return '555'*number+remainder
            number-=1            
    if length>=5:
        number = length//5
        while number >0:
            remainder = decentNumber(length-number*5)
            if remainder != '-1':
                return '33333'*number+remainder
            number-=1
    return '-1'


dn = decentNumber