def main():

    def checkBinaryInput(binaryInput):
        for char in binaryInput:
            if char != '0' and char != '1': # Checks if input only contains ones and zeroes
                print('Input can only be ones and zeroes')
                return False
            elif len(binary) > 8: # Checks that input is 8 characters or less
                print('Must be 8 number or less')
                return False
        return True

    def binary2Decimal(binary):
        binary = binary[::-1] # Reverses the string
        decimal = 0
        power = 0
        for num in binary:
            decimal += (int(num) * 2**power)
            power += 1
        return decimal

    while True:
        binary = input('Binary:')
        if checkBinaryInput(binary):
            decimal = binary2Decimal(binary)
            print(decimal)
            break

main()
