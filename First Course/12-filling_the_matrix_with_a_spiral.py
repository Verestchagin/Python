Выведите таблицу размером n \times nn×n, заполненную числами от 11 до n^2 по спирали, выходящей из левого верхнего угла и закрученной
по часовой стрелке, как показано в примере (здесь n=5):

Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

-------------
n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
h = n // 2
cnt = 1
for c in range(1, h + 1):
    for column in range(c - 1, n - c + 1):
        a[c - 1][column] = cnt
        cnt += 1
    for row in range(c, n - c + 1):
        a[row][n - c] = cnt
        cnt += 1
    for column in range(n - c - 1, c - 2, -1):
        a[n - c][column] = cnt
        cnt += 1
    for row in range(n - c - 1, c - 1, -1):
        a[row][c - 1] = cnt
        cnt += 1
if n % 2 == 1:
    a[h][h] = n ** 2

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
