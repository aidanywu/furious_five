
def make_candy(small, big, goal):
    if goal < big * 5:
        goal %= 5
    else:
        goal -= big * 5
    if goal > small:
        return -1
    else:
        return goal


print(make_candy(4, 1, 9))
print(make_candy(4, 1, 10))
print(make_candy(4, 1, 7))
print(make_candy(6, 6, 34))
print(make_candy(1923, 128, 2312))
print(make_candy(5, 32141234124, 6))
