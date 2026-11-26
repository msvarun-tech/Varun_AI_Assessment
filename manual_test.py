from src.models import Learner, CourseOffering
from src.service import EnrollmentService


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

print("=== Enrollment Tests ===")

print(service.enroll("A"))
print(service.enroll("B"))
print(service.enroll("C"))

print("\nCurrent State:")
print(service.get_status())

print("\n=== Waitlist Promotion Test ===")

print(service.drop("A"))

print("\nState After Promotion:")
print(service.get_status())

print("\n=== Prerequisite Validation Test ===")

print(service.enroll("D"))

print("\n=== Duplicate Enrollment Test ===")

print(service.enroll("B"))

print("\n=== Invalid Drop Test ===")

print(service.drop("UNKNOWN"))