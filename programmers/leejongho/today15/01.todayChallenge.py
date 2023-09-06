# 스택/큐
# 같은 숫자는 싫어

# 스택이란? 쌓아 올린것을 의미한다. 책처럼 차곡 차곡 쌓은것을 말한다.
# 넣는것은 push, 빼는 것은 pop
# |   |
# | 2 |
# | 1 |
# |_0_|
# 특징 : 가장 마지막에 쌓은 자료가 먼저 삭제 되는 특징을 가지고 있다. (후입선출) 웹 브라우저 방문기록(뒤로가기) 연상하면 된다.

# 큐란? 사전적 의미로는 줄을 기다리는 것을 말한다.
# 한쪽 끝에서는 삽입이 다른 반대편은 삭제 작업이 이루어진다.
# 
# | 2 |
# | 1 |
# | 0 |

# 스택의 개념을 활용해서
# arr = [1,1,3,3,0,1,1], result = [1,3,0,1]
# arr = [4,4,4,3,3], result = [4,3]
def solution(arr):
    result = []
    # arr의 길이에 따른 배열을 for문 하여 arr의 각각의 원소가 같은지를 구별한다.
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            result.append(arr[i])
    return result