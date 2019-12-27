import os
os.system('clear')
pcap_file = input("FILE>>>")
def top():
    cmd = 'tshark -T fields -e http.host -r ' + pcap_file + ' | sort | uniq -c | sort -nr | head'
    os.system(cmd)
def user():
    cmd = 'tshark -r ' + pcap_file + ' -Y \'http contains "User-Agent:"\' -T fields -e http.user_agent | sort | uniq -c | sort -nr'
    os.system(cmd)
def con_det():
    inp = input("Do you wish to continue?[Y/N]")
    if inp == 'N':
        print("Going Back To Main Menu..." )
    cmd1 = 'tshark -o "gui.column.format:\\\"Source\\\",\\\"%us\\\",\\\"src port\\\",\\\"%S\\\",\\\"Protocol\\\",\\\"%p\\\",\\\"Destination\\\",\\\"%ud\\\",\\\"dest port\\\"'
    cmd2 = ',\\\"%D\\\",\\\"Protocol\\\",\\\"%p\\\"" -r ' + pcap_file + ' | column -t'
    os.system(cmd1 + cmd2)
def grepstr():
    sa= input("STRING>>>")
    cmd = 'sudo tcpdump -r ' + pcap_file + ' -A | grep "' + sa + '"'
    os.system(cmd)
def ips():
    cmd = 'tshark -nr ' + pcap_file + ' -T fields -e ip.src -e ip.dst'
    os.system(cmd)
    
def ports():
    cmd = 'tshark -r ' + pcap_file + ' -Y "tcp" -T fields -e tcp.srcport | sort | uniq -c | sort -nr'
    os.system(cmd)
while True:
    print("1.Top 10 visited websites\n\n2.User-Agent\n\n3.Connection Details.\n\n4.Grep String.\n\n5.List All IP.\n\n6.List All Ports.\n\n7.Exit.\n")
    x= int(input(">>>"))
    if x == 1:
        print("Top 10 Visited Sites:")
        top()
    if x == 2:
        print("User Agents:")
        user()
    if x == 3:
        print( "Connection Details:" )
        con_det()
    if x == 4:
        grepstr()
    if x == 5:
        print("All Ip's:")
        ips()
    if x == 6:
        print("All Ports:")
        ports()
    if x == 7:
        print( "Closing...")
        break
