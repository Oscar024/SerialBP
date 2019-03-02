import serial
import serial.tools.list_ports
devices= list()
ports = list(serial.tools.list_ports.comports())
count=0
for p in ports:
    devices.append(p.device)
    flag = "COM6" in devices[count]
    if flag == True:
        device = devices[count]
    count = count + 1
    print(p)
# device = devices[0]
print(device)

ser = serial.Serial(device, 115200,timeout=1)

data = ser.read_all()
data = data.decode("ascii")
index = data.find("GetOneBPRec01")
data = data[index:index+60]
data = data.split("\r\n")
sys = data[5]
dia = data[6]
pul = data[7]

sys = int(sys,16)
dia = int(dia,16)
pul = int(pul,16)
print(sys)
print(dia)
print(pul)