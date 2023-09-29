# My DSA Journey

## How to run code?

1. Clone this repo + open in terminal
2. Write `Sample Input` in `input.txt` and `Sample Output` in `output.txt`
3. Open the `.py` file in the VSCode window
4. Click on run button on top-right corner of the window

> Note: Do not cd into nested folders, instead run .py directly from main folder -- because the input and output are fetched from main folder's input.txt and output.txt files.

## Graphs

<details>
<summary>Shortest Path Length in Directed Acyclic Graph (DAG) using Dijkstra's Algorithm </summary>

-   Uses topological sorting
-   Linear time complexity, O(V + E)
-   Links: [Youtube](https://www.youtube.com/watch?v=TXkDpqjDMHA), [Code](./graphs/shortest-path-length-dag.py)

<details><summary>Sample Input</summary>

```
A B 3
A C 6
B C 4
B D 4
B E 11
C D 8
C G 11
D E -4
D F 5
D G 2
E H 9
F H 1
G H 2
```

</details>
<details> <summary>Sample Output</summary>

```
11
```

</details>

</details>

## Leetcode

<details>
<summary>1021. Remove Outermost Parentheses</summary>

-   Simple string iteration
-   Linear time complexity, O(n) where n is the length of input string
-   Links: [Leetcode](https://leetcode.com/problems/remove-outermost-parentheses/), [Code](/leetcode/1021.py)

</details>

<details>
<summary>1903. Largest Odd Number in String
</summary>

-   Simple string iteration
-   Linear time complexity, O(n) where n is the length of input string
-   Links: [Leetcode](https://leetcode.com/problems/largest-odd-number-in-string/description/), [Code](/leetcode/1903.py)

</details>
