import os
pc_name = 'DULE' #PC NAME
def dc97(path,ext):
    for r,d,f in os.walk(path):
        for file in f:
            if ext in file:
                d=os.path.join(r,file)
                print(d)
                try:
                    if os.path.isfile(d):
                        os.remove(d)
                    else:
                        print('Fajl je ne posotji...')
                except:
                    print('Fajl ne moze da se obrise...')
        for dirr in d:
            try:
                d=os.path.join(r,dirr)
                if os.path.isdir(d):
                    os.rmdir(d)
                else:
                    print('Folder ne postoji...')
            except:
                print('Folder ne moze da se obrise...')
def dule():
    dc97('c:\\windows\\temp\\','.')
    dc97('c:\\users\\'+pc_name+'\\appdata\\local\\temp\\','.')
while True:
    dule()

                
