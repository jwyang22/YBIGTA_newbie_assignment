from lib import create_circular_queue, rotate_and_remove


"""
TODO:
- josephus_problem 구현하기
    # 요세푸스 문제 구현
        # 1. 큐 생성
        # 2. 큐가 빌 때까지 반복
        # 3. 제거 순서 리스트 반환
"""


def josephus_problem(n: int, k: int) -> list[int]:
    """
    n명 중 k번째마다 제거하는 순서를 반환

    Args:
        n(int): queue의 크기. 즉 문제에서의 사람 수
        k(int): 제거하는 사람의 위치
    """
    queue = create_circular_queue(n)
    result = []
    while queue:
        temp = rotate_and_remove(queue, k)
        result.append(temp)
    return result

def solve_josephus() -> None:
    """입, 출력 format"""
    n: int
    k: int
    n, k = map(int, input().split())
    result: list[int] = josephus_problem(n, k)
    
    # 출력 형식: <3, 6, 2, 7, 5, 1, 4>
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    solve_josephus()