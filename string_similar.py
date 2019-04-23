import difflib

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

s1 = "hello world"
s2 = "this is a test"

sim = string_similar(s1, s2)

print(sim)
