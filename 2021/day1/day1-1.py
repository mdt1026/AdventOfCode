
def main():
	def input():
		L = []
		with open("input.txt") as f:
			lines = f.read().splitlines()
			for i in lines:
				L.append(int(i))
		return L
	lines = input()
	depths = lines
	count = 0
	prev = depths[0]
	for depth in depths[1:]:
		if depth > prev:
			count += 1
		prev = depth

	print(count)

main()
