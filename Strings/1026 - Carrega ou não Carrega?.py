def xorSum(x,y):
	return x^y

while True:
    try:
      n=map(int, raw_input().split())
      print xorSum(n[0],n[1])   
    except:
        break