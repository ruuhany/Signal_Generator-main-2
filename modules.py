def verification(config, args):
    final_var = list()

    for i, element in enumerate(config) :
        if config[i].split('=')[0].strip().lower() == args[i]:
            final_var.append(int(config[i].split('=')[1].strip()))
        else:
            print('Expected: {}. Recieved : {}'.format(args[i].lower().capitalize(),config[i].split('=')[0].strip()))
    return final_var