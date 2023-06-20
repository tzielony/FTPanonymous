import ftplib

def mount_ftp(ip):
    try:
        ftp = ftplib.FTP(ip)
        ftp.login('anonymous', '')
        print(f"Anonymous login successful on {ip}")
        ftp.cwd('/')
        files = ftp.nlst()
        print(f"Files in root directory: {files}")
        ftp.quit()
    except:
        print(f"Anonymous login failed on {ip}")

with open('ips.txt', 'r') as file:
    ips = file.readlines()

for ip in ips:
    ip = ip.strip()
    mount_ftp(ip)