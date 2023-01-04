# l = [i for i in range(5)]

# g = (i for i in range(5))


# print(l.__sizeof__())

# print(g.__sizeof__())
# import timeit
# print(timeit.timeit('''input_list = range(100)

# def div_by_five(num):
#     return True if num % 5 ==0 else False

# xyz = (i for i in input_list if div_by_five(i))

# for i in xyz:
#     x = i
# ''',number=100000))


corrent_combo = (3,6,2)

'''
Using the list conprehension '''
# found_combo = False
# for c1 in range(10):
#     if not found_combo:

#         for c2 in range(10):
#             if not found_combo:
#                  for c3 in range(10):
#                     if (c1,c2,c3) == corrent_combo:
#                         print(f'Found the correct combo {corrent_combo}')
#                         found_combo = True
#                         break
#                     print(c1,c2,c3)

'''
Using the generator function'''
def get_combo():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1,c2,c3)

for i in get_combo():
    if i == corrent_combo:
        print(f'Found the correct combo {corrent_combo}')
        break
    print(i)
