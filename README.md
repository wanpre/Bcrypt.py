#Bcrypt爆破器
Bcrypt password cracker

options:
  -h, --help            show this help message and exit
  -p PASSWORDFILE, --passwordfile PASSWORDFILE
                        Path to the password file
  -d DICTIONARY, --dictionary DICTIONARY
                        Path to the password dictionary file
-p指定待破解文件,1行填加密文本,2行填盐值,没有盐
不填二行
-d指定字典
使用实例
``
python3 bch1.py -h a.txt -d ../../rockyou.txt
``
