import os

if __name__  == '__main__':
    ftw = open('img_list.txt', 'a')
    for dir in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), dir)):
            for file in os.listdir(os.path.join(os.getcwd(), dir)):
                line = '{}\n'.format(os.path.join(dir, file))
                ftw.write(line)
    ftw.close()