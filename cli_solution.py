"""
Simple CLI solution.
"""

import argparse
import sys

def parse_args(args: list) -> list:
   """
   Parses the arguments from command line. Throws error if it's not a list of integers, or its length is not a multitude of 10.

   Args:
      list: a list of items from command line.

   Returns:
      list: a list of integers.
   """
   parser = argparse.ArgumentParser(description='Process a list of integers, with the items at positions which are multiple of 2 or 3 removed. Emits error if the list is not a multiple of 10 in length.')
   parser.add_argument("-l", "--list", type=int, help="a list of integers. It should be a multiple of 10 in length.", nargs='+')

   # if run program with no flags nor arguments
   if not args:
      raise parser.error("Please add -l flag and follows with a list of integer.")
   
   namespace = parser.parse_args(args)
   lst = namespace.list

   # if input list is not multiple of 10
   if (len(lst) % 10 != 0): 
      raise parser.error("The list must be a multiple of 10 in length")
   return lst

def process_list(lst : list) -> list:
   """
   Return new list by removing items at positions which are a multiple of 2 or 3 in lst.

   Args:
      lst (list): a list of integers.

   Returns:
      list: the processed list.
   """
   
   lst_len = len(lst)
   new_lst = []

   # add to new_lst items at indices not divisible by 2 or 3
   for i in range(lst_len):
      if (i % 2 != 0) and (i % 3 != 0):
         new_lst.append(lst[i])
   return new_lst

def main() -> list: 
   lst = parse_args(sys.argv[1:])
   new_lst = process_list(lst)
   print('The input list is: ', lst)
   print('The processed list is: ', new_lst)
   return new_lst

if __name__=="__main__": 
    main() 

 