def decode(codes: list[int], ascii_list: list[str]) -> str:
    entries: list[str] = ascii_list.copy()
    currentIndex: int = 0
    output: str = ""

    currentCode = codes[currentIndex]
    entries.append(entries[currentCode])
    output += entries[currentCode]
    currentIndex += 1
    while (currentIndex < len(codes)):
        currentCode = codes[currentIndex]
        entries[len(entries)-1] += (entries[currentCode])[0]
        entries.append(entries[currentCode])
        output += entries[currentCode]
        currentIndex += 1

    return output


def bwtDecode(chars: str) -> str:
    lastSpace = chars.rindex(" ")
    oRow = int(chars[lastSpace+1:])
    chars = chars[:-(len(chars)-lastSpace)]
    listBWT = [char for char in chars]
    listBWT.sort()

    for i in range(len(chars)-1):
        listBWT = [oChar+char for oChar, char in zip(chars, listBWT)]
        listBWT.sort()

    return listBWT[oRow]


def rleDecode(chars: str) -> str:
    output = ""
    currentChar = chars[0]
    count = ""

    for i in range (1, chars.rindex(" ")):
        if (not (chars[i].isdigit())):
            if (count == ""):
                output += currentChar
            else:
                output += currentChar*int(count)
            currentChar = chars[i]
            count = ""
        else:
            count += chars[i]

    output += currentChar*int(count) + chars[chars.rindex(" "):]
    return output