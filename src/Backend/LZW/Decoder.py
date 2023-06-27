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