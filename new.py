# mock_coding_assessment.py

"""
Mock Coding Assessment
Duration: 90 Minutes

Learning Outcomes Assessed:
1. Understanding and working with data structures (lists, dictionaries, etc.)
2. Implementing functions for data manipulation
3. Handling validations
4. Utilizing control structures (loops and conditionals)
5. Applying algorithmic thinking to problem-solving
"""


# Task 1: Data Structure Manipulation
# Implement a function to merge two dictionaries. If a key exists in both dictionaries, sum their values.
# Example:
# Input: {'a': 1, 'b': 2}, {'b': 3, 'c': 4}
# Output: {'a': 1, 'b': 5, 'c': 4}
def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()  # Create a copy of dict1
    for key, value in dict2.items():  # Iterate through dict2
        merged[key] = merged.get(key, 0) + value  # Sum values for duplicate keys
    return merged


# Task 2: Data Validation
# Implement a function to validate email addresses. A valid email must contain '@' and '.' after '@'.
# Example:
# Valid: 'user@example.com', 'name.surname@domain.co'
# Invalid: 'userexample.com', 'name@domain', 'name@.com'
def validate_email(email):
    if "@" in email and "." in email.split("@")[-1]:  # Check for '@' and '.' after it
        return True
    return False


# Task 3: Algorithmic Problem Solving
# Implement a function to find the longest increasing subsequence in a list of integers.
# Example:
# Input: [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4 (The sequence: [2, 3, 7, 101])
def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)  # Initialize DP array
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:  # Check for increasing order
                dp[i] = max(dp[i], dp[j] + 1)  # Update DP value
    return max(dp)  # Return the length of the longest subsequence


# Task 4: Control Structures
# Implement a function to count the number of vowels in a given string.
# Example:
# Input: 'hello world'
# Output: 3 (vowels: e, o, o)


def count_vowels(s):
    vowels = "aeiouAEIOU"  # Define vowels
    return sum(1 for char in s if char in vowels)  # Count vowels


# Task 5: Combined Application
# Implement a function that accepts a list of dictionaries containing employee data (name, age, department).
# Return a dictionary summarizing the average age per department.
# Example:
# Input: [
#     {'name': 'Alice', 'age': 30, 'department': 'HR'},
#     {'name': 'Bob', 'age': 40, 'department': 'HR'},
#     {'name': 'Charlie', 'age': 25, 'department': 'IT'},
#     {'name': 'Dave', 'age': 35, 'department': 'IT'}
# ]
# Output: {'HR': 35.0, 'IT': 30.0}


def average_age_per_department(employees):
    department_age = {}  # Dictionary to hold total age and count
    for emp in employees:
        dept = emp["department"]
        if dept not in department_age:
            department_age[dept] = [0, 0]  # [total_age, count]
        department_age[dept][0] += emp["age"]  # Add age
        department_age[dept][1] += 1  # Increment count
    return {
        dept: total / count for dept, (total, count) in department_age.items()
    }  # Calculate average
