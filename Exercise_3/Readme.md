3. What are the possible reasons for the following defect? How would you go about debugging the problem and gathering more information?

Answer : Key here is page refresh also did not change results.

	a. Possibility #1 - UI/Front end issue 
		Response for the PATCH request was 200 it means phone number got updated successfully in the backend. Since page refresh also didn't update the phone number it means GET request got the response but Front end did not update it.
	b. Possibility #2 - backend bug
		Response for the PATCH request was not 200 it means phone number did not get updated in the backend, hence when use did see updates result even when he refreshed the page.