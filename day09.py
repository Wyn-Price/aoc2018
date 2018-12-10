from collections import deque

def maxScore(players, max_score):
    scores = [0 for i in range(players)]
    circle = deque([0])

    for marble in range(1, max_score + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % players] = scores[marble % players] + marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    return max(scores)

print(maxScore(459, 71790))
print(maxScore(459, 71790 * 100))
