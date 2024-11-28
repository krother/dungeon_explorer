
from __future__ import annotations

from pydantic import BaseModel

class Level:
    name: str
    north: Level|None = None
    south: Level|None = None
    east: Level|None = None
    west: Level|None = None


world = Level(name="castle",
              north=Level(name="dungeon"),
              south=Level(name="woods",
                          south=Level(name="deep woods",
                                      south=Level(name="house at the lake")
                                      ),
                          east=Level(name="wooden hut",
                                     east=Level(name="mine")),
                          ),
              east=Level(name="cave"),
              )

# get the names of all levels
