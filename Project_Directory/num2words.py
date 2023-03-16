def num2words(num):
    ones = ['','one','two','three','four','five','six','seven','eight','nine']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    thousands = ['','thousand','million','billion','trillion','quadrillion','quintillion','sextillion','septillion','octillion','nonillion','decillion']
    
    if num == 0:
        return 'zero'
    
    # split number into groups of three digits
    num_str = str(num)
    num_groups = (len(num_str) + 2) // 3
    num_str = num_str.zfill(num_groups * 3)
    groups = [int(num_str[i:i+3]) for i in range(0, len(num_str), 3)][::-1]
    
    # convert each group to words
    words = []
    for i, group in enumerate(groups):
        if group == 0:
            continue
        huns, tens_, ones_ = group // 100, (group % 100) // 10, group % 10
        if huns:
            words.append(ones[huns] + ' hundred')
        if tens_ in (0, 1):
            ones_ += tens_ * 10
        elif tens_:
            words.append(tens[tens_])
        if ones_:
            if tens_ == 0 and i != 0 and groups[i-1] != 0:
                words.append('and ' + ones[ones_])
            elif i == 0 or groups[i-1] == 0:
                words.append(ones[ones_])
            else:
                words.append('-' + ones[ones_])
        if group != 0 and i != len(groups)-1:
            words.append(thousands[i])
    
    return ' '.join(words)

