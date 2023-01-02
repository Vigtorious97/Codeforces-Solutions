t=int(input())
for _ in range(t):
	n,a=int(input()),input()
	ans=""
	sum=a[0]
	for i in range(1,n):
		if sum=='1' and a[i]=='1':
			sum='0'
			ans+='-'
			continue
		sum=str(int(sum)+int(a[i]))
		ans+='+'
	print(ans)