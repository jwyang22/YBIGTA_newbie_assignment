from __future__ import annotations
from collections import deque


"""
TODO:
- rotate_and_remove 구현하기 
"""


def create_circular_queue(n: int) -> deque[int]:
    """1부터 n까지의 숫자로 deque를 생성합니다."""
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> int:
    """
    큐에서 k번째 원소를 제거하고 반환합니다.

    rotate 메서드를 활용해 원소를 회전하여
    제거하고자 하는 원소를 맨 앞으로 이동시켜 추출합니다.

    Args:
        queue(deque[int]): 제거할 원소가 담긴 deque
        k(int): 제거하고 반환할 원소의 인덱스
    """
    queue.rotate(-(k-1))
    remove = queue.popleft()
    return remove