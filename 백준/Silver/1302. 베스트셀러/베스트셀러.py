# 베스트셀러
book = dict()
for _ in range(int(input())):
    name = input()
    if name in book :
        book[name] += 1
    else:
        book[name] = 1
sorted_dict = sorted(book.items(), key = lambda item: (-item[1],item[0]))
print(sorted_dict[0][0])
