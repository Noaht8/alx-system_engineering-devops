# 0x00. Shell, basics

![Image link](image.jpg)

## Author:
* **Noah Tsegay** <[Noaht8](https://github.com/Noaht8)> 😎;

## Repo Contents
___
## [0-current_working_directory](0-current_working_directory)
This repository contains the following files:<br>
Write a script that prints the absolute path name of the current working directory.<br>
Example:
```
$ ./0-current_working_directory
/root/alx-system_engineering-devops/0x00-shell_basics
$
```
## [1-listit](1-listit)
Display the contents list of your current directory.<br>
Example:
```
$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
$
```
## [2-bring_me_home](2-bring_me_home)
Write a script that changes the working directory to the user’s home directory.<br>
You are not allowed to use any shell variables<br>
```
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ echo $HOME
/home/julien
julien@ubuntu:/tmp$ source ./2-bring_me_home
julien@ubuntu:~$ pwd
/home/julien
julien@ubuntu:~$
```
## [3-listfiles](3-listfiles)
Display current directory contents in a long format<br>
Example:<br>
```
$ ./3-listfiles
total 32
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
$
```
## [4-listmorefiles](4-listmorefiles)
Display current directory contents, including hidden files (starting with .). Use the long format.<br>
Example:<br>
```
$ ./4-listmorefiles
total 32
drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
$
```
## [5-listfilesdigitonly](5-listfilesdigitonly)
Display current directory contents.<br>
- Long format<br>
- with user and group IDs displayed numerically<br>
- And hidden files (starting with .)<br>
Example:<br>
```
$ ./5-listfilesdigitonly
total 32
drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
-rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
$
```
## [6-firstdirectory](6-firstdirectory)
Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.<br>
Example:<br>
```
$ ./6-firstdirectory
$ file /tmp/my_first_directory/
/tmp/my_first_directory/: directory
$
```
## [7-movethatfile](7-movethatfile)
## [8-firstdelete](8-firstdelete)
## [9-firstdirdeletion](9-firstdirdeletion)
## [10-back](10-back)
## [11-lists](11-lists)
## [12-file_type](12-file_type)
## [13-symbolic_link](13-symbolic_link)
## [14-copy_html](14-copy_html)
## [100-lets_move](100-lets_move)
## [101-clean_emacs](101-clean_emacs)
## [102-tree](102-tree)
## [103-commas](103-commas)
## [school.mgc](school.mgc)
|File| Description|
|:-------|:-------|
|[0-current_working_directory](0-current_working_directory)| script that prints the absolute path name of the current working directory|
|[1-listit](1-listit)| Display the contents list of your current directory|
|[2-bring_me_home](2-bring_me_home)| Script that changes the working directory to the user’s home directory|
|[3-listfiles](3-listfiles)| Display current directory contents in a long format|
|[4-listmorefiles](4-listmorefiles)| Display current directory contents, including hidden files (starting with .). Use the long format|
|[5-listfilesdigitonly](5-listfilesdigitonly)| Display current directory contents<br><li>Long format<br><li>with user and group IDs displayed numerically<br><li>And hidden files (starting with .)|
|[6-firstdirectory](6-firstdirectory)| Script that creates a directory named my_first_directory in the /tmp/ directory|
|[7-movethatfile](7-movethatfile)| Move the file betty from /tmp/ to /tmp/my_first_directory|
|[8-firstdelete](8-firstdelete)| Delete the file betty<br><li>The file betty is in /tmp/my_first_directory|
|[9-firstdirdeletion](9-firstdirdeletion)| Delete the directory my_first_directory that is in the /tmp directory|
|[10-back](10-back)| Write a script that changes the working directory to the previous one|
|[11-lists](11-lists)| Script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.|
|[12-file_type](12-file_type)| Script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script|
|[13-symbolic_link](13-symbolic_link)| Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory|
|[14-copy_html](14-copy_html)| Script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.|
|[100-lets_move](100-lets_move)| Script that moves all files beginning with an uppercase letter to the directory /tmp/u|
|[101-clean_emacs](101-clean_emacs)| Script that deletes all files in the current working directory that end with the character ~|
|[102-tree](102-tree)| Script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory|
|[103-commas](103-commas)| Command that lists all the files and directories of the current directory, separated by commas (,)<br><li>Directory names should end with a slash (/)<br><li>Files and directories starting with a dot (.) should be listed<br><li>The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning<br><li>Only digits and letters are used to sort; Digits should come first<br><li>You can assume that all the files we will test with will have at least one letter or one digit<br><li>The listing should end with a new line|
|[school.mgc](school.mgc)| A magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0<br><li>Contents of the magic file: `0 string SCHOOL School data`|

