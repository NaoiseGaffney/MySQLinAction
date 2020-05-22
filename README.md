AWS Cloud9 or Gitpod

In AWS Cloud9 or Gitpod, the command to start the MySQL console is simpler than in the old version of Cloud9. Use the following command instead:
> sudo mysql in AWS Cloud9
>
> mysql in Gitpod
>
The following command will create the correct user in the database and allow you to follow what is in the video:
`wget https://raw.githubusercontent.com/Code-Institute-Org/mysql-fix/master/createuser.sh && source ./createuser.sh`
This video will be updated in due course.

1. mysql -> show databases; -> quit

2. wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_MySql_AutoIncrementPKs.sql

3. sudo mysql < Chinook_MySql_AutoIncrementPKs.sql

4. mysql -> use Chinook; -> show tables;