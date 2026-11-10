def dichotomic(input_list, val):
    # caso terminale
    if len(input_list) == 1:
        if input_list[0] == val:
            return True
        else:
            return False
    # caso ricorsivo
    else:
        index = len(input_list)//2
        return (dichotomic(input_list[:index], val)
                or dichotomic(input_list[index:], val))

if __name__ == '__main__':
    sequenza = [1,2,3,4,5,6,7,8,9]
    print(dichotomic(sequenza, 4))
    print(dichotomic(sequenza, 11))