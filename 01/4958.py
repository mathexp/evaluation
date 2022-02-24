def solve():
  """
  This function solves the following problem and returns the answer.
  Ten 6-sided dice are rolled. What is the probability that exactly three of the dice show a 1? Express your answer as a decimal rounded to the nearest thousandth.
  """
  from itertools import combinations

  number_of_sides = 6
  probability_three_dice_show_one = len(list(combinations(range(10), 3)))
  probability_of_any_one_outcome = (1. / number_of_sides)**3 * (1 - (1. / number_of_sides))**7
  return round(probability_of_any_one_outcome * probability_three_dice_show_one, 3)
