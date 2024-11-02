from itertools import permutations


def solution(expression):
    """ 옛날 자료구조 책에서 봤던 기억...
    연산자 세개, 절대값 큰 사람, 이건 외우지 않으면 못풀어

    idea: stack, recursive call
        1) expression 전처리
        2) 연산자 우선순위 지정
        3) 중위 표기 to 후위 표기
            - 이거 변환도 스택

        4) 계산 처리 with stack: top frame vs current loop
            - if t <= c: stack.append(c)
            - else: stack.pop()
            - 시점마다 연산자 우선순위 변경
    """
    answer = 0

    # preprocess the expression array
    exp, num_p = [], 0
    ops = ["-", "+", "*"]
    for i in range(len(expression)):
        if expression[i] in ops:
            exp.append(expression[num_p:i])  # add the number
            exp.append(expression[i])  # add the calc
            num_p = i + 1

    exp.append(expression[num_p:])

    # get the case of expression's priority
    for case in permutations([0, 1, 2], 3):
        calc_stack, frame = [], -1
        priority = {
            "-": case[0],
            "+": case[1],
            "*": case[2],
        }

        # infix to postfix
        postfix = []
        for e in exp:
            if e not in ops:
                postfix.append(e)

            else:
                if priority[e] <= frame:
                    while calc_stack and priority[e] <= frame:  # 탑 프레임의 우선순위
                        postfix.append(calc_stack.pop())
                        if calc_stack:
                            frame = priority[calc_stack[-1]]

                calc_stack.append(e)
                frame = priority[e]

        calc_stack.reverse()
        postfix.extend(calc_stack)

        # do calculate the postfix
        def substract(a, b):
            return a - b

        def add(a, b):
            return a + b

        def multiply(a, b):
            return a * b

        stack = []
        calc_dict = {
            "-": substract,
            "+": add,
            "*": multiply,
        }

        for i in postfix:
            if i not in ops:
                stack.append(i)

            else:
                a, b = int(stack[-2]), int(stack[-1])  # 이거 할당 순서도 중요해!
                for j in range(2):
                    stack.pop()

                stack.append(calc_dict[i](a, b))

        answer = max(answer, abs(stack[0]))
    return answer


if __name__ == '__main__':
    solution("100-200*300-500+20")
