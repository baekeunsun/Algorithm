# 에너그램 만들기
first = input()
second = input()

for f in first:
    if f in second:
        second = second.replace(f, '',1)
        first = first.replace(f, '',1)

sums = len(first)+len(second)
print(sums)