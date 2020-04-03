# https://open.kattis.com/problems/aboveaverage
cases = int(input())

for i in range(cases):
	N, *marks = list(map(int,input().split()))

	mean = sum(marks) / N

	above = 0
	
	for i in range(N):
		if marks[i]>mean:
			above += 1

	print('%.3f%s' % (round(above / N * 100, 3), "%"))
