def word_to_number(word):
    if word == 'one':
        return(1)
    elif word == 'two':
        return(2)
    elif word == 'three':
        return(3)
    elif word == 'four':
        return(4)
    elif word == 'five':
        return(5)
    elif word == 'six':
        return(6)
    elif word == 'seven':
        return(7)
    elif word == 'eight':
        return(8)
    elif word == 'nine':
        return(9)
    elif word == 'ten':
        return(10)
    elif word == 'eleven':
        return(11)
    elif word == 'twelve':
        return(12)
    elif word == 'thirteen':
        return(13)
    elif word == 'fourteen':
        return(14)
    elif word == 'fifteen':
        return(15)
    elif word == 'sixteen':
        return(16)
    elif word == 'seventeen':
        return(17)
    elif word == 'eighteen':
        return(18)
    elif word == 'nineteen':
        return(19)
    elif word == 'twenty':
        return(20)
    elif word == 'thirty':
        return(30)
    elif word == 'forty':
        return(40)
    elif word == 'fifty':
        return(50)
    elif word == 'sixty':
        return(60)
    elif word == 'seventy':
        return(70)
    elif word == 'eighty':
        return(80)
    elif word == 'ninety':
        return(90)
    elif word == 'hundred':
        return(100)
    elif word == 'thousand':
        return(1000)
    elif word == 'million':
        return(1000000)
    elif word == 'billion':
        return(1000000000)
    
def converting_number(word):
    global new_list
    word = word.lower()
    word = word.split(' ')
    new_list = []
    for word in word:
        answer = word_to_number(word)
        new_list.append(answer)  
    #print(new_list)

def multiply_number(new_list):
    global output
    output = []
    hold = 0
    for current_number in new_list:
        if current_number > 999:
            if hold > 0:
                output.append(hold)
                output.append(current_number)
                hold = 0
            else:
                hold = current_number
        elif hold == 0:
            hold = current_number
        elif current_number > hold:
            hold = hold * current_number
        else:
            output.append(hold)
            output.append(current_number)
            hold = 0
    if hold != 0:
        output.append(hold)
    #print(output)
    
def add_number(output):
    global after_add
    after_add = []
    hold = 0
    for i in output:
        if i > 999:
            if hold > 0:
                after_add.append(hold)
                after_add.append(i)
                hold = 0
            else:
                hold = i
        elif hold == 0:
            hold = i
        elif  i < hold:
            hold = hold+i
        else:
            after_add.append(hold)
            after_add.append(i)
            hold = 0
    if hold != 0:
        after_add.append(hold)
    #print (after_add)
        
def combine(after_add):
    global combine
    combine = []
    hold = 0
    answer = 0
    for i in after_add:
        if i > 999:
            if hold > 0:
                hold = hold*i
            else:
                hold = i
        elif hold == 0:
            hold = i
        else:
            combine.append(hold)
            hold = i
    if hold != 0:
        combine.append(hold)
    for i in combine:
        answer = answer+i
    print (answer)

def main(a):
    converting_number(a)
    multiply_number(new_list)
    add_number(output)
    combine(after_add)
