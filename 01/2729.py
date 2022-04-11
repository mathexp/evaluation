PROBLEM = "What is $11111111_2+111111_2$? Write your answer in base $10$."
SOLUTION = 318

def sum_two_binary_numbers_to_base_ten(summand_1, summand_2):
  """
  Returns the sum of two binary numbers, summand1 and summand2, in base 10
  """
  return int(summand_1, 2) + int(summand_2, 2)


def problem(summand_1, summand_2):
  return f"What is ${summand_1}_2+{summand_2}_2$? Write your answer in base $10$."
  

def test():
  assert problem("11111111", "111111") == PROBLEM
  assert sum_two_binary_numbers_to_base_ten("11111111", "111111") == SOLUTION
