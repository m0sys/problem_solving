def data_reverse(data):
    # CONSTANT
    LEN_BYTE = 8
    NUM_BYTE = (len(data) / LEN_BYTE)

    # Variables
    start = (len(data) - LEN_BYTE)
    end = len(data)
    newData = []

    # Reversing data
    for i in range(NUM_BYTE):
        newData += data[start : end]
        start -= LEN_BYTE
        end -= LEN_BYTE

    return newData



    
    
# Testing
data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]

print data_reverse(data1) == data2
print data_reverse(data3) == data4


