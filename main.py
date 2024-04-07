from pysnmp.hlapi import *

f = open("ips.txt", "r")


def getCount(ip, oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData("public", mpModel=0),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid)),
    )
    g = next(iterator)
    return g


for x in f:
    y = x.split(", ")
    ip = y[0].strip()
    try:
        imp = y[1].strip()
    except:
        imp = ""

    if imp == "Canon":
        oid = [
            ".1.3.6.1.4.1.1602.1.11.1.3.1.4.101",
            ".1.3.6.1.4.1.1602.1.11.1.3.1.4.201",
        ]
        count = 0

        for id in oid:
            try:
                count += getCount(ip, id)[3][0][1]
            except:
                count = "Erro :("
        print(f"{ip} = {count}")
    else:
        oid = "1.3.6.1.2.1.43.10.2.1.4.1.1"
        g = getCount(ip, oid)
        try:
            count = g[3][0][1]
        except:
            count = "Erro :("
        print(f"{ip} = {count}")

f.close()
