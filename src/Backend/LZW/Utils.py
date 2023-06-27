class Utils:
    def decimalToBinary(code: int) -> str:
        binary: str = bin(code).replace("0b","")
        return binary
    
    def binaryToDecimal(binary: str):
        return int(binary, 2)