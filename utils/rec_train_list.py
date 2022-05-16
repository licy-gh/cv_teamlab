import os

if __name__ == '__main__':
    sub_path = ['masked', 'unmasked']

    id = 0
    f = open("list.txt", "a")

    for d in os.listdir(os.getcwd()):
        path0 = os.path.join(os.getcwd(), d)
        if(os.path.isdir(path0)):
            for sub in sub_path:
                path1 = os.path.join(path0, sub)
                tmp = os.path.join(d, sub)
                for file in os.listdir(path1):
                    path2 = os.path.join(path1, file)
                    write_path = os.path.join(tmp, file)
                    line = write_path + ' ' + str(id) + '\n'
                    f.write(line)
        id = id + 1
    f.close()
