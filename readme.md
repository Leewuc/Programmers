# Programmers Python Practice

프로그램머스(Programmers)에서 제공하는 문제들의 풀이를 정리한 저장소입니다. 문제 풀이 코드는 주로 **Python**으로 작성되었습니다.

## Repository Layout

- `PCCE_1`, `PCCE_3`, `PCCE_4`, `PCCE_5` : PCCE 과정을 공부하면서 작성한 간단한 예제 코드
- `프로그래머스/` : 문제 번호와 제목으로 이루어진 디렉터리들이 있으며, 각 디렉터리에는 문제 설명과 풀이가 들어 있습니다.
  - 각 문제 폴더 내부에는 `README.md` 파일과 Python 솔루션 파일(`*.py`)이 있습니다.

## How to Use

1. 파이썬 3 환경에서 실행 가능합니다.
2. 원하는 문제 폴더로 이동한 뒤 Python 파일을 실행하거나 직접 확인하면 됩니다.

## Example

아래는 `181919. 콜라츠 수열 만들기` 문제의 간단한 풀이 예시입니다.
```python
def solution(n):
    answer = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer
```

각 풀이 파일의 코드는 GitHub에서 직접 확인할 수 있습니다.

## License

해당 저장소의 코드는 공부 목적으로 자유롭게 사용 가능합니다.
