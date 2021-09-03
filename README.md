<p align="center">
  <a href="https://play.codejam.devsu.com/" rel="noopener">
 <img src="https://play.codejam.devsu.com/images/login/dcj_logo.svg?imwidth=750" alt="Project logo"></a>
</p>
<div align="center">

[![Code Jam](https://img.shields.io/badge/Devsu%20Code%20Jam-2021-orange.svg)](http://hackathon.url.com)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---

<p align="center"> Soluciones a los problemas de la pre-clasificatoria del Devsu Code Jam 2021
    <br> 
</p>

## 📝 Table of Contents

- [Problem Statement](#problem_statement)
- [Idea / Solution](#idea)
- [Usage](#usage)
- [Authors](#authors)
## 🧐 Problem Statement <a name = "problem_statement"></a>

### 1. Maximum distance

  Given a text and a subText that might be in the text, return the maximum distance from the subText to any side of the text. If the subText is not in the text, return -1. The distance is the number of characters from the subText to any of the text sides.

    Example 1:

    Input:
        text = abcdefghi
        subText = de

    Output: 4

    Explanation:

    The minimum distance is the one on the right side (fghi).

    Example 2:

    Input:
        text = abcdefgci
        subText = c

    Output: 7

    Explanation:

    The maximum distance is on the left side to the second c.

    Constraints:
        1 <= text.length <= 2147483647
        1 <= subText.length <= text.length

  Text and subText contain only English lowercase letters

### 2. Maximum element with the minimum sum

  Let numbers be an array of integers. Get the maximum element in the array that produces the smallest sum when adding all the elements that are different from itself.

    Example 1:

    Input:

    numbers = [1,2,3,3,3,3,4,5,6,6]

    Output: 6

    Explanation:
        For 1, the sum of the rest of elements different from itself is 2+3+3+3+3+4+5+6+6 = 35
        For 2, the sum is 34.
        For 3, the sum is 24.
        For 4, the sum is 32.
        For 5, the sum is 31.
        For 6, the sum is 24.

  Both 3 and 6 produce the smallest sum (24), but 6 is greater than 3. Therefore, 6 is the maximum element that produces the smallest sum.

  Also, consider that the numbers can be positive or negative.

### 3. Simple sequence

  Consider the following sequence: 1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, …

  Given a number n that represents an index in the sequence, return the corresponding element in the sequence.

    Example 1
    Input:
    n = 0
    Output: 1

    Example 2
    Input:
    n = 5
    Output: 4

    Example 3
    Input:
    n = 76
    Output: 39

    Example 4
        The result for 545421 is 272712

    Constraints
        0 <= n < 9223372036854775807

  Hint

  An integer might not be able to store some of these values.


###  4. Custom header title

  Let letters be a string of uppercase English letters and n an integer that represents a column number. Return the an “excel-like” header title (a string) that corresponds to n using the characters in letters.

    Example 1

    Input
        letters = AB
        n = 5

    Output

    BB

    Explanation

    For the first values of n, the header title is:
        n = 0 -> A
        n = 1 -> B
        n = 2 -> AA
        n = 3 -> AB
        n = 4 -> BA
        n = 5 -> BB
        n = 6 -> AAA
        n = 7 -> AAB

    So, for n = 5, the output is BB.

    Example 2

    Input
        letters = ABC
        n = 4

    Output:

    AB

    For the first values of n, the header title is:
        n = 0 -> A
        n = 1 -> B
        n = 2 -> C
        n = 3 -> AA
        n = 4 -> AB
        n = 5 -> AC
        n = 6 -> BA
        n = 7 -> BB

    Therefore, the output is AB

    Example 3:

    Input
        letters = ABCD
        n = 83

    Output:

    DDD

  Constraints
      0 <= n < 2147483647
      letters string contains only uppercase English letters.

  Consider that letters can have repeated characters, thus, you can get the same header title for multiple columns.

  Pregunta 5 - 0 PUNTOS - Peso: 29%

###  5. Minimum sum in paths

  Given a rectangular matrix of integers m, consider all the paths starting from the top right to the bottom left corner and return the minimum sum of numbers among all paths.

  You can only move in two directions: left or down.

    Example 1

    Input:

    m = [[0,0,0],[0,1,1], [0,1,1]]

    Output:

    0

    Explanation:

    The sum of the elements in the following path, which is 0, is the minimum.

                    0 ◀ 0 ◀ 0     < start here
                    ▼
                    0   1   1
                    ▼
    End here >     0   1   1

    Example 2

    Input:

    m = [[1,2], [3,4], [6,-10]]

    Output:

    2

    Explanation:

    The sum of the elements in the following path, which is 2, is the minimum.

                1    2   < start here
                      ▼
                3    4
                      ▼
    End here >  6 ◀ -10

  
###  6. Arrays creator

  Given two integers size and u, return the number of all the possible arrays of length size you can create using u different integers with the condition that no more than 2 elements are repeated one after another. The elements you use do not matter, just make sure they are different.

    Example 1

    Input:

    size = 1, u = 3

    Output: 3

    Explanation:

    Here, u = 3 different elements were used: 1, 2, and 3. The arrays of length size = 1 are:

    [1]
    [2]
    [3]

    Example 2

    Input:

    size = 3, u = 3

    Output: 24

    Explanation:

    The possible arrays are:

    [1,1,2]    [2,2,1]    [3,3,1]
    [1,1,3]    [2,2,3]    [3,3,2]
    [1,2,2]    [2,1,1]    [3,1,1]
    [1,2,3]    [2,1,3]    [3,1,2]
    [1,3,2]    [2,3,1]    [3,2,1]
    [1,3,3]    [2,3,3]    [3,2,2]
    [1,2,1]    [2,1,2]    [3,1,3]
    [1,3,1]    [2,3,2]    [3,2,3]

    Note that the following arrays are not an option because the elements are repeated sequentially more than two times.

    [1,1,1]
    [2,2,2]
    [3,3,3]

    Constraints
        1 <= size <= 9
        1 <= u <= 10

## 💡 Idea / Solution <a name = "idea"></a>

This section is used to describe potential solutions.

Once the ideal, reality, and consequences sections have been
completed, and understood, it becomes easier to provide a solution for solving the problem.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development
and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

```
Python 3
```

## 🎈 Usage <a name="usage"></a>

Run python Questioxx.py (replace xx with number answer)

## ✍️ Authors <a name = "authors"></a>

- [@CrisPirat](https://github.com/CrisPirat) 

