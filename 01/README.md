# Math problem translation task


## Overview

The file `evaluation.json` contains 6 word problems. Each word problem has the following sections:
 - index: identifier for the example
 - problem: problem statement
 - solution: solution to the problem

The first 2 word problems have corresponding `.py` files as examples for you to follow. These are `2729.py` and `4958.py`.

## Your task

Your task is to create python files that correspond to the other four problems in `evaluation.json`. Each file must have the following:
 - `PROBLEM` and `SOLUTION` specified at the top of the file
 - `solve` function that directly solves the problem
 -  a generalized function with a semantic name that solves a broader version of the problem by accepting arguments
 -  `problem` function, which generates a string that represents the problem
 -  `test` function, which tests for the correctness of the other functions and must be called at the bottom of the file.

## Specifications
 - Each python file should match the format of the provided files as closely as possible.
 - You are encouraged to use libraries such as `math`, `sympy` and `itertools` and other useful common python libraries.
 - Try to make your python files as pedagogical as possible. Please include descriptive docstrings and comments.
 - Submit your files via email. **DO NOT open a pull request.**
