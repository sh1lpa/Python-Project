#-----------------------------------------------------------------------------------------------------------------
'''
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

'''



def main():
    s = input("Enter the word :")
    funcs = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    [print( any(fun(l) for l in s)) for fun in funcs]


if __name__ == '__main__':
    main()
    