import ftplib

def anon_ftp(ip):
    try:
        ftp = ftplib.FTP(ip)
        ftp.login('anonymous', '')
        ftp.quit()
        return True
    except:
        return False

with open('ips.txt', 'r') as file:
    ips = file.readlines()

for ip in ips:
    ip = ip.strip()
    if anon_ftp(ip):
        print(f"Anonymous login is allowed on {ip}")
    else:
        print(f"Anonymous login is not allowed on {ip}")
