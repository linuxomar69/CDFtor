import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 cdftor.py')
    run('mkdir /usr/share/aut')
    run('cp autoTOR.py /usr/share/aut/cdftor.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/cdftor.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/cdftor.py')
    print('''\n\ncongratulation CDFTor Ip Changer is installed successfully \nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] now Auto Tor Ip changer  has been removed successfully')
