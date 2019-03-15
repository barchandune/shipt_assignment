3. What are the possible reasons for the following defect? How would you go about debugging the problem and gathering more information?

Answer : Key here is page refresh also did not change results.

	a. Possibility #1 - UI/Front end issue 
		Response for the PATCH request was 200 it means phone number got updated successfully in the backend. Since page refresh also didn't update the phone number it means GET request got the response but Front end did not update it.
	b. Possibility #2 - backend bug
		Response for the PATCH request was not 200 it means phone number did not get updated in the backend, hence when user hit referesh he still found old result.
		
Debugging options - 
1. Find HTTP Status code.
2. Verify right header is being used.
3. Look body of response.
4. Add some logs/print statements in web app 
5. Similarly add some print statement in backend.
6. Run Wireshark and/or Charles to intercept/sniff SSL/TLS traffic if required.
