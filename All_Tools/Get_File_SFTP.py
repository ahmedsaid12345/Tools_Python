import pysftp

Hostname = "10.28.1.18"
Username = "root"
Password = "rooter"

with pysftp.Connection(host=Hostname, username=Username, password=Password) as sftp:
    print("Connection successfully established ... ")

# Define the remote path where the file will be uploaded
    remoteFilePath = '/tl3010/var/log/'

# Define a file that you want to upload from your local directorty
    localFilePath = 'C:/Users/m.ali/Shaheen-Elsour_1/'

# Use get method to download a file
    sftp.get(remoteFilePath, localFilePath)