#!/usr/local/opt/pyenv/shims/python
def solve():
	with open("input.txt", "r") as f:
		lines = f.readlines()
		for i in range(0, len(lines)):
			currentLine = lines[i]
			for j in range(i+1, len(lines)):
				difference = 0
				commonLetters = []
				comparedLine = lines[j]
				for k in range(0, len(currentLine)):
					if currentLine[k] == comparedLine[k]:
						commonLetters += currentLine[k]
					else:
						difference += 1
				if difference == 1:
					print(''.join(commonLetters))
					return

if __name__ == "__main__":
	solve()