import os

if __name__ == '__main__':
    sub_path = ['masked', 'unmasked']

    f = open("det_list.txt", "a")

    for root in os.listdir(os.getcwd()):
        curr =  os.path.join(os.getcwd(), root)
        if os.path.isdir(curr) and not curr.endswith('.ipynb_checkpoints'):
            # deal with masked
            for file in os.listdir(os.path.join(os.getcwd(), root, 'masked')):
                if file.endswith('.jpg'):
                    line = '{} 1\n'.format(os.path.join(root, 'masked', file))
                    f.write(line)
            # deal with unmasked
            for file in os.listdir(os.path.join(os.getcwd(), root, 'unmasked')):
                if file.endswith('.jpg'):
                    line = '{} 0\n'.format(os.path.join(root, 'unmasked', file))
                    f.write(line)
    f.close()
