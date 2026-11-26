\# Design



This solution manages enrollment for a single course.



Components:



\- Learner

\- CourseOffering

\- EnrollmentService



Rules:



\- Learners must meet prerequisites.

\- Learners can only enroll once.

\- If the course is full, learners join the waitlist.

\- Waitlist follows FIFO order.

\- When a seat opens, the first eligible learner is promoted.



Data is stored in memory and no database is used.

