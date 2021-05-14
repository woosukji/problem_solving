# 🥇 Problem Solving 🥇
PS Solutions & Troubleshooting

### [1012 유기농 배추](https://www.acmicpc.net/problem/1012)
- [sol : BFS]()
- 고정 길이의 list를 할당 :
```python
[[0]*N for _ in range(M)]
```
- queueing 시 같은 위치를 여러 번 예약하는 지 확인
- 일단 방문 후 queue 하거나, queue에서 pop할 때 방문 (이 때 먼저 방문했는지 체크해야 불필요한 탐색 줄어듦)
