# lib.py의 Matrix 클래스를 참조하지 않음
import sys


"""
TODO:
- fast_power 구현하기 
"""


def fast_power(base: int, exp: int, mod: int) -> int:
    """
    세 정수를 받아 거듭제곱 및 나머지 연산을 수행합니다.

    Args:
        base (int): 거듭제곱할 수(밑)
        exp (int): 거듭제곱할 지수
        mod (int): 나머지 연산에서의 나누는 수

    Returns:
        int: (base ** exp) % mod의 결과값
    """

    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = fast_power(base, exp // 2, mod)
        return (half * half) % mod
    else:
        half = fast_power(base, exp // 2, mod)
        return (half * half * base) % mod
    

def main() -> None:
    A: int
    B: int
    C: int
    A, B, C = map(int, input().split()) # 입력 고정
    
    result: int = fast_power(A, B, C) # 출력 형식
    print(result) 

if __name__ == "__main__":
    main()
