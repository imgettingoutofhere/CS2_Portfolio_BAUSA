# 1. Student Name - Presence Validation

sname = str(input("Please enter your name: "))
if not sname:
  print("Student name is required.")
  raise SystemExit

# 2. Age - Data Type + Range Validation

try:
  age = int(input("Please enter your age: "))
  if age < 11 or age > 18:
    print("Age must be from 11 to 18.")
    raise SystemExit
    
except ValueError:
    print("Age must be a number.")
    raise SystemExit

# 3. Grade Level - Acceptable Value Validation
try:
  glevel = int(input("Please input your grade level: "))
  if glevel < 7 or glevel > 12:
    print ("Invalid grade level.")
    raise SystemExit

except ValueError:
  print("Invalid grade level.")
  raise SystemExit

# 4. Email - Simple Pattern Validation
try:
 email = str(input("Please input your email: "))
 if "@" not in email and "." not in email:
    print ("Invalid email.")
    raise SystemExit

except ValueError:
  print("Invalid email.")
  raise SystemExit

# 5. Registration Code - Length Validation
try:
  rcode = str(input("Please enter your registration code: "))
  if len(rcode) != 6:
    print("The registration code must contain exactly 6 characters.")
    raise SystemExit
    
except ValueError:
  print("The registration code must contain exactly 6 characters.")
  raise SystemExit

print ("---------------------")
print ("REGISTRATION COMPLETE")
print ("---------------------")
print("Name: ",sname)
print("Age: ",age)
print("Grade level: ",glevel)
print("Email: ",email)
print("Registration code: ",rcode)

