import time,subprocess 

Filename="update_time.conf"

def get_time():
    n=300
    try:
        with open(Filename,"r") as f:
            n=int(f.read())*30
            f.close()
    except:
        print(f"FAILURE OPENING {Filename}, DEFAULTING TO 5 MINUTES.")
        n=300
        
    return n

def crawl():
    try:
        subprocess.run("rm ./latest_1024_HMIIC.jpg",shell=True,stdout=subprocess.DEVNULL)
    finally:
        try:
            subprocess.run("wget -q -o /dev/null http://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_HMIIC.jpg",shell=True,stdout=subprocess.DEVNULL)
            #print("IMAGE DOWNLOADED.")
        except:
            print("FAILURE GETTING IMAGE.")
    

while(True):
    crawl()
    n=get_time()
    time.sleep(n)
