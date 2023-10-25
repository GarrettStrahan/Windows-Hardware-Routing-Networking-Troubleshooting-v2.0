#Programmed by Garrett Strahan
#Extended Windows Hardware/Routing/Networking/Troubleshooting v2.0

import os

if os.path.isdir('C:/test') == False:
    os.mkdir('C:/test')

print("Sytem information from systeminfo cmd")
os.system('echo "Sytem information from systeminfo cmd" > C:/test/test.txt')
os.system('systeminfo >> C:/test/testEXTENDED.txt')

print("\nHere are all your IP addresses + mac addresses")
os.system('echo "Here are all your IP addresses + mac addresses >> C:/test/test.txt')
os.system('ipconfig /a >> C:/test/testEXTENDED.txt')

print("\nCan you reach/ping Google?")
os.system('echo "Can you reach Google?" >> C:/test/test.txt')
os.system('Ping 8.8.8.8 >> C:/test/testEXTENDED.txt')

#Traceroute to google
print("\nHere is the traceroute to Google.")
os.system('echo "Here is the traceroute traceroute to Google" >> C:/test/test.txt')
os.system('tracert 8.8.8.8 >> C:/test/testEXTENDED.txt')

#This is the extended version of Windows Hardware/Routing/Networking/Troubleshooting v2.0
print("\nHere is the Path ping to Google.")
os.system('echo "This is pathping, this tells you how many packets dropped along the route to google / 8.8.8.8 on each node. Takes a while like 4 minutes." >> C:/test/testEXTENDED.txt')
os.system('pathping 8.8.8.8 >> C:/test/testEXTENDED.txt')

print("\nHere is the users to this node/system, MAKE SURE THERE IS NOT A USER YOUR NOT AWARE OF!")
os.system('echo "This lists all the users attached to this node" >> C:/test/testEXTENDED.txt')
os.system('net user >> C:/test/testEXTENDED.txt')

print("\nHere is the all the open network connections you have and the port #s.")
os.system('echo "Here is the all the open network connections you have and the port #s:" >> C:/test/testEXTENDED.txt')
os.system('netstat -n >> C:/test/testEXTENDED.txt')

print("\nHere is your ARP Table.")
os.system('echo "Here is your ARP Table." >> C:/test/testEXTENDED.txt')
os.system('arp -a >> C:/test/testEXTENDED.txt')

print("\nHere is the all the open remote sessions connected to your node.")
os.system('echo "Here is the all the open network connections you have and the port #s:" >> C:/test/testEXTENDED.txt')
os.system('net session /list  >> C:/test/testEXTENDED.txt')

print("\nHere is your routing information")
os.system('echo "Here is your routing information" >> C:/test/testEXTENDED.txt')
os.system('netstat -r >> C:/test/testEXTENDED.txt')

print("\nHere is Hard drive information including your serial numbers")
os.system('echo "Here is Hard drive information including your serial numbers" >> C:/test/testEXTENDED.txt')
os.system('wmic diskdrive get Name, Manufacturer, Model, InterfaceType, MediaType, SerialNumber. >> C:/test/testEXTENDED.txt')

print("\nHere is CPU information")
os.system('echo "Here is CPU information" >> C:/test/testEXTENDED.txt')
os.system('wmic cpu list full >> C:/test/testEXTENDED.txt')

print("\nHere is your GPU information")
os.system('echo "Here is your GPU information" >> C:/test/testEXTENDED.txt')
os.system('wmic path win32_VideoController get name >> C:/test/testEXTENDED.txt')

print("\nHere is your motherboard information")
os.system('echo "Here is your motherboard information" >> C:/test/testEXTENDED.txt')
os.system('wmic baseboard >> C:/test/testEXTENDED.txt')

print("\nHere is your driver information")
os.system('echo "Here is your driver information" >> C:/test/testEXTENDED.txt')
os.system('driverquery -v >> C:/test/testEXTENDED.txt')

print("\nHere are the programs your running")
os.system('echo "Here are the programs your running" >> C:/test/testEXTENDED.txt')
os.system('tasklist >> C:/test/testEXTENDED.txt')

print("\nWhat user is logged in?")
os.system('echo "What user is logged in?" >> C:/test/testEXTENDED.txt')
os.system('whoami >> C:/test/testEXTENDED.txt')

print("\nWhat does the system's clock say?")
os.system('echo "What does the systems clock say?" >> C:/test/testEXTENDED.txt')
os.system('echo=%DATE% >> C:/test/testEXTENDED.txt')

os.system('dxdiag -x C:/test/dxdiag')

print("Everything has been outputted to C:/test/testEXTENDED.txt, please either give this to your IT professional or read the outputted file to fix your issue")
print("Please see test.txt + dxdiag.xml")


#This was supposed to give your office version # but it does not work in python but it works in the CMD
#os.system('powershell.exe [reg query "HKEY_CLASSES_ROOT\Word.Application\CurVer"]') #got close but having issues but any powershell command is os.system('powershell.exe [command]')

#This I might erase it halts the time it takes you have to close the popup to proceed further. It is also in the "systeminfo" cmd
#print("Pop up window will present you with your Windows system version #")
#os.system('winver')