import argparse
parser = argparse.ArgumentParser(description='Process a list of integers, with the items at positions which are multiple of 2 or 3 removed. Emits error if the list is not a multiple of 10 in length.')
parser.add_argument("-l", "--list", type=int, help="a list of integers. It should be a multiple of 10 in length.", nargs='+')
args = parser.parse_args()

lst = args.list

if (len(lst) % 10 != 0): 
   raise parser.error("The list must be a multiple of 10 in length")


lst_len = len(lst)
new_lst = []

for i in range(lst_len):
   if (i % 2 != 0) and (i % 3 != 0):
      new_lst.append(lst[i])

print('The input list: ', lst)
print('The output list: ', new_lst)



 