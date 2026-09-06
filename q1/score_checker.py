# Ask the user to enter a score

score = int(input("Enter the score of the student: "))

# Check whether the score is in the range of 0 - 100

if score < 0 or score > 100:
  print("Invalid score.")

# If the score is valid, classify it among the required performance ranges.

elif score >= 90:
  print("Outstanding")
elif score >= 80:
  print("Very Satisfactory")
elif score >= 75:
  print("Satisfactory")
else:
  print("Needs Improvement")
