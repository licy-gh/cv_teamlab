import os
import random

if __name__ == '__main__':
    appendix_list = ['am.jpeg', 'au.jpeg', 'bm.jpeg', 'bu.jpeg']
    file_to_write = open('pairs.txt', 'a')  

    # deal with true 0 to 599
    curr_dir = os.path.join(os.getcwd(), 'true')
    for i in range(0, 600):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('true', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 1\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    # deal with false 0 to 599
    curr_dir = os.path.join(os.getcwd(), 'false')
    for i in range(0, 600):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('false', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 0\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    # deal with true 600 to 1199
    curr_dir = os.path.join(os.getcwd(), 'true')
    for i in range(600, 1200):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('true', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 1\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    # deal with false 600 to 1199
    curr_dir = os.path.join(os.getcwd(), 'false')
    for i in range(600, 1200):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('false', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 0\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    # deal with true 1200 to 1799
    curr_dir = os.path.join(os.getcwd(), 'true')
    for i in range(1200, 1800):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('true', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 1\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    # deal with false 1200 to 1799
    curr_dir = os.path.join(os.getcwd(), 'false')
    for i in range(1200, 1800):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('false', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 0\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    # deal with true 1800 to 2399
    curr_dir = os.path.join(os.getcwd(), 'true')
    for i in range(1800, 2400):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('true', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 1\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    # deal with false 1800 to 2399
    curr_dir = os.path.join(os.getcwd(), 'false')
    for i in range(1800, 2400):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('false', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 0\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    # deal with true 2400 to 2999
    curr_dir = os.path.join(os.getcwd(), 'true')
    for i in range(2400, 3000):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('true', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 1\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    # deal with false 2400 to 2999
    curr_dir = os.path.join(os.getcwd(), 'false')
    for i in range(2400, 3000):
        file_list = [str(i) + x for x in appendix_list]
        path_list = [os.path.join('false', x) for x in file_list]
        first_random_item, second_random_item = random.sample(path_list, 2)
        if os.path.isfile(first_random_item) and os.path.isfile(second_random_item):
            pair_line = '{} {} 0\n'.format(first_random_item, second_random_item)
            file_to_write.write(pair_line)

    file_to_write.close()
