def decode(codes: list[int], ascii_list: list[str]) -> str:
    currentIndex: int = 0
    output: str = ""

    currentCode = codes[currentIndex]
    ascii_list.append(ascii_list[currentCode])
    output += ascii_list[currentCode]
    currentIndex += 1
    while (currentIndex < len(codes)):
        currentCode = codes[currentIndex]
        ascii_list[len(ascii_list)-1] += (ascii_list[currentCode])[0]
        ascii_list.append(ascii_list[currentCode])
        output += ascii_list[currentCode]
        currentIndex += 1

    return output