# phase3-Wk1-CodeChallenge

# Challenge1
 ## Problem Explanation
In this challenge, you are provided with a time in the 12-hour format (hour ranging from 1 to 12, minute from 0 to 59, and period "am" or "pm"). The goal is to convert this time into the 24-hour format and return it as a four-digit string.

## Solution Explanation
The convert_to_24_hour function takes three arguments: hour, minute, and period. It first checks if the period is "pm". If it is, it adds 12 to the hour (except for 12 PM, which remains 12). If the period is "am", the function converts 12 AM to 0 hour, otherwise, it keeps the same hour. The function then formats the hour and minute with leading zeros (if needed) and combines them to form a four-digit string representing the time in 24-hour format.

# Challenge 2
## Problem Explanation
In this challenge, you are given three integers a, b, and c. You need to determine if exactly two of these three integers are positive (greater than zero).

## Solution Explanation
The positive_count function takes three integer arguments: a, b, and c. It calculates the sum of positive numbers among the three arguments using a generator expression and the sum function. If the sum of positive numbers is greater than or equal to 2, the function returns True, indicating that exactly two out of the three integers are positive; otherwise, it returns False.

# Challenge3
## Problem Explanation
In this challenge, you are given a lowercase string consisting of alphabetic characters only. You need to find the highest value of consonant substrings. Consonants are defined as any letters of the alphabet except "aeiou", and each consonant has a corresponding value from a=1 to z=26.

## Solution Explanation
The highest_consonant_value function takes a string s as input. It iterates through each character in the string and checks if the character is a consonant using the is_consonant function. If it's a consonant, the function calculates the value of the consonant using the get_consonant_value function and adds it to the current_value variable. The function also keeps track of the max_value, updating it whenever a higher value is encountered. If a vowel is encountered, the current_value is reset to 0. The function returns the max_value at the end, which represents the highest value of consonant substrings in the input string.

Remember to implement the helper functions (is_consonant and get_consonant_value) as described in the initial solution.

# Setup & Pre-requisite Data
git clone the repository to your local machine using the command. 
```bash
$ git clone git@github.com:Cairie5/Phase3-Wk1-CodeChallenge.git
```

Navigate to the project using the command cd 
```bash
$ cd phase3-Wk1-CodeChallenge
```

Run the code using the command code . on your terminal 
```bash
$ code .
```

Install the necessary dependencies required 
```bash
$ pipenv install
```
```bash
 $ pipenv shell
 ```
### Technologies Used
. Python

### Author
The author of this script is Patience Wangari Muraguri.

### License
MIT License Copyright (c) [2023] [Patience Muraguri]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
