import re

# 1. String that has 'a' followed by zero or more 'b'
pattern = r"ab*"
text = "abbb"
print(bool(re.fullmatch(pattern, text)))


# 2. 'a' followed by two to three 'b'
pattern = r"ab{2,3}"
text = "abbb"
print(bool(re.fullmatch(pattern, text)))


# 3. Sequences of lowercase letters joined with an underscore
pattern = r"[a-z]+_[a-z]+"
text = "hello_world test_value"
print(re.findall(pattern, text))


# 4. One uppercase letter followed by lowercase letters
pattern = r"[A-Z][a-z]+"
text = "Hello World Test"
print(re.findall(pattern, text))


# 5. 'a' followed by anything, ending in 'b'
pattern = r"a.*b"
text = "axxxb"
print(bool(re.fullmatch(pattern, text)))


# 6. Replace spaces, commas, or dots with colon
text = "Hello, world. Python is cool"
result = re.sub(r"[ ,\.]", ":", text)
print(result)


# 7. Convert snake_case to camelCase
def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)

print(snake_to_camel("snake_case_string"))


# 8. Split string at uppercase letters
text = "HelloWorldPython"
result = re.findall(r"[A-Z][^A-Z]*", text)
print(result)


# 9. Insert spaces between words starting with capital letters
text = "HelloWorldPython"
result = re.sub(r"([A-Z])", r" \1", text).strip()
print(result)


# 10. Convert camelCase to snake_case
def camel_to_snake(text):
    return re.sub(r"([A-Z])", r"_\1", text).lower().lstrip("_")

print(camel_to_snake("camelCaseString"))