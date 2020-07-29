import os
import subprocess
import time
import shutil
####OpenFrame DIR
OF="/opt2/tmaxapp/OpenFrame/util/IDCAMS"
CPBK="/opt2/tmaxapp/OpenFrame/tsam/copybook/"

####CODE START

def LGIN():
    subprocess.call(["clear"])
    print("==============================")
    print("IDCAMS")
    os.system("offile " + OF + " | awk {'print $2,$3'} | cut -d , -f1")
    print("==============================")
    print("==================================================")
    print(" (Disclaimer)")
    print(" These scripts come without warranty of any kind.")
    print(" Use them at your own risk.")
    print("==================================================")
    print(" ")

    psswd = raw_input("Enter ROOT Password :")
    if psswd == "####":
       pass
    else :
       subprocess.call(["clear"])
       print("==============================")
       print( "Wrong Password")
       print("==============================")
       quit()

def HMSCR():
    print("==============================")
    print(" IDCAMS CATALOG ALL IN TOOL   ")
    print("==============================")
    print("-----------------------------------------------------------------------------------")
    print("  1.CREATE                               |  2.GENERAL COMMAND                      ")
    print("---------------------------------------- + ----------------------------------------")
    print("  11 - CREATE KSDS VSAM                  |  21 - DELETE VSAM CLUSTER               ")
    print("  12 - CREATE RRDS VSAM                  |  22 - VIEW CATALOG INFORMATION          ")
    print("  13 - CREATE ESDS VSAM                  |  23 - REPOR CLUSTER                     ")
    print("  14 - CREATE OSC REGION SD              |  24 - LOCK VSAM CHECK STATUS            ")
    print("-----------------------------------------------------------------------------------")
    print("  3.TSAM COPYBOOK                        |  4.GENERAL COMMAND                      ")
    print("  31 - COPY ORIGIONAL TO TEST VSAM       |  41 - LOCK VSAM CHECK STATUS            ")
    print("  32 - COBGENSCHEMA VSAM COPYBOOK        |  42 - LOCK VSAM CHECK STATUS            ")
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
        OSCREG()
    if chos == "21" :
        DELVSAM()
    if chos == "22" :
        VCTLG()
    if chos == "23" :
        RPCL()
    if chos == "24" :
        LOCKM()
    if chos == "31" :
        CPYTST()
    if chos == "32" :
        COBGEN()
    else :
        print("You choose wrong number.")
        print("Try Again..")
        time.sleep(1)
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
          subprocess.call(["clear"])
          HMSCR()
       if rqrt == "n" :
          print("Next Time...")
          print("QUIT")
          quit()
       else :
          print("Try Again..")
    if vrf == "n":
       quit()
    else :
        print (" ")
        print("VSAM CLUSTER NOT GENERATED")


####CREATE OSC REGION SD
def OSCREG():
    subprocess.call(["clear"])
    print("CREATE OSC REGION SD")
    print(" ")
    sdnam = raw_input("REGION NAME:")

    line = ("idcams define -t CL -n OSC.SDLIB."+sdnam+" -o KS -k 18,0 -l 128,4096 -s 1024,128,128 -v DEFVOL")
    print (" ")
    print(line)
    vrf = raw_input("is this correct information(y/n):")
    print (" ")

    if vrf == "y":
       print("Creating VSAM FILE ")
       os.system(line)
       rqrt = raw_input("Do you wish to return to HOME Screen? (y/n) :")
       if rqrt == "y" :
          subprocess.call(["clear"])
          HMSCR()
       if rqrt == "n" :
          print("Next Time...")
          print("QUIT")
          quit()
    if vrf =="n" :
          quit()
    else :
        print (" ")
        print("VSAM CLUSTER NOT GENERATED")


####21 - DELETE VSAM CLUSTER
def DELVSAM():
    subprocess.call(["clear"])
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
          subprocess.call(["clear"])
          HMSCR()
       if rqrt == "n":
          print("Next Time...")
          print("QUIT")
          quit()
    if vrf =="n":
       quit()
    else :
       print("Error Deleting VSAM CLUSTER")


####22 - VIEW CATALOG INFORMATION
def VCTLG():
    subprocess.call(["clear"])
    dsn = raw_input("Which VSAM Cluster do you wish to view?:")
    line = ("tjesmgr psds " + dsn)
    subprocess.call(["clear"])
    os.system(line)
    print(" ")

    scrsve = raw_input("Do you wish to keep the catalog information(y/n):")
    if scrsve == "y":
       pass
    if scrsve == "n":
       subprocess.call(["clear"])
       pass

    rqrt = raw_input("Do you wish to return to HOME Screen?(y/n):")
    if rqrt == "y" :
       #subprocess.call(["clear"])
       HMSCR()
    if rqrt == "n":
       print("Next Time...")
       print("QUIT")
       quit()


