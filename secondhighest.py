if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newArr = list(sorted(set(arr)))
    print(newArr[-2])