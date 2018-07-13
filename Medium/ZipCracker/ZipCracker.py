
'''
Usage: python3 ZipCracker.py -f <zipfile> -d <dictionaryfile>
Demo: python3 ZipCracker.py -f demo.zip -d dictionary.txt
'''
import zipfile
import  optparse
import threading
from threading import Thread

threadmax = threading.BoundedSemaphore(1000)

def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password.encode('utf-8'))
        print(" \n\n [+] Password founded:"+password+"");
    except Exception as err:
        #print(" [-] cracking ... status: failed, try password:",password)
        pass
    finally:
        threadmax.release()

def main():
    parser=optparse.OptionParser("\nUsage:\n\npython3 ZipCracker.py -f <zipfile> -d <dictionaryfile>"
                                 "\n\nDemo: python3 ZipCracker.py -f demo.zip -d dictionary.txt\n")
    parser.add_option('-f',dest='zname',type='string',help='specify zip file')
    parser.add_option('-d',dest='dname',type='string',help='specify dictionary file')
    (options,args)=parser.parse_args()
    if(options.zname==None) | (options.dname==None):
        print(parser.usage)
        exit(0)
    else:
        zname=options.zname
        dname=options.dname
    zFile=zipfile.ZipFile(zname)
    passFile=open(dname)
    for line in passFile.readlines():
        threadmax.acquire()
        password=line.strip('\n')
        t=Thread(target=extractFile,args=(zFile,password))
        t.start()

if __name__ == '__main__':
        main()
