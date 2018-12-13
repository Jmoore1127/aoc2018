#!/usr/local/opt/pyenv/shims/python
import re
def solve():
	chain = None
	with open("input.txt", "r") as f:
		chain = f.readline()
	baseChain = chain.strip()
	polymers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	allChains = []
	for p in polymers:
		pattern = "["+p + chr(ord(p) + 32) + "]"
		newChain = re.sub(pattern, '', baseChain)
		foundMatch = True
		while foundMatch:
			foundMatch = False
			for i in range(0, len(newChain) - 1):
				if abs(ord(newChain[i]) - ord(newChain[i + 1])) == 32:
					foundMatch = True
					if i + 2 >= len(newChain):
						newChain = newChain[:i]
					else:
						newChain = newChain[:i] + newChain[i+2:]
					break
		print("%s: %d" % (p, len(newChain)))
		allChains.append(newChain)
	bestChain = min(allChains, key=lambda c: len(c))
	print(len(bestChain))
	print(bestChain)
	# print("done")

if __name__ == "__main__":
	solve()

