import numpy as np
import random
import os
from PIL import Image

def crask(num):
    start = int(np.sqrt(num))
    factor = num / start
    while int(factor) != factor:
        start += 1
        factor = num / start
    return start, int(factor)

if __name__ == "__main__":
    total = 9
    m, n = crask(total)
    M, N = 1000, 1000
    
    scaleRow, scaleCol = [0]*m , [0]*n
    for i in range(1, m):
        scaleRow[i] = random.randint(scaleRow[i-1], M//np.sqrt(2))
    scaleRow.append(M)
    for j in range(1, n):
        scaleCol[j] = random.randint(scaleCol[j-1], N//np.sqrt(2))
    scaleCol.append(N)

    filenames = os.listdir('img/')

    img = Image.new('RGB', (M,N), (255,255,255))
    for i in range(m):
        for j in range(n):
            imgNow = Image.open('img/'+filenames[-1]).crop((scaleRow[i],scaleCol[j],scaleRow[i+1],scaleCol[j+1]))
            filenames.pop()
            img.paste(imgNow, (scaleRow[i],scaleCol[j],scaleRow[i+1],scaleCol[j+1]))
            img.show()
    
    img.show()
