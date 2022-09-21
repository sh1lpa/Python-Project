#-----------------------------------------------------------------------------------------------------------------
'''
Sample Input 

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''


from turtle import width


def wrap(string, max_width):
    # l=[]
    start = 0
    end = max_width
    for i in range(round(len(string)/max_width)+1):
        num  = (max_width * (round(len(string)/max_width)))
        # print(round(len(string)/max_width), i,len(string),num,start)
        if start == num:
            result = string[start:]
            # l.append(result)      # uncomment this for hacker rank challenge format
        else:
            result = string[start:end]
            # l.append(result)       # uncomment this for hacker rank challenge format
            start = end
            end = end + max_width
        # return '\n'.join(l)     # uncomment this for hacker rank challenge format
        yield result     # comment this fror hackerrank challenge
            
if __name__ == '__main__':
    string = input('Enter String :')
    max_width = int(input('enter width :'))
    [print(value) for value in wrap(string, max_width)]
    # print(result)    # uncomment this for hacker rank challenge format