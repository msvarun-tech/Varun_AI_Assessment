\# AI Usage Record



\## How AI Was Used



I used AI as an engineering assistant while working on the assessment.



\## Topics Discussed



\- Overall design approach

\- Waitlist implementation

\- Choosing deque instead of list

\- Test scenarios

\- Documentation structure



\## What AI Contributed



AI suggested:



\- Separating data models from business logic.

\- Using a queue-based (deque) waitlist to support FIFO behavior.

\- Adding tests for duplicate requests, waitlist promotion, and prerequisite validation.

\- Keeping the implementation simple and focused on the assessment scope.



\## What I Changed



\- Kept the implementation focused on a single course offering as required by the assessment.

\- Simplified the design to use in-memory storage instead of introducing a database.

\- Adjusted the service structure and method names to keep the solution easy to understand.

\- Rewrote the documentation and AI usage notes in my own words.



\## What I Rejected



\- Adding a database layer.

\- Adding REST API endpoints.

\- Adding extra infrastructure beyond the assessment requirements.



These ideas were not implemented because the assessment was limited to a single course offering and allowed an in-memory solution.



\## Verification



\- Reviewed AI suggestions before implementation.

\- Manually tested enrollment, waitlist, prerequisite validation, and promotion scenarios using sample data.

\- Verified FIFO waitlist behavior using sample learners.

\- Executed automated tests using pytest.

\- Confirmed all test cases passed successfully.

