import os

config_file = os.path.basename('/test_case/config.txt')
config = {}
with open(config_file) as f:
    for line in f:
        key, value = line.strip().split('=')
        config[key] = value

# read the text file and replace the values
text_file = os.path.basename('/test_case/text.txt')
changed_lines = []
with open(text_file) as f:
    for line in f:
        changed_line = line
        for key, value in config.items():
            changed_line = changed_line.replace(key, value)
        if changed_line != line:
            changed_lines.append((changed_line, len(changed_line) - len(line)))

# sort the changed lines by the number of symbols replaced
changed_lines.sort(key=lambda x: x[1], reverse=True)

# output the resulting text to console
for line, count in changed_lines:
    print(line.strip())

# run the following command in terminal
# python main.py config.txt text.txt 