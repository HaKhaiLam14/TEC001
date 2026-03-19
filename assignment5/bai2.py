import re

def is_valid_hex_color(color):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(pattern, color))


print(is_valid_hex_color("#FFA500"))  
print(is_valid_hex_color("#ff00ff"))  
print(is_valid_hex_color("123456"))   