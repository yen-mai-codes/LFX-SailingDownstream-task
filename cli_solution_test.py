"""
Simple test module for the CLI solution.   
"""

import unittest
import os
import random
import string
import cli_solution

class TestCliSolution(unittest.TestCase):
   """Test class for the CLI solution."""
      
   def invalidListGenerator(self, type: str) -> list:
      """Generates a list of floats or characters with correct list length."""
      length = 10
      lst = ['-l']

      while length > 0:
         if type == 'float':
            item = str(random.random())
         else:
            item = random.choice(string.ascii_letters + string.punctuation)

         lst.append(item)
         length -= 1
      return lst  

   def listOfInvalidLengthGenerator(self) -> list:
      """Generate an invalid list with length that is not a multiple of 10."""
      generated = False
   
      # generates a length not divisible by 10
      while not generated:
         length = random.randrange(100) 
         if (length % 10 != 0):
            generated = True
      lst = ['-l']

      for i in range(length):
         lst.append(str(i))
      return lst
   
   def test_entry_point(self) -> None:
      """Runs the cli_solution.py file."""
      exit_status = os.system('python cli_solution.py -h')
      self.assertEqual(exit_status, 0)

   def test_parse_args(self) -> None:
      """Check if parse_args accepts valid lists only."""
      with self.assertRaises(SystemExit):
         float_lst = self.invalidListGenerator('float')
         cli_solution.parse_args(float_lst)

      with self.assertRaises(SystemExit):
         character_lst = self.invalidListGenerator('character')
         cli_solution.parse_args(character_lst)

      with self.assertRaises(SystemExit):
         invalid_length_lst = self.listOfInvalidLengthGenerator()
         cli_solution.parse_args(invalid_length_lst)

   def test_process_list(self) -> None:
      """Check if process_list removed the correct numbers."""
      length = 10*random.randrange(10)
      lst = []

      for i in range(length):
         lst.append(i)

      new_lst = cli_solution.process_list(lst)

      for i in new_lst:
         self.assertFalse(i % 2 == 0)            
         self.assertFalse(i % 3 == 0)            

if __name__ == "__main__":
    unittest.main()
