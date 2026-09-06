# Part 1 - Analyze the Logic

## What information does the program need?
> The program needs a student's score as an input

## What is the minimum valid score?
> Minimum: 0

## What is the maximum valid score?
> Maximum: 100

## What outcomes can the program producs?
> It can produce, Outstanding, Very Satisfactory, Satisfactory, Needs Improvement and Invalid Score.

## Which prt uses a boundary condition
> The program checks if the score is below 0 or above 100. If it is outside this range, the program displays "Invalid Score."

## Which part uses multiple decision parts?
> The program uses `if`, `elif`, and `else` statements to choose the correct classification based on the student's score. It checks the score from the highest classification to the lowest until the correct result is found.

# Part 2 - Create the Flowchart
## Link to flowchart: ![Score Checker Flowchart](score_checker_flowchart.png)

# Part 3 - Write the Pseudocode
START

INPUT score

IF score >= 90 AND score <= 100

→ DISPLAY "Outstanding"

ELSE IF score >= 80 AND score <= 89

→ DISPLAY "Very Satisfactory"

ELSE IF score >= 75 AND score <= 79

→ DISPLAY "Satisfactory"

ELSE IF score < 75

→ DISPLAY "Needs Improvement"

END

# Part 4 - Clean Code Implementation
## Link to python file: ![Score Checker Python Code](score_checker.py)

# Part 5 - Test the Program
| Test | Input | Purpose | Expected Output | Actual Output | Result |
|---|---:|---|---|---|---|
| 1 | -1 | Below minimum | Invalid Score | Invalid Score | PASS |
| 2 | 0 | Minimum boundary | Needs Improvement | Needs Improvement | PASS |
| 3 | 74 | Below satisfactory boundary | Needs Improvement | Needs Improvement | PASS |
| 4 | 75 | Satisfactory boundary | Satisfactory | Satisfactory | PASS |
| 5 | 80 | Very satisfactory boundary | Very Satisfactory | Very Satisfactory | PASS |
| 6 | 90 | Outstanding boundary | Outstanding | Outstanding | PASS |
| 7 | 100 | Maximum boundary | Outstanding | Outstanding | PASS |
| 8 | 101 | Above maximum | Invalid Score | Invalid Score | PASS |


# Testing Reflection
## Why is it important to test the values 0 and 100?
> Because 0 and 100 are the minimum and maximum valid scores. Anything below or above that is invalid.

## Why did you also test -1 and 101?
> To determine if the program properly identifies values outside of the range.

## Which test helped you understand boundary conditions the most?
> Testing 75, 80, and 90 helped me understand boundary conditions the most because these values are where the classifications change.

## What outcomes can the program producs?
> It can produce, Outstanding, Very Satisfactory, Satisfactory, Needs Improvement and Invalid Score.

## Did any of your tests initially fail? If yes, what did you change in your program?
> No, my tests did not initially fail. The program produced the expected results for all the test cases.

# Reflection
## How did selection structures make the program more useful?
> Selection structures allowed the program to make decisions and give the correct classification based on the student's score.

## How did proper comments and readable formatting improve your program?
> They made the code easier to understand, read, and check for mistakes.

## Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
> It helps organize the logic first and makes it easier to write the code correctly.
