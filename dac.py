import os
import subprocess
import time

def HMSCR():
    print("==============================")
    print(" IDCAMS CATALOG ALL IN TOOL   ")
    print("==============================")
    print("-----------------------------------------------------------------------------------")
    print("  1.CREATE                               |  2.GENERAL COMMAND                      ")
    print("---------------------------------------- + ----------------------------------------")
    print(" 11 - CREATE KSDS VSAM                   |  21 - DELETE VSAM CLUSTER               ")
    print(" 12 - CREATE RRDS VSAM                   |  22 - VIEW CATALOG INFORMATION          ")
    print(" 13 - CREATE ESDS VSAM                   |  23 - REPOR CLUSTER                     ")
    print(" 14 - Instance/Database Info             |  24 - LIBGEN ALL VSAM CLUSTER           ")
    print("-----------------------------------------------------------------------------------")
    print("  Q - QUIT                                                                         ")
    print("-----------------------------------------------------------------------------------")
    chos = raw_input("Choose the Number or Command :")
    if chos == "Q" :
       quit()
    if chos == "11" :
        KSDS()
    if chos == "12" :
        print("Feature NOT RDY")
        return(HMSCR)
    if chos == "13" :
        print("Feature NOT RDY")
        return(HMSCR)
    if chos == "14" :
        print("Feature NOT RDY")
        return(HMSCR)
    if chos == "21" :
        DELVSAM()
    if chos == "22" :
        VCTLG()
    else :
        print("You choose wrong number.")
        print("Try Again..")
        time.sleep(2)
        subprocess.call("clear")
        HMSCR()


#####11 - CREATE KSDS VSAM
def KSDS():
    subprocess.call(["clear"])
    print("VSAM KSDS CLUSTER CREATER")

    dsn = raw_input("VSAM NAME :")
    kl = raw_input("KEY LEN/POS :")
    le = raw_input("AVG/MAX LRECL : ")
    vl = raw_input("VOLUME : ")

    line= ("idcams define -t CL -n " + dsn + " -k " + kl + " -l " + le + " -v " + vl)

    print (" ")
    print(line)
    vrf = raw_input("is this correct information(y/n):")
    print (" ")

    if vrf == "y":
       print("Creating VSAM FILE ")
       os.system(line)
       rqrt = raw_input("Do you wish to return to HOME Screen? (y/n) :")
       if rqrt == "y" :
          HMSCR()
       if rqrt == "n" :
          print("Next Time...")
          print("QUIT")
          quit()
       else :
          print("Try Again..")
    else :
        print (" ")
        print("VSAM CLUSTER NOT GENERATED")



####21 - DELETE VSAM CLUSTER
def DELVSAM():
    dsn = raw_input("Which VSAM Cluster do you wish to delete?:")
    line = ("idcams delete " + dsn)

    print(" ")
    print(line)
    vrf = raw_input("is this correct information(y/n):")
    print(" ")

    if vrf =="y":
       print("Deleting VSAM CLUSTER " + dsn)
       os.system(line)
       rqrt = raw_input("Do you wish to return to HOME Screen? (y/n) :")
       if rqrt == "y" :
          HMSCR()
       if rqrt == "n":
          print("Next Time...")
          print("QUIT")
          quit()
    else :
       print("Error Deleting VSAM CLUSTER")


####22 - VIEW CATALOG INFORMATION
def VCTLG():
    dsn = raw_input("Which VSAM Cluster do you wish to view?:")
    line = ("tjesmgr psds " + dsn)
    subprocess.call(["clear"])
    os.system(line)
    print(" ")

    rqrt = raw_input("Do you wish to return to HOME Screen? (y/n) :")
    if rqrt == "y" :
       subprocess.call(["clear"])
       HMSCR()
    if rqrt == "n":
       print("Next Time...")
       print("QUIT")
       quit()


####23 - REPOR CLUSTER
def RPCL():
    rpentr = raw_input("ENTRY DATASET:")
    rptarg = raw_input("TARGET DATASET:")

    line = ("idcams repro -o " + rpentr + " -i " + rptrag)

    print(" ")
    print(line)
    vrf = raw_input("is this correct information(y/n):")
    print(" ")

    if vrt == "y":
       print("IDCAMS REPRO START " + rptarg )
       os.system(line)
       rqrt = raw_input("Do you wish to return to HOME Screen? (y/n) :")
       if rqrt == "y" :
          HMSCR()
       if rqrt == "n":
          print("Next Time...")
          print("QUIT")
          quit()


####24 - LIBGEN ALL VSAM CLUSTER

####CONSOL COMMAND
HMSCR()
