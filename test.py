#ATBS Ch 7: Regular Expressions
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code
    (\s|-|\.)?  # separator
    (\d{3}) # first 3 digits
    (\s|-|\.)?  # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @
    [a-zA-Z0-9.-]+  # domain name
    (\.[a-zA-Z]+)    # dot-something
)''', re.VERBOSE)

def find_clip_matches():
    text = str(pyperclip.paste())
    matches = []

    for groups in phoneRegex.findall(text):
        pNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            pNum += ' x' + groups[8]
        matches.append(pNum)

    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    return matches

def main():
    matches = find_clip_matches()
    if len(matches) > 0:
        text = '\n'.join(matches)
        print(text)
    else:
        print('No matches found')

main()