####23 - REPOR CLUSTER
def RPCL():
    rpentr = raw_input("ENTRY DATASET:")
    rptarg = raw_input("TARGET DATASET:")

    line = ("idcams repro -o " + rpentr + " -i " + rptarg)

    print(" ")
    print(line)
    vrf = raw_input("is this correct information(y/n):")
    print(" ")

    if vrf == "y":
       print("IDCAMS REPRO START " + rptarg )
       os.system(line)
       rqrt = raw_input("Do you wish to return to HOME Screen? (y/n) :")
       subprocess.call(["clear"])
       if rqrt == "y" :
          HMSCR()
       if rqrt == "n":
          print("Next Time...")
          print("QUIT")
          quit()
    if vrf == "n":
       quit()
    else :
        print("TRY AGAIN")


####24 - LOCK VSAM CHECK STATUS
def LOCKM():
    lokdn = raw_input("Search Lock / Allocated VSAM File:")
    line1 = ("lockm list -n " + lokdn + " | grep '*' | awk {'print $4,$6'} | grep -v complete | sort -u")
    line2 = ("lockm list -n " + lokdn + " | grep '*' | awk {'print $4,$6'} | grep -v complete | sort -u | wc -l")
    print("---------SUMMARY LIST START---------------")
    os.system(line1)
    print(" ")
    print("Total Count")
    os.system(line2)
    print("---------SUMMARY LIST END-----------------")

    complist = raw_input("Do you wish to see all the list(y/n)?:")
    if complist == "y":
        line3 = ("lockm list -n " + lokdn)
        os.system(line3)
        pass
    else :
        pass

    rqrt = raw_input("Do you wish to return to HOME Screen? (y/n) :")
    subprocess.call(["clear"])
    if rqrt == "y" :
       HMSCR()
    if rqrt == "n":
       print("Next Time...")
       print("QUIT")
       quit()


####31 - COPY ORG CPYBOOK TO TEST CPYBOOK
def CPYTST():
    subprocess.call(["clear"])
    print (" ")
    print ("Exclude extension .cpy")
    print (" ")
    entrcpy = raw_input("ORG Copybook Name : ")
    targcpy = raw_input("TRG Copybook Name : ")
    
    entrful = (CPBK + entrcpy +".cpy")
    targul = (CPBK + targcpy +".cpy")

    print(" ")
    print("Copybook being copied...")
    shutil.copyfile(entrful,targul)
    print(" ")
    subprocess.call(["date"])
    print(" ")
    subprocess.call(["ls", "-rtl", targul])

    print(" ")
    cobrqu = raw_input("Do you wish to cobgensh the copybook you copied? (y/n) : ")
    if cobrqu == "y":
       rcq= raw_input("Option) Specify the length is  needed? (y/n):" )
       if rcq == "y":
          rcl = raw_input("Specify the length of the record: ")
          line1 = ("cobgensch " + targul + " -r " + rcl)
          os.system(line1)
       else :
          print("Skip Option -r ")
          line2 = ("cobgensch " + targul )
          os.system(line2)

    else :
       print("Cobgenschema not done")
       print(" ")

    rqrt = raw_input("Do you wish to return to HOME Screen? (y/n) :")
    subprocess.call(["clear"])
    if rqrt == "y" :
       HMSCR()
    if rqrt == "n":
       print("Next Time...")
       print("QUIT")
       quit()


####32 - COBGENSCHM COPYBOOK
def COBGEN():
    subprocess.call(["clear"])
    targcpy = raw_input("TRG Copybook Name : ")
    targul = (CPBK + targcpy +".cpy")
    
    rcq= raw_input("Option) Specify the length is  needed? (y/n):" )
    if rcq == "y":
       rcl = raw_input("Specify the length of the record: ")
       line1 = ("cobgensch " + targul + " -r " + rcl)
       os.system(line1)
    else :
       print("Skip Option -r ")
       line2 = ("cobgensch " + targul )
       os.system(line2)

    rqrt = raw_input("Do you wish to return to HOME Screen? (y/n) :")
    subprocess.call(["clear"])
    if rqrt == "y" :
       HMSCR()
    if rqrt == "n":
       print("Next Time...")
       print("QUIT")
       quit()


####CONSOL COMMAND
#subprocess.call(["clear"])
#LGIN()
subprocess.call(["clear"])
tm=subprocess.call(["date"])
HMSCR()
