import re

def is_valid_course_code(code):
    pattern = r'^[A-Z]{2,3}\d{3}$'
    return bool(re.match(pattern, code))


print(is_valid_course_code("TEC001"))  
print(is_valid_course_code("AU006"))   
print(is_valid_course_code("T1C001"))