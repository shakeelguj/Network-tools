from tkinter import W
from netaddr import IPNetwork
import sys

if len(sys.argv) != 2:
    print("Please Specify file")
    sys.exit(1)

file_data = ""
prefix_array = []
with open(sys.argv[1], 'r') as file:
    file_data = file.readlines()

for i in range(len(file_data)):
    net_addr = file_data[i].split('-')[0]
    broadcast_addr = file_data[i].split('-')[1]

    net_id_octects = net_addr.split('.')
    broad_id_octects = broadcast_addr.split('.')

    same_octect = 0
    same_bit = 0

    # prefix length - net mask convertion
    for k in range(4):
        net_id_octects[k] = int(net_id_octects[k])
        broad_id_octects[k] = int(broad_id_octects[k])
        if net_id_octects[k] == broad_id_octects[k]:
            same_octect += 1
        else:
            net_one = format(net_id_octects[k], '08b') 
            broad_one = format(broad_id_octects[k], '08b')
            for j in range(8):
                if net_one[j] == broad_one[j]:
                    same_bit += 1
            
            

    # prefix
    # saving the result in the new file
    with open('prefix_result.txt', 'a') as file:
        file.write(f"{net_addr}/{((same_octect)*8) + same_bit}\n")

