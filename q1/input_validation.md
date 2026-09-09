# Part A - Validation Requirements

| Field | Expected Input | Validation Type | Rule | Invalid Example | Error Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Student Name** | String | Presence | Cannot be empty / left blank | `""` (Just pressing Enter) | "Student name is required." |
| **2. Age** | Integer | Data Type + Range | Must be a whole number from 11 to 18 | `10` or `"sixteen"` | "Age must be from 11 to 18." / "Age must be a number." |
| **3. Grade Level** | Integer | Range / Acceptable Value | Must be a whole number from 7 to 12 | `6` or `13` | "Invalid grade level." |
| **4. Email** | String | Simple Pattern | Must contain both "@" and "." characters | `"student[at]email.com"` | "Invalid email." |
| **5. Registration Code** | String | Length | Must be exactly 6 characters long | `"12345"` (5 characters) | "The registration code must contain exactly 6 characters." |

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
## Python Code: [Workshop Validator Python Code](q1/workshop_validator.py)

# Part D - Testing
