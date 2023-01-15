if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        command_lst = input().split()
        command = command_lst[0]

        if   command == 'insert' :
            lst.insert(int(command_lst[1]), int(command_lst[2]))
        elif command == 'print' :
            print(lst)
        elif command == 'remove' :
            lst.remove(int(command_lst[1]))
        elif command == 'append' :
            lst.append(int(command_lst[1]))
        elif command == 'sort' :
            lst.sort()
        elif command == 'reverse' :
            lst.reverse()
        elif command == 'pop' :
            lst.pop()
        else:
            pass