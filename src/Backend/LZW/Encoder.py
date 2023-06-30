def encode(chars: str, ascii_list: list[str]) -> list[int]:
    entries: list[str] = ascii_list.copy()
    currentChars: str = chars[0]
    currentIndex: int = 0
    output: list[int] = []

    while (currentIndex < len(chars)-1):
        if (currentChars in entries):
            currentIndex += 1
            currentChars += chars[currentIndex]
        else:
            entries.append(currentChars)
            output.append(entries.index(currentChars[:-1]))
            currentChars = currentChars[-1]

    if (currentChars in entries):
        output.append(entries.index(currentChars))
    else:
        output.append(entries.index(currentChars[:-1]))
        output.append(entries.index(currentChars[-1]))
        currentChars = ""

    return output


def bwtEncode(chars: str) -> str:
    originalChars = chars
    listBWT = [chars]

    for i  in range(len(chars)-1):
        temp = chars[-1]
        chars = chars[:-1]
        chars = temp + chars
        listBWT.append(chars)

    listBWT.sort()
    charPosition = listBWT.index(originalChars)
    output = "".join(char[-1] for char in listBWT)
    output = output + " " + str(charPosition)

    return output


def rleEncode(chars: str) -> str:
    currentChar = chars[0]
    currentCount = 1
    output = ""

    for i in range (1, chars.rindex(" ")):
        if (chars[i] == currentChar):
            currentCount += 1
        else:
            if (currentCount == 1):
                output += currentChar
            else:
                output += currentChar + str(currentCount)
            currentChar = chars[i]
            currentCount = 1

    output += currentChar + str(currentCount) + chars[chars.rindex(" "):]
    return output