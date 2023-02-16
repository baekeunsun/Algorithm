def cut (problem):
    problem_2 = problem.replace('()','1')

    pipe = 0
    num = 0

    for i in range(len(problem_2)):
        if problem_2[i] == '(':
            pipe += 1
        elif problem_2[i] == '1':
            num += pipe
        elif problem_2[i] == ')':
            pipe -= 1
            num += 1

    return num


problem = input()
print(cut(problem))