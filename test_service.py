from src.models import Learner
from src.models import CourseOffering
from src.service import EnrollmentService


def create_service():

    course = CourseOffering(
        course_id="CS101",
        capacity=1,
        prerequisite="INTRO"
    )

    service = EnrollmentService(course)

    service.add_learner(
        Learner("A", {"INTRO"})
    )

    service.add_learner(
        Learner("B", {"INTRO"})
    )

    service.add_learner(
        Learner("C", {"INTRO"})
    )

    service.add_learner(
        Learner("D", set())
    )

    return service


def test_successful_enrollment():

    service = create_service()

    result = service.enroll("A")

    assert result == "Enrolled successfully"
    assert "A" in service.course.enrolled


def test_waitlist_when_full():

    service = create_service()

    service.enroll("A")

    result = service.enroll("B")

    assert result == "Added to waitlist"
    assert list(service.course.waitlist) == ["B"]


def test_duplicate_enrollment():

    service = create_service()

    service.enroll("A")

    result = service.enroll("A")

    assert result == "Already enrolled"


def test_duplicate_waitlist():

    service = create_service()

    service.enroll("A")
    service.enroll("B")

    result = service.enroll("B")

    assert result == "Already waitlisted"
    assert len(service.course.waitlist) == 1


def test_fifo_promotion():

    service = create_service()

    service.enroll("A")
    service.enroll("B")
    service.enroll("C")

    service.drop("A")

    assert "B" in service.course.enrolled
    assert list(service.course.waitlist) == ["C"]


def test_prerequisite_failure():

    service = create_service()

    result = service.enroll("D")

    assert result == "Prerequisite not satisfied"


def test_invalid_drop():

    service = create_service()

    result = service.drop("A")

    assert result == "Learner not enrolled"


def test_repeated_drop():

    service = create_service()

    service.enroll("A")

    first = service.drop("A")
    second = service.drop("A")

    assert first == "Dropped successfully"
    assert second == "Learner not enrolled"
