# Python does not impose a limit on the range of values and integer can take so
# this method is possible. Must be careful in other languages
def plus_one(A):
    val = 0
    for i in range(len(A)):
        val = val*10 + A[i]
    valPlusOne = val + 1
    output = []

    while valPlusOne:
        output.append(valPlusOne%10)
        valPlusOne = valPlusOne // 10
    return output[::-1]

# Work on each bit at a time
def plus_one_alt(A):
    output = []
    lastVal = A[-1] + 1
    carryBit = lastVal // 10
    output.append(lastVal % 10)
    for i in range(len(A)-2, -1, -1):
        val = A[i] + carryBit
        carryBit = val // 10
        output.append(val % 10)
    return output[::-1]

def binary_variant(stringOne, stringTwo):
    a, b = int(stringOne, 2), int(stringTwo, 2)
    sum, carryin, k, temp_a, temp_b = 0, 0, 1, int(stringOne, 2), int(stringTwo, 2)
    while temp_a or temp_b:
        ak, bk = a & k, b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        sum = sum | (ak ^ bk ^ carryin)



def better_binary_variant(stringOne, stringTwo):
    return None

if __name__ == "__main__":
    A = [1, 2, 9]
    input1 = "110"
    input2 = "111"
   # input2 = "10101101"
    print(plus_one(A))
    print(plus_one_alt(A))
    print(binary_variant(input1, input2))