import sys


def main():
    filename = sys.argv[1]
    with open(filename, 'rb') as f:
        b: bytes = f.read()
    
    allData = b''
    startSearchIndex = 0

    while True:
        idatIndex = b.find(b'IDAT', startSearchIndex)
        if idatIndex == -1:
            break
        startSearchIndex = idatIndex + 1;
        size_bytes = b[idatIndex - 4:idatIndex]
        dataSize = int.from_bytes(size_bytes, byteorder='big')
        data = b[idatIndex + 4:idatIndex + 4 + dataSize]

        allData += data

    sys.stdout.buffer.write(allData)


if __name__ == "__main__":
    main()
