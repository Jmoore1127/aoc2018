#!/usr/local/opt/pyenv/shims/python
def solve():
	with open("input.txt", "r") as f:
		twos = 0
		threes = 0
		for line in f:
			counts = dict({})
			for c in line:
				if c == '\n':
					continue
				if c in counts:
					counts[c] += 1
				else:
					counts[c] = 1
			hasTwo = False
			hasThree = False
			for k, v in counts.items():
				hasTwo = hasTwo or v == 2
				hasThree = hasThree or v == 3
			if hasTwo:
				twos += 1
			if hasThree:
				threes += 1
		print("Checksum: %d" % (twos * threes))

if __name__ == "__main__":
	solve()