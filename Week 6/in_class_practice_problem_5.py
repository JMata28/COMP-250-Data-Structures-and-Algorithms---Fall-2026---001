from collections import deque

def timeRequiredToBuy(tickets, k):
    q = deque(range(len(tickets)))
    time = 0

    while True:
        person = q.popleft()

        tickets[person] -= 1
        time += 1

        if person == k and tickets[person] == 0:
            return time

        if tickets[person] > 0:
            q.append(person)