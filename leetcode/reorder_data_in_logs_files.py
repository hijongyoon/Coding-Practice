logs = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
str_logs = []
num_logs = []
for i in logs:
    x = i.split(" ")[1]
    if not x.isnumeric():
        str_logs.append(i)
    else:
        num_logs.append(i)

str_logs.sort(key=lambda x: x.split(" ")[0])  # ID sort before string in logs sort.
str_logs.sort(key=lambda x: " ".join(x.split(" ")[1:]))  # string in logs sort
# str_logs.sort(key=lambda x: (x.split()[1:], x.split()[0])) this can be instead of previous two sentences
# second argument is used to sort list when result of sort by first argument is equal.
str_logs.extend(num_logs)
print(str_logs)