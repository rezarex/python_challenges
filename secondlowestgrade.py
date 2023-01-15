if __name__ == '__main__':
    score_list = []
    marksheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        marksheet.append([name, score])
    second_low = sorted(list(set(score_list)))[1]
    names = [name for name, score in sorted(marksheet) if score == second_low]
    print('\n'.join(names))