import re

def solve():
	drift = 0
	patt = re.compile("([+-])(\d+)")
	frequencies = set({})
	frequencies.add(0)

	duplicated = False

	while not duplicated:
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
				
				if drift in frequencies:
					print("Found duplicate frequency %d" % drift)
					duplicated = True
					break
				frequencies.add(drift)

	print("Total Drift: %d" % drift)
	print("Keys: %d" % len(frequencies))
	
if __name__ == "__main__":
	solve()