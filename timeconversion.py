import os
def timeConversion(s):
    # Write your code here
    meridian = s[-2:]
    if (s[:2] != '12') and (meridian == 'PM'):
        s = str(12 + int(s[:2])) + s[2:]
    elif (s[:2] == '12') and (meridian == 'AM'):
        s = '00' + s[:2]
    return s[:-2]
        
    print(meridian)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
