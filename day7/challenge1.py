#!/usr/local/opt/pyenv/shims/python
import re
from collections import OrderedDict

def solve():
	patt = re.compile(r'Step ([A-Z]) must be finished before step ([A-Z])')
	deps = set()
	with open("input.txt", "r") as f:
		for line in f:
			match = patt.match(line)
			if not match:
				print("FAILED TO PARSE LINE: %s" % line)
				exit(1)
			parts = match.groups()
			deps.add((parts[1], parts[0]))

	tasks = OrderedDict()
	for dep in sorted(deps):
		key = dep[0]
		val = dep[1]
		if key not in tasks:
			tasks[key] = set()
		if val not in tasks:
			tasks[val] = set()
		tasks[key].add(val)
	tasks = OrderedDict(sorted(tasks.items(), key=lambda t: t[0]))

	completed = []
	found = True
	while len(tasks) > 0 and found:
		found = False
		for task, deps in tasks.items():
			if len(deps) == 0:
				found = True
				completed.append(task)
				for k, other in tasks.items():
					if k != task:
						tasks[k] = other - {task}
				del tasks[task]
				break
	if len(tasks) != 0:
		print("FAILED TO COMPLETE ALL TASKS: %s\n" % tasks)
		exit(1)
	print(''.join(completed))
	# print(deps)
	print("done")

if __name__ == "__main__":
	solve()

