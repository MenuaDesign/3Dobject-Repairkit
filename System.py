import re
def checkFile(input):
    x = re.search('[a-z0-9]*[^.]\.stl', input)
    if (x != None):
        print("File -> [VALID]")
        return True
    else:
        print("File -> [NOT VALID]")
        return False

def convertTo3MF():
    print("")