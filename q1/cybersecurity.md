# Part A - Cybersecurity Threat Analysis
## Chosen Case: Case 2 - Fake Prize

### 1. What threat is present?
| The threat present is a phishing which includes a dangerous individual asking for your personal and payment information.

### 2. What clues make it suspicious?
| One clue making it suspicious is abruptly asking for personal information without any explanation.

### 3. What data, device, account, application or financial information could be affected?
| The attacker may use the stolen information to do horrible things such as unauthorized transactions and blackmailing.

### 4. What should the user do?
| The user should not give the user any information and avoid interacting with them. They should  immediately block and report the sender.

### 5. What mitigation can reduce the risk?
| Cybersecurity awareness is one of the best ways to reduce the risk as it provides the necessary knowledge to determine if something is  a scam or "too good to be true."

# Part B - Data Privacy and Secure Data Capture
Student Name - **COLLECT**: This is required to identify which specific student is registering for the club activity.

Section - **COLLECT**:  This is necessary to ensure the student belongs to an approved class.

Club Choice - **COLLECT**: This determines the student's preference for the specific club they wish to join.

School Email - **COLLECT**:  This serves as the official communication channel for sending club updates.

Attendance Status - **COLLECT**:  This tracks the student's presence during the registration or initial meeting period.

Password - **DO NOT COLLECT**: Storing or asking for account passwords introduces a severe security risk.

OTP - **DO NOT COLLECT**: OTPs are short-lived security codes used exclusively for identity verification.

Home Address - **DO NOT COLLECT**: Collecting physical addresses violates the principle of data minimization since a student's home location is irrelevant to running a school club.

Parent Bank Account - **DO NOT COLLECT**: Financial details are highly sensitive and completely unrelated to a free school club activity, creating a major data breach risk if gathered.

# Part C - Validation Rules

| Data Captured | Expected Input | Possible Risk | Invalid Input | Validation Rule | Error Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Student Name** | Text that is not blank | Leaves the name empty in the list | `""` (blank) | Cannot be empty | Student name is required. |
| **Section** | A real section name from the list (like Dahlia) | Typing a section that does not exist | `"Rose"` | Must be in the allowed sections list | Invalid Section. |
| **Club Choice** | Robotics, Science, Mathematics, or Programming | Choosing a club the school does not offer | `"Gaming"` | Must match one of the 4 choice options | Please choose a valid club. |
| **Student Email** | An email with symbols | Entering a broken email that will not work | `"studentpshs"` | Must have both an `@` and a `.` inside it | Invalid email. |
| **Attendance Status** | Present, Absent, or Late | Writing an unapproved status | `"Sick"` | Must be exactly Present, Absent, or Late | Invalid attendance status. |

# Part D - Secure Program Implementation
### [Secure Registration Python Code](q1/secure_registration.py)

# Part E - Security Testing and Reflection
### Part E - Security Testing and Reflection

| Test | Input Situation | Expected Result | Actual Output | PASS / FAIL |
| :--- | :--- | :--- | :--- | :--- |
| 1 | All fields valid | Registration accepted | Shows the full "REGISTRATION ACCEPTED" block with all user details | PASS |
| 2 | Blank name | Rejected | Prints "Student name is required." and stops the program | PASS |
| 3 | Invalid section | Rejected | Prints "Invalid Section." and stops the program | PASS |
| 4 | Invalid club | Rejected | Prints "Please choose a valid club." and stops the program | PASS |
| 5 | Email missing @ | Rejected | Prints "Invalid email." and stops the program | PASS |
| 6 | Email missing . | Rejected | Prints "Invalid email." and stops the program | PASS |
| 7 | Invalid attendance status | Rejected | Prints "Invalid attendance status." and stops the program | PASS |
| 8 | Valid alternative values | Accepted | Shows the full "REGISTRATION ACCEPTED" block with alternative list items | PASS |

# Reflection
# Reflection

# Reflection

### 1. What is one cybersecurity threat that can affect an application or user?
A big threat is **phishing**, where scammers send fake messages—like fake account warnings or fake prizes—to trick people into giving away important things like passwords, personal details, or money.

### 2. How can users reduce the risk of phishing or suspicious messages?
People can stay safe by never clicking on links in unexpected messages, double-checking who actually sent the message, using extra login protection like two-factor authentication, and checking with official sources to see if a claim is real.

### 3. How can validation rules improve the security of user input?
Validation rules act like a gatekeeper for data by checking it before the program accepts it, which stops broken information, blank fields, or harmful text from messing up the system or crashing the program.

### 4. Why should a program avoid collecting unnecessary personal information?
Following the rule of **data minimization** means you only ask for what you actually need; by not gathering extra details like home addresses or banking info, there is less personal data lying around for hackers to steal if the system ever gets breached.

### 5. How did SG7's input validation concepts become security practices in SG8?
In **Study Guide 7**, we used input validation rules simply to keep data neat, complete, and free of normal coding errors; in **Study Guide 8**, those exact same rules became defensive tools to actively protect user privacy and block people from entering bad data on purpose.
