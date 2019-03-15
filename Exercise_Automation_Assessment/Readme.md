Automation Assessment : 
1. Skip - used Pyhton/Pytest
2. How do you debug a failed test in your test framework?
	Assuming test framework has some logging available.

1. If you chose to use a tool or language other than the recommended, briefly explain why.
2. How do you debug a failed test in your test framework?
	a. Assuming test framework has way to collect logs first thing I would do to see if logs show anything.
	b. if logs don't show anything then work with developers to add few print/debug statements and try to reproduce the issue.
3. What do you believe are the most common causes for instability in UI automation?
	a. Change in accessibility-id, tag name, label or xpath
	b. Web application uses asysnchronous calls due to which sometimes when ui script tries to find web element it cannot do so as resource is still not loaded yet. One way to overcome this would be to add Explicit wait time.
4. How do you make your tests consistent and easy to debug?
	a. Run test suite over and over to get benchmark if some test scripts fail due to instability I would remove or fix them.
	b. I will have a logging mechanism that will dump logs based on log-level being defined (1-5) 1 being verbose, 2 - error etc.