with open('machine_code.hack', 'r') as machine_code, open('pong/Pong.hack', 'r') as pong:
    counter = 0
    wrong_code = {}
    for mine, their in zip(machine_code, pong):
        counter += 1
        if mine != their:
            print(mine, their)
            if mine + ' ' + 'instead of' + ' ' + their in wrong_code.values():
                continue
            else:
                wrong_code[counter] = mine + ' ' + 'instead of' + ' ' + their

    print(wrong_code)