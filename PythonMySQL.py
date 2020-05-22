import os
import pymysql

# Get username from GtiPod
username = os.getenv("GITPOD_GIT_USER_NAME")
print(username)
