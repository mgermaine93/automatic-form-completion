# from email_validator import validate_email, EmailNotValidError

# email = "mgermaine93@gmail.com"

# print(bool(validate_email(email)))
import re

result = bool(re.match("(?:214|469|972)-\d{3}-\d{4}", "214-567-9808"))
print(result)
