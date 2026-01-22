from __future__ import annotations
import copy
from collections import deque
from collections import defaultdict
from typing import DefaultDict, List


"""
TODO:
- __init__ 구현하기
- add_edge 구현하기
- dfs 구현하기 (재귀 또는 스택 방식 선택)
- bfs 구현하기
"""


class Graph:
    def __init__(self, n: int) -> None:
        """
        그래프 초기화

        Args:
            n(int): 정점의 개수 (1번부터 n번까지)
        """
        self.items: list[list[int]] = [[] for i in range(n + 1)]
        self.n = n
        # 구현하세요!

    
    def add_edge(self, u: int, v: int) -> None:
        """
        양방향 간선 추가
        u번 정점의 이웃 목록에 v를 추가한다

        Args:
            u(int): 연결할 정점의 번호
            v(int): 연결할 정점의 번호
        """
        self.items[u].append(v)
        self.items[u].sort()
        self.items[v].append(u)
        self.items[v].sort()
        # 구현하세요!
    
    def dfs(self, start: int) -> list[int]:
        """
        재귀 방식을 활용한 깊이 우선 탐색 (DFS) 구현
        
        Args:
            start(int): 탐색을 시작할 정점의 번호
        """
        # 구현하세요!
        visited = [False] * (self.n + 1)
        result = []

        def dfs_search(v: int):
            visited[v] = True
            result.append(v)
            
            for adj in self.items[v]:
                if not visited[adj]:
                    dfs_search(adj)

        dfs_search(start)
        return result
    
    def bfs(self, start: int) -> list[int]:
        """
        큐를 활용한 너비 우선 탐색 (BFS) 구현
        
        Args:
            start(int): 탐색을 시작할 정점의 번호
        """

        visited = [False] * (self.n + 1)
        queue = deque([start])
        visited[start] = True
        result = []

        while queue:
            v = queue.popleft()
            result.append(v)

            for adj in self.items[v]:
                if not visited[adj]:
                    visited[adj] = True
                    queue.append(adj)

        return result

    def search_and_print(self, start: int) -> None:
        """
        DFS와 BFS 결과를 출력
        """
        dfs_result = self.dfs(start)
        bfs_result = self.bfs(start)
        
        print(' '.join(map(str, dfs_result)))
        print(' '.join(map(str, bfs_result)))
