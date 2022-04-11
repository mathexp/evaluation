PROBLEM = "10 6-sided dice are rolled. What is the probability that exactly three of the dice show a 1? Express your answer as a decimal rounded to the nearest thousandth."
SOLUTION = 0.155

def probability_three_dice_show_one(number_of_dice, number_of_sides):
  """
  Given number_of_dice dice, each with number_of_sides sides, returns the
  probability that exactly three of the dice show a 1, rounded to the nearest
  thousandth.
  """
  from itertools import combinations

  probability_three_dice_show_one = len(list(combinations(range(number_of_dice), 3)))
  probability_of_any_one_outcome = (1. / number_of_sides)**3 * (1 - (1. / number_of_sides))**(number_of_dice - 3)
  return round(probability_of_any_one_outcome * probability_three_dice_show_one, 3)

def problem(number_of_dice, number_of_sides):
  return f"{number_of_dice} {number_of_sides}-sided dice are rolled. What is the probability that exactly three of the dice show a 1? Express your answer as a decimal rounded to the nearest thousandth."

def test():
  assert problem(10, 6) == PROBLEM
  assert probability_three_dice_show_one(10, 6) == SOLUTION

test()
