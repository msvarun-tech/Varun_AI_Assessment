from dataclasses import dataclass, field
from collections import deque


@dataclass
class Learner:
    learner_id: str
    completed_courses: set[str]


@dataclass
class CourseOffering:
    course_id: str
    capacity: int
    prerequisite: str | None = None

    enrolled: set[str] = field(default_factory=set)
    waitlist: deque = field(default_factory=deque)