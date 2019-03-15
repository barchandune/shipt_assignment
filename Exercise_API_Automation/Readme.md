API Automation - How to run it? If required other credentials can be added to ```@pytest.mark.parametrize```
"pytest -v"

Apoorvs-MacBook-Pro:Exercise_API_Automation apoorvkhare$ pytest -v -s
====================================================================================== test session starts ======================================================================================
platform darwin -- Python 2.7.10, pytest-4.3.0, py-1.8.0, pluggy-0.9.0 -- /System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
cachedir: .pytest_cache
rootdir: /Users/apoorvkhare/Documents/GitHub_apoorv/shipt_assignment/Exercise_API_Automation, inifile:
collected 3 items                                                                                                                                                                               
```
  test_shipt_login.py::test_invalid_credentails[apoorv@gmail.com-Test12_44] ('Response : ', u'{"error":{"message":"Invalid Username or Password","type":"invalid_grant"}}')
  PASSED
  test_shipt_login.py::test_invalid_credentails[abc@gmail.com-123456#*] ('Response : ', u'{"error":{"message":"Invalid Username or Password","type":"invalid_grant"}}')
  PASSED
  test_shipt_login.py::test_invalid_credentails[shipt@yahoo.com-123456] ('Response : ', u'{"error":{"message":"Invalid Username or Password","type":"invalid_grant"}}')
  PASSED
  ```

=================================================================================== 3 passed in 1.30 seconds ====================================================================================
