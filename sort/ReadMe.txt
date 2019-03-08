

每一个算法在ReadMe.txt里面要有对应的伪代码
伪代码示例如下

input: an array a of length n with array elements numbered 0 to n − 1
inc ← round(n/2)
while inc > 0 do:
    for i = inc .. n − 1 do:
        temp ← a[i]
        j ← i
        while j ≥ inc and a[j − inc] > temp do:
            a[j] ← a[j − inc]
            j ← j − inc
        a[j] ←  temp
    inc ← round(inc / 2)

输入：1个长度为n的矩阵a，矩阵的编号从0到n - 1
整数inc从n / 2到1，每次循环inc变为inc / 2
	i从inc到n - 1，每次循环i变为i + 1
		将a[ i ]的值赋给temp
		j从i 到inc，每次循环j变为j - inc
			如果a[ j − inc ]大于temp，则将a[ j - inc ]的值赋给a[ j ]
			否则跳出j循环
		j循环结束
		将temp的值赋给a[ j ]
	i循环结束
inc循环结束




左箭头 ← >=
右箭头 → 到 表示 <=