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
            currentChars = currentChars[len(currentChars)-1]

    if (currentChars in entries):
        output.append(entries.index(currentChars))
    else:
        output.append(entries.index(currentChars[:-1]))
        output.append(entries.index(currentChars[len(currentChars)-1]))
        currentChars = ""

    return output