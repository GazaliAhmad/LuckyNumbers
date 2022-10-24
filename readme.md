# Lucky numbers for 4D and Toto

A simple Python program to generate random 4 digits number and 6 two-digits number. One is using the random module and the other is using a generated list.

- `LuckyNumbersRandomModule.py` uses Random module and its methodolodies are described below.
- `LuckyNumbersRandomList` generates a list of numbers. List4D (0 to 9999) and ListToto (1 to 50). The numbers are randomly selected from the respective lists.

## 4D methodology

- Randomly select from 0 to 9 for each digit of 4D number.
- This is to ensure that there is an equal chance for each single digit to be selected.
- For example, if we use `random.randint(0, 9999)`, there is a higher chance for the first digit to be `0`.
- This is because the first digit has 10 possible values (0 to 9) while the other 3 digits have 1000 possible values (0 to 999). Hence, the first digit has a higher chance to be selected.
- In order to ensure that each digit has an equal chance to be selected, we randomly select from 0 to 9 for each digit
- This is to ensure that the first digit has a 10% chance to be selected, the second digit has a 10% chance to be selected, and so on

## Toto methodology

- Random selection from list (1 to 50)

Do all numbers stand an equal chance of getting selected? 

## Result

- The result is displaced as what is familiar to people.
- Removed `[] , ()`
- Leading zeros are added. Correct format: `08` and not `8`.
