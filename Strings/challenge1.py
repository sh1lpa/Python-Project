
#-----------------------------------------------------------------------------------------------------------------
'''
Output the integer number indicating the total number of occurrences of the substring in the original string.

Input (stdin)

ABCDCDC
CDC

Expected Output
2
'''

def count_substring(sentence, sub_string):
    count = 0
    for index, letter in enumerate(range(len(sentence) - len(sub_string)+1)):
        print(sentence[index:index+len(sub_string)]+' '+sub_string)
        print(sentence[index:index+len(sub_string)] == sub_string)
        if sentence[index:index+len(sub_string)] == sub_string:
            count +=1
    return count

    # return 0 if sentence.find(sub_string) == -1 else sentence.find(sub_string)



def main():
    sentence = 'abcdcdc'
    sub = 'cdc'
    print(count_substring(sentence,sub))


if __name__ == '__main__':
    main()



#-----------------------------------------------------------------------------------------------------------------
''''''





#-----------------------------------------------------------------------------------------------------------------