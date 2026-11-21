from __future__ import annotations

from typing import Any


def py_room_scheduler(meetings: list[list[int]]) -> dict[str, Any]:
    if not meetings:
        return {"total_rooms": 0, "schedule": []}
    rooms = []
    for start, end in sorted(meetings, key=lambda m: (m[0], m[1])):
        for room in rooms:
            if room[-1][1] <= start:
                room.append([start, end])
                break
        else:
            rooms.append([[start, end]])
    return {"total_rooms": len(rooms), "schedule": rooms}
