import os
import hashlib


def md5(path):
    m_md5 = hashlib.md5()
    fs = open(path, "rb")
    m_md5.update(fs.read())
    fs.close()
    return str(m_md5.hexdigest())


dirs = ["/home/dual/code/adnewsbee-client"]
files = {}
black_list = ['package.json']
while len(dirs) > 0:
    for dir1 in dirs:
        for file1 in os.scandir(dir1):
            if file1.is_dir():
                dirs.append(file1.path)
            elif file1.is_file():
                if file1.name in black_list:
                    continue
                if file1.name not in files:
                    files[file1.name] = []
                files[file1.name].append(file1)
        dirs.remove(dir1)

for key, it in files.items():
    if len(it) > 1:
        print(key, ":")
        for it1 in it:
            print("\t[size:%s\tmd5:%s] %s" %
                  (os.path.getsize(it1.path), md5(it1.path), it1.path))
