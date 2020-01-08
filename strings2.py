string = "birthday"
print(string)
print("="*80)
start = "This is converting {} to upper case and finding the word day"
output = start.format(string)
print(output)
print("="*80)
print("index location of day before conversion:")
print(string.find("day"))
print("="*80)
print(string.upper())
print("index location of day after conversion:")
print(string.upper().find("DAY")
