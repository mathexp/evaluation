PROBLEM = "10 6-sided dice are rolled. What is the probability that exactly three of the dice show a 1? Express your answer as a decimal rounded to the nearest thousandth."
SOLUTION = 0.155

def solve():
  from itertools import combinations
  p_three_dice_show_one = len(list(combinations(range(10), 3)))
  p_3_dice_match = (1. / 6)**3
  p_other_dice_dont_match = (1 - (1. / 6))**(10 - 3)
  p_any_one_outcome = p_3_dice_match * p_other_dice_dont_match
  return round(p_any_one_outcome * p_three_dice_show_one, 3)

def probability_three_dice_show_one(number_of_dice: int, number_of_sides: int):
  """
  Given number_of_dice dice, each with number_of_sides sides, returns the
  probability that exactly three of the dice show a 1, rounded to the nearest
  thousandth.
  """
  from itertools import combinations
  
  # Compute n choose r for n = number of dice, r = 3 
  p_three_dice_show_one = len(list(combinations(range(number_of_dice), 3)))
  p_3_dice_match = (1. / number_of_sides)**3
  p_other_dice_dont_match = (1 - (1. / number_of_sides))**(number_of_dice - 3)
  p_any_one_outcome = p_3_dice_match * p_other_dice_dont_match
  return round(p_any_one_outcome * p_three_dice_show_one, 3)

def problem(number_of_dice: int, number_of_sides: int):
  return f"{number_of_dice} {number_of_sides}-sided dice are rolled. What is the probability that exactly three of the dice show a 1? Express your answer as a decimal rounded to the nearest thousandth."

def test():
  assert problem(10, 6) == PROBLEM
  assert solve() == SOLUTION
  assert probability_three_dice_show_one(10, 6) == SOLUTION
  # Additional examples
  assert probability_three_dice_show_one(15, 4) == 0.225
  assert probability_three_dice_show_one(4, 9) == 0.005
  assert probability_three_dice_show_one(5, 5) == 0.051

test()
