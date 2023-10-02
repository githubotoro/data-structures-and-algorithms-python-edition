# My DSA Journey

## How to run code?

1. Clone this repo + open in terminal
2. Write `Sample Input` in `input.txt` and `Sample Output` in `output.txt`
3. Open the `.py` file in the VSCode window
4. Click on run button on top-right corner of the window

> Note: Do not cd into nested folders, instead run .py directly from main folder -- because the input and output are fetched from main folder's input.txt and output.txt files.

## Graphs

<details>
<summary>Cycle Detection Algorithm using DFS</summary>

-   We use DFS and maintain two hash sets visited + cycle.
-   Time Complexity -- O(V + E), same as that of DFS traversal
-   Links: [Youtube](https://www.youtube.com/watch?v=TXkDpqjDMHA), [Code](./graphs/cycle-detection.py)

<details><summary>Sample Input</summary>

```
0 1
1 2
2 3
3 4
4 1
3 5
```

</details>
<details> <summary>Sample Output</summary>

```
True
```

</details>

</details>

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
<summary>14. Longest Common Prefix</summary>

-   We just need to find 2 strings -- lexicographically smallest and lexicographically largest
-   Then, we only need to find common between these 2 strings -- that will be the common prefix for all strings
-   Time complexity is: O(n) (array traversal) + O(m) (finding prefix), where n is the total number of strings and m is the maximum length of the string among all the strings in the list
-   Links: [Leetcode](https://leetcode.com/problems/longest-common-prefix/), [Code](/leetcode/0014.py)

</details>

<details>
<summary>205. Isomorphic Strings</summary>

-   We create 2 caches -- then, start traversing either of the strings
-   If s1 char exists in cache 1, if it does but is not equal to s2 char -- then, strings are not isomorphic
-   Else, if s2 char exists in cache 2, that means strings are not isomorphic (why? -- think yourself)
-   At the end in else statement, store s1 char in cache1 and s2 char in cache2
-   Linear time complexity, O(n) where n is the length of input string
-   Links: [Leetcode](https://leetcode.com/problems/isomorphic-strings/), [Code](/leetcode/0205.py)

</details>

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
