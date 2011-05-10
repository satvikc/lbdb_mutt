import os,sys,subprocess,time,datetime,shutil
MAILDIR=os.path.expanduser("~/Mail")
LBDB=os.path.expanduser("~/.lbdb")
FIRST_TIME=True
DAY=1

def lbdb(x):
    if not os.path.isdir(LBDB):
        os.mkdir(LBDB)
    for root,dirs,files in os.walk(x):
        if 'cur' in root:
            for f in files:
                if FIRST_TIME or (int(time.time()-os.stat(root+'/'+f).st_mtime)/(60*60*24))<=DAY:
                    subprocess.getoutput("cat "+root+'/'+f+' | '+ "lbdb-fetchaddr -a ")
    try:
        os.remove(LBDB+'/m_inmail.list.temp')
    except:
        pass
    shutil.move(LBDB+'/'+'m_inmail.list',LBDB+'/'+'m_inmail.list.temp')
    subprocess.getoutput('sort -u -d -f -i -k 1,1 '+ LBDB +'/m_inmail.list.temp > ' + LBDB+'/m_inmail.list')
    fp=open(LBDB+'/m_inmail.list.temp',"r")
    lines=fp.readlines()
    fp.close()
    tdict={}
    for l in lines:
        tdict[l[:l.index('\t')]]=l
    lines2=[]
    for key in tdict:
        lines2.append(tdict[key])
    lines2.sort()
    fp=open(LBDB+'/m_inmail.list',"w")
    fp.writelines(lines2)
    fp.close()
    os.remove(LBDB+'/m_inmail.list.temp')
if __name__=="__main__":
    lbdb(MAILDIR)
