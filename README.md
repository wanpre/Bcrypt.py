# Bcrypt爆破器
Bcrypt password cracker
<hr>
-h==help
-p  指定待破解文件,1行填加密文本,2行填盐值,没有盐
不填2行
-d 指定字典
使用实例

``
python3 Bcrypt.py -ppp a.txt -d ../../rockyou.txt
``
