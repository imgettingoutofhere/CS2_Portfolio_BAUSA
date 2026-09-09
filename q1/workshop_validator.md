# Part A - Validation Requirements

| Field | Expected Input | Validation Type | Rule | Invalid Example | Error Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Student Name** | String | Presence | Cannot be empty / left blank | `""` (Just pressing Enter) | "Student name is required." |
| **2. Age** | Integer | Data Type + Range | Must be a whole number from 11 to 18 | `10` or `"sixteen"` | "Age must be from 11 to 18." / "Age must be a number." |
| **3. Grade Level** | Integer | Range / Acceptable Value | Must be a whole number from 7 to 12 | `6` or `13` | "Invalid grade level." |
| **4. Email** | String | Simple Pattern | Must contain both "@" and "." characters | `"student[at]email.com"` | "Invalid email." |
| **5. Registration Code** | String | Length | Must be exactly 6 characters long | `"12345"` (5 characters) | "The registration code must contain exactly 6 characters." |

# Part B - Program Design
