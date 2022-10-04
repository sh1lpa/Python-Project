import decimal


def plus_minus(arr) -> None:
    '''
        Function must not return anything
        arr = [1, 1, 0, -1, -1]
        There are  elements, two positive, two negative and one zero. 
        Their ratios are 2/5 = 0.400000, 2/5=0.400000 and 1/5 = 0.200000. 
        Results are printed as:

            0.400000
            0.400000
            0.200000

    '''
#---------------------------------start----------------------------------------------------------------------------------
    decimal.getcontext().prec = 6
    plus = 0
    minus = 0
    length = decimal.Decimal(len(arr))
    for i in arr:
        if i < 0:
            minus+=1
        elif i > 0:
            plus+=1
    print(f'{decimal.Decimal(plus)/length}\n{decimal.Decimal(minus/length)}\n{decimal.Decimal((length - (plus+minus)))/length}')

#-----------------------------------------------End --------------------------------------------------------------

def main():
    arr = [1, 1, 0, -1, -1]
    plus_minus(arr)

if __name__ == '__main__':
    main()