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
	workers = [None] * 5
	currentTime = 0
	while len(tasks) > 0 or not workersDone(workers):
		task = getNextTask(tasks)
		if task is None:
			worker = getNextWorker(workers)
			currentTime = worker[1]
			completeTask(worker[0], tasks, completed)
		else:
			try:
				idx = workers.index(None)
				time = 60 + (ord(task) - ord('A') + 1)
				workers[idx] = (task, currentTime + time)
				del tasks[task]	
			except ValueError:
				worker = getNextWorker(workers)
				currentTime = worker[1]
				completeTask(worker[0], tasks, completed)

	print(''.join(completed))
	print(currentTime)
	# print(deps)
	print("done")

def workersDone(workers):
	allDone = True
	for w in workers:
		allDone = allDone and w is None
	return allDone

def getNextWorker(workers):
	worker = min(workers, key=lambda w: 99999 if w is None else w[1])
	idx = workers.index(worker)
	workers[idx] = None
	return worker

def completeTask(task, tasks, completed):
	completed.append(task)
	for k, other in tasks.items():
		if k != task:
			tasks[k] = other - {task}

def getNextTask(tasks):
	for task, deps in tasks.items():
			if len(deps) == 0:
				return task
	return None

if __name__ == "__main__":
	solve()

