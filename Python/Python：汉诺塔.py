# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
现有三个柱子，在第一个柱子有number个盘子要移动多少次才能全部移动到第三个柱子？
规则：1、第一个柱子是按照盘子大小从小到大放置，
      2、在三根柱子之间一次只能移动一个圆盘
      3、移动的时候只能小盘子在上，大盘子在下
"""
# 第一种
count = 0


def move(n, x, y, z):
    if n == 1:
        global count
        count += 1
        print("第%d次： %s -->  %s" % (count, x, z))
    else:
        move(n - 1, x, z, y)  # 将前n-1个盘子从x移动到y上
        move(1, x, y, z)  # 将最底下的最后一个盘子从x移动到z上
        move(n - 1, y, x, z)  # 将y上的n-1个盘子移动到z上


n = int(input("请输入汉诺塔的层数："))
move(n, "x", "y", "z")

# 第二种
def move(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return move(number - 1) * 2 + 1


print(move(10))
