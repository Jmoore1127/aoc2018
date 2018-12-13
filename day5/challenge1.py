#!/usr/local/opt/pyenv/shims/python
def solve():
	chain = None
	with open("input.txt", "r") as f:
		chain = f.readline()
	chain = chain.strip()
	foundMatch = True
	while foundMatch:
		foundMatch = False
		for i in range(0, len(chain) - 1):
			if abs(ord(chain[i]) - ord(chain[i + 1])) == 32:
				foundMatch = True
				if i + 2 >= len(chain):
					chain = chain[:i]
				else:
					chain = chain[:i] + chain[i+2:]
				break
	print(len(chain))
	print("done")

if __name__ == "__main__":
	solve()

