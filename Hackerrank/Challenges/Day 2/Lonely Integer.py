from collections import Counter


def get_key(my_dict):
    for key, value in my_dict.items():
        # print(key,value)
        if value == 1:
            return key
 
    return "key doesn't exist"

def lonely_integer(a):
    return get_key(Counter(a))
    

def main():
    arr = [1,2,3,4,3,2,1]
    print(lonely_integer(arr))


if __name__ == '__main__':
    main()