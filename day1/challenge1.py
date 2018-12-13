import re

def solve():
	drift = 0
	patt = re.compile("([+-])(\d+)")
	with open('challenge1input.txt', 'r') as f:
		for line in f:
			line = line.strip()
			m = patt.match(line)
			if not m:
				print("FAILED TO MATCH: " + line)
				exit(1)
			if m.group(1) == "+":
				drift += int(m.group(2))
			else:
				drift -= int(m.group(2))
	print("Total Drift: %d" % drift)
	
if __name__ == "__main__":
	solve()