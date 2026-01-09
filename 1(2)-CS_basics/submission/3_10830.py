from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))

    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        """
        행렬의 특정 위치에 값을 할당하거나 수정합니다.
        수가 커지는 걸 방지하기 위해 1000으로 나눈 나머지를 입력합니다.
        
        Args:
            key(tuple): 수정을 원하는 행렬의 인덱스 (행, 열)을 담은 튜플
            value(int): 해당 위치에 새로 저장할 정수값
        """
        self.matrix[key[0]][key[1]] = value % Matrix.MOD

    def __matmul__(self, matrix: Matrix) -> Matrix:
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1

        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j]

        return result

    def __pow__(self, n: int) -> Matrix:
        """
        분할 정복 논리를 사용하여 행렬 제곱 연산을 수행합니다.

        Args:
            n(int): 행렬을 곱할 횟수. 즉 행렬 제곱에서의 지수

        Returns: 
            Matrix: 행렬 제곱 연산을 수행한 결과
        """
        if n == 0:
            return Matrix.eye(self.shape[0])
        half = self ** (n//2)
        if n % 2 == 0:
            return half @ half
        else:
            return half @ half @ self

    def __repr__(self) -> str:
        """
        행렬을 문제에서 요구하는 출력 형식에 맞추어 변환합니다.

        Returns:
            str: 띄어쓰기와 줄바꿈으로 구성된 행렬
        """
        result = ""
        for row in self.matrix:
            line = ""
            for i in row:
                line += str(i) + " "
            result += line.strip() + "\n"
        return result.strip()
            


from typing import Callable
import sys


"""
-아무것도 수정하지 마세요!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    lines: list[str] = sys.stdin.readlines()

    N, B = intify(lines[0])
    matrix: list[list[int]] = [*map(intify, lines[1:])]

    Matrix.MOD = 1000
    modmat = Matrix(matrix)

    print(modmat ** B)


if __name__ == "__main__":
    main()