import pysftp as sftp
import re
import math
import sys

from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, UnknownLength





def progressbar_1(x, y):
    ''' progressbar for the pysftp
    '''
    bar_len = 60
    filled_len = math.ceil(bar_len * x / float(y))
    percents = math.ceil(100.0 * x / float(y))
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    filesize = f'{math.ceil(y/1024):,} KB' if y > 1024 else f'{y} byte'
    sys.stdout.write(f'[{bar}] {percents}% {filesize} {x} / {y}\r')  #{x} /{y}
    sys.stdout.flush()


#FTP_HOST_1 = "10.28.1.14"
FTP_USER = "root"
FTP_PASS = "rooter"

cnopts = sftp.CnOpts()
cnopts.hostkeys = None


Names_OF_SITES=[#'Zordozy'
                #,'GAMAL'
                #,'Ebn_Elfared'
                #,'Shaheen_Police'
              #,'Shaheen_Elsour'
               'Crstal'
                ]


List_of_IPS=[#'10.28.1.26'
             #,'10.28.1.14'   
             #,'10.28.0.174'   
             #,'10.28.1.22'
             #,'10.28.1.18'   
            '10.121.34.234'
                ]                

Types_of_Network=['plc','rf1','rf2']
#Real_Name_Onsite=['plc','rf1','kpi_rf2']
for FTP_HOST,site_name in zip(List_of_IPS,Names_OF_SITES):
    print("")
    print("............................................................")
    print(".................Pls Wait Trying to Connect.............%s:%s "%(FTP_HOST,site_name))
    print("............................................................")
    with sftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp_1:
        print("Connection succesfully stablished ...%s:%s "%(FTP_HOST,site_name))
        sftp_1.cwd('/tl3010/var/log/')  # Switch to a remote directory
   #directory_structure = sftp.listdir_attr() # Obtain structure of the remote directory
        for Network_Type in Types_of_Network:
            
            #Filter Rf1 Rf2 from Download
            if (((Network_Type == 'rf1' ) or (Network_Type == 'rf2')) and site_name == 'Shaheen_Elsour'):
                continue
    
            # Filter Plc File From Download to other sites. 
            if ((Network_Type == 'plc' ) and site_name != 'Shaheen_Elsour'):
                continue
            # Filter RF2 For Ebn_Elfared
            if ((Network_Type == 'rf2' ) and site_name == 'Ebn_Elfared'):
                continue
            
            print(".....................Downloading...............%s..%s"%(site_name,Network_Type))
           # size_file_1=[]
            size_file= sftp_1.lstat('/tl3010/var/log/kpi_'+Network_Type+'.log')
            print(size_file.st_size)
            #size_file_1 = re.findall(r'\d+', str(size_file))
            #print("file_size"+str(size_file)+"\nsize_file_1:")
           # print(size_file_1[3])
            sftp_1.get('/tl3010/var/log/kpi_'+Network_Type+'.log','C:/Users/m.ali/All_Sites/'+site_name+'/kpi_'+Network_Type+'.txt',callback=lambda x,y: progressbar_1(x,y))
            #################################
    
    
    sftp_1.close()  #Close the connection to open New Connection For New Site

#for attr in directory_structure:
 #  print(attr.filename, attr)


print('***********************************************')
print('|                      DONE                     ')
print('***********************************************')








