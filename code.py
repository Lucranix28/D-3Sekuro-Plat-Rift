import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def jarak_terpendek (zone1, zone2) : # langkah yang harus diambil untuk mencapai zone 2 dari zone 1

    a = zoneMap[zone1]
    b = zoneMap[zone2]
    c = []
    if zone1 in zoneMap[zone2] :
        return [zone2]
    else :
        way = [ [] for i in (len(b)) ]
        for i in (len(b)) :
            if b[i] == zone1 :
                return way[i]
            else :
                way[i].extend(jarak_terpendek(zone1,b[i]))
    return way

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]

# Array of array zone yang terhubung
zoneMap = [[] for i in range (zone_count)]
for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    zoneMap[zone_1].append(zone_2)
    zoneMap[zone_2].append(zone_1)

# game loop
mapped = [ False for i in range (zone_count+1)] # daerah yang pernah dilewati kita
mapped_plat = [ 0 for i in range (zone_count+1)]
mypod = [0 for i in range (zone_count+1)] # array berisi jumlah pod kita tiap zone
enBase = str('A') # base musuh
i = int(0) # indeks
while True:
    my_platinum = int(input())  # your available Platinum
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]
        pod_p = 0
        if my_id==0 :
            pod_p = pods_p0
            pod_en = pods_p1
        else :
            pod_p = pods_p1
            pod_en = pods_p2

        mypod[i] = pod_p

        if pod_p > 0 :
            mapped[zone_count] = True
            mapped_plat[zone_count] = platinum

    eksekusi =""
    for i  in range (zone_count):
        if pod_en != 0 and enBase == 'A':
            enBase = int(zone_count)

        unmapped = []
        if mypod[i] > 0 :
            sekitar = zoneMap[i]
            for j in range(len(sekitar)) :
                if (not mapped[sekitar[j]]) :
                    unmapped.append(sekitar[j])

                if len(unmapped) > 0 :
                    for j in range (len(unmapped)) :
                        if ( not(mapped[j]) and len(unmapped) >= 1 ) :
                            if ( mypod[i] == 1):
                                eksekusi += str(mypod[i])+" "+str(i)+" "+str(int(unmapped[j]))+" "
                            else :
                                eksekusi += str(mypod[i]//(len(unmapped)-1))+" "+str(i)+" "+str(unmapped[j])+" "
                else :
                    for j in range (len(sekitar)) :
                        if ( not(mapped[j]) and len(sekitar) >= 1 ) :
                            if ( mypod[i] == 1):
                                eksekusi += str(mypod[i])+" "+str(i)+" "+str(int(sekitar[j]))+" "
                            else :
                                eksekusi += str(mypod[i]//(len(sekitar)-1))+" "+str(i)+" "+str(int(sekitar[j]))+" "



    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    print(eksekusi)
    print("WAIT")
