import os
import random

if __name__ == '__main__':
    appendix_list = ['am.jpeg', 'au.jpeg', 'bm.jpeg', 'bu.jpeg']
    file_to_write = open('pairs.txt', 'a')  

    # deal with true
    curr_dir = os.path.join(os.getcwd(), 'true')
    for i in range(3000):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('true', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 1\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    # deal with false
    curr_dir = os.path.join(os.getcwd(), 'false')
    for i in range(3000):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('false', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 0\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    file_to_write.close()
