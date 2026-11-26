class EnrollmentService:

    def __init__(self, course):
        self.course = course
        self.learners = {}

    def add_learner(self, learner):
        self.learners[learner.learner_id] = learner

    def is_eligible(self, learner_id):

        learner = self.learners.get(learner_id)

        if learner is None:
            return False

        if self.course.prerequisite is None:
            return True

        return (
            self.course.prerequisite
            in learner.completed_courses
        )

    def enroll(self, learner_id):

        if learner_id not in self.learners:
            return "Learner not found"

        if learner_id in self.course.enrolled:
            return "Already enrolled"

        if learner_id in self.course.waitlist:
            return "Already waitlisted"

        if not self.is_eligible(learner_id):
            return "Prerequisite not satisfied"

        if len(self.course.enrolled) < self.course.capacity:
            self.course.enrolled.add(learner_id)
            return "Enrolled successfully"

        self.course.waitlist.append(learner_id)
        return "Added to waitlist"

    def drop(self, learner_id):

        if learner_id not in self.course.enrolled:
            return "Learner not enrolled"

        self.course.enrolled.remove(learner_id)

        self.promote_waitlist()

        return "Dropped successfully"

    def promote_waitlist(self):

        size = len(self.course.waitlist)

        for _ in range(size):

            learner_id = self.course.waitlist.popleft()

            if self.is_eligible(learner_id):
                self.course.enrolled.add(learner_id)
                return

            self.course.waitlist.append(learner_id)

    def get_status(self):
        return {
            "enrolled": sorted(list(self.course.enrolled)),
            "waitlist": list(self.course.waitlist)
        }