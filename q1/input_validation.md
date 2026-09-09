# Part A - Validation Requirements

| Field | Expected Input | Validation Type | Rule | Invalid Example | Error Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Student Name** | String | Presence | Cannot be empty / left blank | "" (Just pressing enter) | "Student name is required." |
| **2. Age** | Integer | Data Type + Range | Must be a whole number from 11 to 18 | 10 or "sixteen" | "Age must be from 11 to 18." / "Age must be a number." |
| **3. Grade Level** | Integer | Range / Acceptable Value | Must be a whole number from 7 to 12 | 6 or 13 | "Invalid grade level." |
| **4. Email** | String | Simple Pattern | Must contain both "@" and "." characters | "student[at]email.com" | "Invalid email." |
| **5. Registration Code** | String | Length | Must be exactly 6 characters long | "12345" (5 characters) | "The registration code must contain exactly 6 characters." |

## Validation Questions
### 1. Why should the student name not be blank?
> Because the system would recognize it as an error and immediately display the error message and end the program.

### 2. Why should age be checked for both data type and range?
> To determine what value is needed and to set a limit for how old you must be to be registered, in this situation being between 11 and 18 years old.

### 3. Why should grade level only accept specific values?
> So that it is easier for the user to understand what is needed and give the correct value.

### 4. What format requirements did you use for the email address?
> The format requirements I set that is needed for the email address is that it has to have a dot(.) and the at symbol(@)

### 5. What length requirement did you use for the registration code?
> I set the length requirement to 6 characters, no more and no less.

# Part B - Program Design
 
 START
 
    # 1. Student Name Validation
    OUTPUT "Please enter your name: "
    INPUT sname
    IF sname == "" THEN
        OUTPUT "Student name is required."
        EXIT PROGRAM
    END IF
    
    # 2. Age Validation
    OUTPUT "Please enter your age: "
    INPUT age
    IF age IS NOT A NUMBER THEN
        OUTPUT "Age must be a number."
        EXIT PROGRAM
    ELSE IF age < 11 OR age > 18 THEN
        OUTPUT "Age must be from 11 to 18."
        EXIT PROGRAM
    END IF

    # 3. Grade Level Validation
    OUTPUT "Please input your grade level: "
    INPUT glevel
    IF glevel IS NOT A NUMBER OR glevel < 7 OR glevel > 12 THEN
        OUTPUT "Invalid grade level."
        EXIT PROGRAM
    END IF

    # 4. Email Validation (Using corrected logic)
    OUTPUT "Please input your email: "
    INPUT email
    IF email DOES NOT CONTAIN "@" OR email DOES NOT CONTAIN "." THEN
        OUTPUT "Invalid email."
        EXIT PROGRAM
    END IF

    # 5. Registration Code Validation
    OUTPUT "Please enter your registration code: "
    INPUT rcode
    IF LENGTH(rcode) != 6 THEN
        OUTPUT "The registration code must contain exactly 6 characters."
        EXIT PROGRAM
    END IF

    // Display Registration Summary
    OUTPUT "---------------------"
    OUTPUT "REGISTRATION COMPLETE"
    OUTPUT "---------------------"
    OUTPUT "Name: " + sname
    OUTPUT "Age: " + age
    OUTPUT "Grade level: " + glevel
    OUTPUT "Email: " + email
    OUTPUT "Registration code: " + rcode
END

# Part C - Program Implementation
## Python Code: [Workshop Validator Python Code](workshop_validator.py)

# Part D - Testing

| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| **1** | All inputs valid | Normal case | Full registration details printed successfully. | Full registration details printed successfully. | **PASS** |
| **2** | Blank student name | Presence | "Student name is required." | "Student name is required." | **PASS** |
| **3** | Age = fourteen | Data type | "Age must be a number." | "Age must be a number." | **PASS** |
| **4** | Age = 11 | Minimum boundary | No error; moves to Grade Level prompt. | No error; moves to Grade Level prompt. | **PASS** |
| **5** | Age = 18 | Maximum boundary | No error; moves to Grade Level prompt. | No error; moves to Grade Level prompt. | **PASS** |
| **6** | Age = 10 | Range | "Age must be from 11 to 18." | "Age must be from 11 to 18."` | **PASS** |
| **7** | Grade Level = 13 | Acceptable value | "Invalid grade level." | "Invalid grade level." | **PASS** |
| **8** | Email = studentpshs.edu.ph | Pattern *(Missing @)* | "Invalid email." | "Invalid email." | **PASS** |
| **9** | Registration Code = ABC | Length *(Too short)* | "The registration code must contain exactly 6 characters." | "The registration code must contain exactly 6 characters." | **PASS** |
| **10** | Registration Code = CS2026 | Valid length | Full registration details printed successfully. | Full registration details printed successfully. | **PASS** |

# Part E - Output Verification
## Verification Test 1
*Input*:
Please enter your name: 

*Expected Output:*
Student name is required.

*Actual Output:*
Student name is required.

*Result:* PASS

*Explanation:*
> The input was left blank. The presence validation successfully detected the empty value of string, printed the required error message, and ended the program as expected.

## Verification Test 2
*Input:*
Please enter your name: Jo
Please enter your age: fourteen

*Expected Output:*
Age must be a number.

*Actual Output:*
Age must be a number.

*Results:* PASS

*Explanation:*
> The user entered a string value instead of an integer value for the age. The data type validation caught the ValueError exception, displayed the correct error message, and ended the program.

## Verification Test 3
*Input:*
Please enter your name: Jo
Please enter your age: 15
Please input your grade level: 10
Please input your email: studentpshs.edu.ph

*Expected Output:*
Invalid email.

*Actual Output:*
Invalid email.

*Result:* PASS

*Explanation:*
> The user entered an email string that lacks the `@` character symbol requirement. The pattern boundary check correctly flagged this format as invalid.

# Reflection
## 1. Why should a program validate input before processing it?
> Validating input prevents the program from crashing or breaking due to unexpected user entries. It also ensures that the system only processes clean, accurate data.

## 2. What is the difference between input validation and output verification?
> Input validation checks if the user's data is correct and safe before the program accepts it. Output verification checks the final results after processing to ensure the program produced the right answer.

## 3. Which validation technique was easiest for you to implement? Why?
> Presence validation for the student name was the easiest to implement. It only requires a simple check to see if the input string is empty or blank.

## 4. Which validation technique was most challenging? Why?
> Email pattern validation was the most challenging because checking for specific characters like @ and . requires a more complex logical condition. A small logic mistake can easily let invalid email formats slip through undetected.

## 5. How did testing invalid inputs help you improve your program?
> Testing invalid inputs helped reveal a logical bug in the original email validation code that let bad data pass through. Finding this flaw allowed the logic to be corrected so the program handles errors properly.
