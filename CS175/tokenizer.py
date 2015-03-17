# Correct words in file starts with '$'

def split_data(filename):
    '''Reads file and returns a dictionary of words with 
       key as the correct word, and values as strings of misspelled words
       to match Norvig's testing set format'''
       
    f = open(filename, 'r')
    test_dict = dict()

    for line in f:
        if line.startswith('$'):
            key = line.strip('$\n')
            test_dict[key] = ''
        else:
            if len(test_dict[key]) == 0:
                test_dict[key] += line.strip('\n')
            else:
                test_dict[key] += ' ' + line.strip('\n')
    f.close()
    return test_dict

if __name__ == '__main__':
    print(split_data('wikipedia.dat'))