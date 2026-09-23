# 1. Student Name

sname = str(input("Please enter your name: "))
if not sname:
  print("Student name is required.")
  raise SystemExit

# 2. Section

sec = str(input("Please enter your section: "))
valid_sections = ["Diamond", "Emerald", "Jade", "Sapphire", "Dahlia", "Ilang-Ilang", "Rosal", "Sampaguita", "Beryllium", "Magnesium", "Platinum", "Silicon", "Electron", "Gluon", "Graviton", "Photon", "Biology", "Chemistry", "Physics", "Bio-Chemistry"]
if sec not in valid_sections:
  print("Invalid Section.")
  raise SystemExit

# 3. Club Choice

clubc = str(input("Please enter your club choice: "))
valid_clubc = ["Robotics", "Science", "Mathematics", "Programming"]
if clubc not in valid_clubc:
  print("Please choose a valid club.")
  raise SystemExit

# 4. Student Email

email = str(input("Please input your student email: "))
if "." not in email or "@" not in email:
  print("Invalid email.")
  raise SystemExit

  # 5. Attendance Status
  
astatus = str(input("Please input your attendance status: "))
valid_astatus = ["Present", "Absent", "Late"]
if astatus not in valid_astatus:
  print("Invalid attendance status.")
  raise SystemExit

print("----------------------")
print("REGISTRATION ACCEPTED")
print("----------------------")
print("Student:", sname)
print("Section:", sec)
print("Club:", clubc)
print("Email:", email)
print("Attendance:", astatus)
