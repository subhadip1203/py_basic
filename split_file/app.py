

import os
 
def fileBreak(filename , chunkSize = 8):
  file_size = os.path.getsize(filename)
  print(file_size, "bytes")
  
  with open(filename, "rb") as f:
    while (byte := f.read(chunkSize)):
      print(byte)

fileBreak('./sample-file.txt.encrypted' , 20)