# 🥇 Problem Solving 🥇
#### PS Solutions & Troubleshooting

### [1003 피보나치 함수](https://www.acmicpc.net/problem/1003)
- [sol : DP](https://github.com/woosukji/problem_solving/blob/main/problems/1003.py)

### [1012 유기농 배추](https://www.acmicpc.net/problem/1012)
- [sol : BFS](https://github.com/woosukji/problem_solving/blob/main/problems/1012.py)
- 고정 길이의 list를 할당 :
```python
[[0]*N for _ in range(M)]
```
- queueing 시 같은 위치를 여러 번 예약하는 지 확인
- 일단 방문 후 queue 하거나, queue에서 pop할 때 방문 (pop 후 먼저 방문했는지 체크해야 불필요한 탐색 줄어듦)

### [1074 Z](https://www.acmicpc.net/problem/1074)
- [sol : DP](https://github.com/woosukji/problem_solving/blob/main/problems/1074.py)

### [1463 1로 만들기](https://www.acmicpc.net/problem/1463)
- [sol : DP](https://github.com/woosukji/problem_solving/blob/main/problems/1463.py)
- 무조건 전체 경우를 재귀로 때려넣는다고 되는 게 아님!
- edge case에서 recursive depth를 고려하자.

### [1697 숨바꼭질](https://www.acmicpc.net/problem/1697)
- [sol : DP(bit complex)](https://github.com/woosukji/problem_solving/blob/main/problems/1697.py)
- 재귀로 최댓값이 나온다는 증명이 필요함. 잘 안될 경우 고려 못한 case가 있을 수 있다

### [1764 듣보잡](https://www.acmicpc.net/problem/1764)
- [sol : linear search](https://github.com/woosukji/problem_solving/blob/main/problems/1764.py)
- string 간 대소비교 가능:
```python
'abc' < 'cba'    #True
```

### [1927 최소 힙](https://www.acmicpc.net/problem/1927)
- [sol : heap](https://github.com/woosukji/problem_solving/blob/main/problems/1927.py)
- 문제에 따라 인덱스 1부터 시작하는 것이 편할 수 있다.

### [1931 회의실 배정](https://www.acmicpc.net/problem/1931)
- [sol : linear search](https://github.com/woosukji/problem_solving/blob/main/problems/1931.py)
- O(n) 크기 데이터를 재귀로 전달하면 O(n^2) 가 된다. (반복문으로 바꾼다고 나아지는 게 아닌 듯)

### [2630 색종이 만들기](https://www.acmicpc.net/problem/2630)
- [sol : DP](https://github.com/woosukji/problem_solving/blob/main/problems/2630.py)
- multiple for-loop in list comprehension :
```python
list = [[1,2],[3,4]]
flat = [ x for li in list for x in li ]  # [1,2,3,4]

# for list flattening, you can try (note: super slow) :
flat = sum(list, [])
```

### [7576 토마토](https://www.acmicpc.net/problem/7576)
- [sol : BFS](https://github.com/woosukji/problem_solving/blob/main/problems/7576.py)
