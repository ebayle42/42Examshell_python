import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_room_scheduler.py")
r = t.rng


def min_rooms(meetings):
    events = []
    for s, e in meetings:
        events += [(s, 1), (e, -1)]
    events.sort(key=lambda x: (x[0], x[1]))
    cur = best = 0
    for _, d in events:
        cur += d
        best = max(best, cur)
    return best


def checker(args, expected, got):
    """Exact match, or any valid assignment that uses the minimum number of rooms."""
    if got == expected:
        return True
    meetings = args[0]
    if not isinstance(got, dict) or set(got) != {"total_rooms", "schedule"}:
        return False
    rooms = got["schedule"]
    if got["total_rooms"] != min_rooms(meetings) or len(rooms) != got["total_rooms"]:
        return False
    used = []
    for room in rooms:
        room = [list(m) for m in room]
        for a, b in zip(room, room[1:]):
            if a[0] > b[0] or a[1] > b[0]:
                return False
        used += room
    return sorted(used) == sorted(list(m) for m in meetings)


cases = [([[0, 30], [5, 10], [15, 20]],), ([],), ([[7, 10], [2, 4]],), ([[1, 5]],),
         ([[0, 10], [10, 20], [20, 30]],), ([[1, 4], [2, 5], [3, 6], [4, 7]],)]
for _ in range(300):
    starts = r.sample(range(0, 60, 2), r.randint(1, 10))
    cases.append(([[s, s + 2 * r.randint(1, 10) + 1] for s in starts],))
t.func("py_room_scheduler", cases, checker=checker).done()
