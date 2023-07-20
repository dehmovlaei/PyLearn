def concentric(num, emo='emo_list'):
    emo_list = ['💀','😥','😖','🥶','😡','🤢','🤐','👽']
    center = (num-1) / 2
    if not center.is_integer() or center < 0:
        raise ValueError('input an odd positive number')
    rug = []
    for row in range(num):
        tmp = []
        for col in range(num):
            result = int(max(abs(col - center), abs(row - center)))
            if emo == 'emo_list':
                tmp.append(emo_list[result%(len(emo_list))])
            else:
                tmp.append(result)
        rug.append(tmp)
    return rug

def print_concentric_rugs(rug):
    for row in rug:
        for char in row:
            print(char, end=' ')
        print()

number = int(input('concentric rugs...enter a number:   '))
print_concentric_rugs(concentric(number))