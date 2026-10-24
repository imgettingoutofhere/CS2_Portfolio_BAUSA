score1 = float(input("Please enter your first score: "))
score2 = float(input("Please enter your second score: "))
score3 = float(input("Please enter your third score: "))
total = score1 + score2 + score3
average = total / 3
ctasks = int(input("Completed tasks: ")) 

def calculate_average(score1, score2, score3):
  return average

def get_performance(average):
  if average >= 85:
    return "Mastery"
  elif average >= 70:
    return "Developing"
  else:
    return "Needs review"

def is_eligible(average, ctasks):
  if average >= 85 and ctasks >= 3:
    return True
  else:
    return False

final_avg = calculate_average(score1, score2, score3)
category = get_performance(average)
eligible = is_eligible(average, ctasks) 

print("Average Score:", average)
print("Category:", category)
print("Eligible:", eligible)

# Docuentation Questions
# 1. The function calculate_average returns a number, the function get_performance returns a string, and the function is_eligible returns a boolean.
# 2. Data moves from one function to another by using a variable to catch the output of the first function, and then passing that variable as an argument into the next function.
# 3. If a student has a high average but has fewer than 3 tasks accomplished, they will not be eligible to join the practice challenge, as both values conditions need to be met in order to trigger a True boolean.
# 4. Using return is more appropriate because it gives your code flexibility and reusability. Print is a complete dead end, while return hands the data back.
