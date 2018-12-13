#!/usr/local/opt/pyenv/shims/python
import re
from collections import deque, defaultdict

def solve():
	with open("input.txt", "r") as f:
		players, marbles = [int(x) for x in re.findall("\d+", f.readline())]
		# print(simulate(players, marbles*100))
		print(play_game(players, marbles * 100))
		print(players, marbles)
		print("done")

def simulate(players, marbles):
	circle = [0]
	scores = [0] * players
	currentMarble = 0
	for m in range(1, marbles + 1):
		if m % 23 == 0:
			currentPlayer = (m - 1) % players
			scores[currentPlayer] += m
			extraIndex = currentMarble - 7
			scores[currentPlayer] += circle[extraIndex]
			if extraIndex < 0:
				currentMarble = len(circle) + extraIndex
			else:
				currentMarble = extraIndex % len(circle)
			del circle[extraIndex]
		else:
			if (currentMarble == len(circle) - 2) or len(circle) == 1:
				circle.append(m)
				currentMarble = len(circle) - 1
			else:
				nextIndex = (currentMarble + 2) % len(circle)
				circle.insert(nextIndex, m)
				currentMarble = nextIndex
	winningScore = max(scores)
	winner = scores.index(winningScore) + 1
	return winner, winningScore

def play_game(max_players, last_marble):
	scores = defaultdict(int)
	circle = deque([0])

	for marble in range(1, last_marble + 1):
		if marble % 23 == 0:
			circle.rotate(7)
			scores[marble % max_players] += marble + circle.pop()
			circle.rotate(-1)
		else:
			circle.rotate(-1)
			circle.append(marble)

	return max(scores.values()) if scores else 0

if __name__ == "__main__":
	solve()

