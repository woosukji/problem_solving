# ๐ฅ Problem Solving ๐ฅ
#### PS Solutions & Troubleshooting

### [1003 ํผ๋ณด๋์น ํจ์](https://www.acmicpc.net/problem/1003)
- [sol : DP](https://github.com/woosukji/problem_solving/blob/main/problems/1003.py)

### [1012 ์ ๊ธฐ๋ ๋ฐฐ์ถ](https://www.acmicpc.net/problem/1012)
- [sol : BFS](https://github.com/woosukji/problem_solving/blob/main/problems/1012.py)
- ๊ณ ์  ๊ธธ์ด์ list๋ฅผ ํ ๋น :
```python
[[0]*N for _ in range(M)] 
```
- queueing ์ ๊ฐ์ ์์น๋ฅผ ์ฌ๋ฌ ๋ฒ ์์ฝํ๋ ์ง ํ์ธ
- ์ผ๋จ ๋ฐฉ๋ฌธ ํ queue ํ๊ฑฐ๋, queue์์ popํ  ๋ ๋ฐฉ๋ฌธ (pop ํ ๋จผ์  ๋ฐฉ๋ฌธํ๋์ง ์ฒดํฌํด์ผ ๋ถํ์ํ ํ์ ์ค์ด๋ฆ)

### [1074 Z](https://www.acmicpc.net/problem/1074)
- [sol : DP](https://github.com/woosukji/problem_solving/blob/main/problems/1074.py)

### [1463 1๋ก ๋ง๋ค๊ธฐ](https://www.acmicpc.net/problem/1463)
- [sol : DP](https://github.com/woosukji/problem_solving/blob/main/problems/1463.py)
- ๋ฌด์กฐ๊ฑด ์ ์ฒด ๊ฒฝ์ฐ๋ฅผ ์ฌ๊ท๋ก ๋๋ ค๋ฃ๋๋ค๊ณ  ๋๋ ๊ฒ ์๋!
- edge case์์ recursive depth๋ฅผ ๊ณ ๋ คํ์.

### [1697 ์จ๋ฐ๊ผญ์ง](https://www.acmicpc.net/problem/1697)
- [sol : DP(bit complex)](https://github.com/woosukji/problem_solving/blob/main/problems/1697.py)
- ์ฌ๊ท๋ก ์ต๋๊ฐ์ด ๋์จ๋ค๋ ์ฆ๋ช์ด ํ์ํจ. ์ ์๋  ๊ฒฝ์ฐ ๊ณ ๋ ค ๋ชปํ case๊ฐ ์์ ์ ์๋ค

### [1764 ๋ฃ๋ณด์ก](https://www.acmicpc.net/problem/1764)
- [sol : linear search](https://github.com/woosukji/problem_solving/blob/main/problems/1764.py)
- string ๊ฐ ๋์๋น๊ต ๊ฐ๋ฅ:
```python
'abc' < 'cba'    #True
```

### [1927 ์ต์ ํ](https://www.acmicpc.net/problem/1927)
- [sol : heap](https://github.com/woosukji/problem_solving/blob/main/problems/1927.py)
- ๋ฌธ์ ์ ๋ฐ๋ผ ์ธ๋ฑ์ค 1๋ถํฐ ์์ํ๋ ๊ฒ์ด ํธํ  ์ ์๋ค. 

### [1931 ํ์์ค ๋ฐฐ์ ](https://www.acmicpc.net/problem/1931)
- [sol : linear search](https://github.com/woosukji/problem_solving/blob/main/problems/1931.py)
- O(n) ํฌ๊ธฐ ๋ฐ์ดํฐ๋ฅผ ์ฌ๊ท๋ก ์ ๋ฌํ๋ฉด O(n^2) ๊ฐ ๋๋ค. (๋ฐ๋ณต๋ฌธ์ผ๋ก ๋ฐ๊พผ๋ค๊ณ  ๋์์ง๋ ๊ฒ ์๋ ๋ฏ)

### [2630 ์์ข์ด ๋ง๋ค๊ธฐ](https://www.acmicpc.net/problem/2630)
- [sol : DP](https://github.com/woosukji/problem_solving/blob/main/problems/2630.py)
- multiple for-loop in list comprehension :
```python
list = [[1,2],[3,4]]
flat = [ x for li in list for x in li ]  # [1,2,3,4]

# for list flattening, you can try (note: super slow) :
flat = sum(list, [])
```

### [7576 ํ ๋งํ ](https://www.acmicpc.net/problem/7576)
- [sol : BFS](https://github.com/woosukji/problem_solving/blob/main/problems/7576.py)
