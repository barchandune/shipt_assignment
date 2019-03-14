import credentials
import pytest

expected_output = "Invalid Username or Password"
@pytest.mark.parametrize("test_input, expected_output",
                         [
                             ("apoorv@gmail.com", "Test12_44"),
                             ("abc@gmail.com", "123456#*"),
                             ("shipt@yahoo.com", "123456")
                         ]
                         )

def test_invalid_credentails(test_input, expected_output):

    result = credentials.invalid_credentials(test_input)

    assert result == "Invalid Username or Password"