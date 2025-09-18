#import os
#os.remove("myfile.txt")
try:
    import os
    os.remove("myfile.txt")
except FileNotFoundError:
    print("file not found")
