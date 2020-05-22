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

3. mysql < Chinook_MySql_AutoIncrementPKs.sql

4. mysql -> use Chinook; -> show tables; -> desc Genre; -> tee Logfile.txt -> notee

5. source test.sql

6. select Title, Name from Album -> join Artist on Album.ArtistId = Artist.ArtistID -> limit 10;

7. insert into Genre (Name) values('Trad'); -> select last_insert_id(); -> select * from Genre where GenreId = 26;

8. update Genre set Name = 'Traditional' where Name = 'Trad';

9. delete from Genre where Name = 'Traditional';

## To get this to work...as the CI course material is unsuitable for this task.

1. wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_MySql_AutoIncrementPKs.sql

2. mysql < Chinook_MySql_AutoIncrementPKs.sql

3. mysql -> CREATE USER 'naoise'@'localhost' IDENTIFIED BY 'password'; -> GRANT ALL PRIVILEGES ON *.* TO 'naoise'@'localhost' WITH GRANT OPTION;

4. PythonMySQL.py: connection = pymysql.connect(host='localhost', user='naoise', password='password', db='Chinook')