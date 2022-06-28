import re
EMAIL_REGEX = r"[\w\.-]+@[\w\.-]+"
for a in re.findall(EMAIL_REGEX, """ahmed@gmail.com
M@gmail.com"""):
    print(a)