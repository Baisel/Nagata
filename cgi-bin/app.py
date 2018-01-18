#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import shlex
import subprocess

html_body = """
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>app</title>
<style>
h1 {
font-size: 3em;
}
</style>
</head>
<body>
<h1>クエリ</h1>
<p>クエリ名はcount</p>
<p>count=%s</p>
</body>
</html>
"""

form = cgi.FieldStorage()
query = form['count'].value
print ('Content-type: text/html; charset=UTF-8')
print(html_body % query)


def writeFlagFile(): # フラグをファイルに書き込む
    with open('flag.txt','w') as f:
        f.write('start')


def startControlScript(): # catch.pyを実行する
    cmd = "python /home/tenma/Desktop/class/tech_kawamoto/Nagata/Server/catch.py"
    augs = shlex.split(cmd)
    p = subprocess.Popen(augs)


if __name__ == '__main__':
    writeFlagFile()
    startControlScript()
