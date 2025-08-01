# 0x00. Shell, basics

## Author: **Noah Tsegay** <[Noaht8](https://github.com/Noaht8)> 😎;

![Image link](image.jpg)

Resources
---------

**Read or watch**:

-   [What Is "The Shell"?](https://alx-intranet.hbtn.io/rltoken/vwO91sqNBgRL03BLu-ueiA)
-   [Navigation](https://alx-intranet.hbtn.io/rltoken/iblidp7yp6i-QpT8rDXHaA "Navigation")
-   [Looking Around](https://alx-intranet.hbtn.io/rltoken/xEKUCnQsMH0esQ6fJU5vLA "Looking Around")
-   [A Guided Tour](https://alx-intranet.hbtn.io/rltoken/HUhQ73fFR1GOC5nb4r-mDw "A Guided Tour")
-   [Manipulating Files](https://alx-intranet.hbtn.io/rltoken/olv-1tj4d1LA57Z0PrLNvw "Manipulating Files")
-   [Working With Commands](https://alx-intranet.hbtn.io/rltoken/zUtux3Pm0BkvtwXzbTtkmA "Working With Commands")
-   [Reading Man pages](https://alx-intranet.hbtn.io/rltoken/rddGdsqLf8_kRzp12RaD4A "Reading Man pages")
-   [Keyboard shortcuts for Bash](https://alx-intranet.hbtn.io/rltoken/JcsRq7PW6v7SdpPH_N8udQ "Keyboard shortcuts for Bash")
-   [LTS](https://wiki.ubuntu.com/LTS)
-   [Shebang](https://alx-intranet.hbtn.io/rltoken/cE8ZA3kgEaFhB-IDNv31bQ "Shebang")

**man or help**:

-   `cd` &emsp; Change directory.
-   `ls` &emsp; List files and folders in the current directory.
-   `pwd` &emsp;  Print Working Directory—shows your current path.
-   `less` &emsp;  View a file one page at a time (with scrolling).
-   `file` &emsp;  Identify the type of a file by examining its contents.
-   `ln` &emsp;  Create links (Hard link (default) or Symbolic (soft) link)
-   `cp`  &emsp; Copy files or directories.
-   `mv`  &emsp; Move or rename files or directories.
-   `rm` &emsp;  Remove (delete) files or directories.
-   `mkdir`  &emsp; Make a new directory.
-   `type`  &emsp; Tell how a command name is interpreted (builtin, alias, function, or external).
-   `which` &emsp;  Show the full path of an executable that would run.
-   `help` &emsp;  Display help for a shell builtin.
-   `man` &emsp;  View the manual (“manpage”) for a command.

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/Cn1p1E1_3FRvKpHfiKJ1GQ "explain to anyone"), **without the help of Google**:

### General

-   What does RTFM mean?
-   What is a Shebang

### What is the Shell

-   What is the shell
-   What is the difference between a terminal and a shell
-   What is the shell prompt
-   How to use the history (the basics)

### Navigation

-   What do the commands or built-ins `cd`, `pwd`, `ls` do
-   How to navigate the filesystem
-   What are the . and .. directories
-   What is the working directory, how to print it and how to change it
-   What is the root directory
-   What is the home directory, and how to go there
-   What is the difference between the root directory and the home directory of the user root
-   What are the characteristics of hidden files and how to list them
-   What does the command `cd -` do

### Looking Around

-   What do the commands `ls`, `less`, `file` do
-   How do you use options and arguments with commands
-   Understand the ls long format and how to display it
-   [A Guided Tour](https://alx-intranet.hbtn.io/rltoken/HUhQ73fFR1GOC5nb4r-mDw "A Guided Tour")
-   What does the `ln` command do
-   What do you find in the most common/important directories
-   What is a symbolic link
-   What is a hard link
-   What is the difference between a hard link and a symbolic link

### Manipulating Files

-   What do the commands `cp`, `mv`, `rm`, `mkdir` do
-   What are wildcards and how do they work
-   How to use wildcards

### Working with Commands

-   What do `type`, `which`, `help`, `man` commands do
-   What are the different kinds of commands
-   What is an alias
-   When do you use the command help instead of man

### Reading Man Pages

-   How to read a man page
-   What are man page sections
-   What are the section numbers for User commands, System calls and Library functions

### Keyboard Shortcuts for Bash

-   Common shortcuts for Bash

### LTS

-   What does `LTS` mean?

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your scripts will be tested on Ubuntu 20.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
-   All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
-   The first line of all your files should be exactly `#!/bin/bash`
-   A `README.md` file at the root of the repo, containing a description of the repository
-   A `README.md` file, at the root of the folder of *this* project, describing what each script is doing
-   You are not allowed to use backticks, `&&`, `||` or `;`
-   All your scripts must be executable. To make your file executable, use the `chmod` command: `chmod u+x file`. Later, we'll learn more about how to utilize this command.

More Info
---------

*Example of line count and first line*

```
julien@ubuntu:/tmp$ wc -l 12-file_type
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type
#!/bin/bash
julien@ubuntu:/tmp$

```

In order to test your scripts, you will need to use this command: `chmod u+x file`. We will see later what does `chmod` mean and do, but you can have a look at `man chmod` if you are curious.

*Example*

```
julien@ubuntu:/tmp$ ls
12-file_type
lll
julien@ubuntu:/tmp$ ls -la lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ cat lll
#!/bin/bash
ls
julien@ubuntu:/tmp$ ls -l lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ chmod u+x lll # you do not have to understand this yet
julien@ubuntu:/tmp$ ls -l lll
-rwxrw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ ./lll
12-file_type
lll
julien@ubuntu:/tmp$

```
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
Move the file betty from `/tmp/` to `/tmp/my_first_directory`.<br>
Example:<br>
```
$ ./7-movethatfile
$ ls /tmp/my_first_directory/
betty
$
```
## [8-firstdelete](8-firstdelete)
Delete the file `betty`.<br>
- The file `betty` is in `/tmp/my_first_directory`<br>

Example:<br>
```
$ ./8-firstdelete
$ ls /tmp/my_first_directory/
$
```
## [9-firstdirdeletion](9-firstdirdeletion)
Delete the directory `my_first_directory` that is in the `/tmp` directory.<br>
Example:<br>
```
$ ./9-firstdirdeletion
$ file /tmp/my_first_directory
/tmp/my_first_directory: cannot open `/tmp/my_first_directory' (No such file or directory)
$
```
## [10-back](10-back)
Write a script that changes the working directory to the previous one.<br>
```
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ cd /var
julien@ubuntu:/var$ pwd
/var
julien@ubuntu:/var$ source ./10-back
/tmp
julien@ubuntu:/tmp$ pwd
/tmp
```
## [11-lists](11-lists)
Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.
## [12-file_type](12-file_type)
Write a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.<br>
Example<br>
```
ubuntu@ip-172-31-63-244:~$ ./12-file_type
/tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
```
Note that depending on the file, the output of your script will be different.
## [13-symbolic_link](13-symbolic_link)
Create a symbolic link to `/bin/ls`, named` __ls__`. The symbolic link should be created in the current working directory.
```
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
ubuntu@ip-172-31-63-244:/tmp/sym$./13-symbolic_link
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
```
## [14-copy_html](14-copy_html)
Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
<br>
You can consider that all HTML files have the extension .`html`
## [100-lets_move](100-lets_move)
Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.

You can assume that the directory `/tmp/u` will exist when we will run your script
```
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 My_file
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Elif_ym
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
ubuntu@ip-172-31-63-244:/tmp/sym$ ./100-lets_move
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 My_file
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Elif_ym
```
## [101-clean_emacs](101-clean_emacs)
Create a script that deletes all files in the current working directory that end with the character `~`.
```
ubuntu@ip-172-31-63-244:/tmp/sym$ ls
main.c  main.c~  Makefile~
ubuntu@ip-172-31-63-244:/tmp/sym$ ./101-clean_emacs
ubuntu@ip-172-31-63-244:/tmp/emacs$ ls
main.c
ubuntu@ip-172-31-63-244:/tmp/emacs$
```
## [102-tree](102-tree)
Create a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.

You are only allowed to use two spaces (and lines) in your script, not more.
```
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 44 Sep 20 12:09 102-tree
julien@ubuntu:/tmp/h$ wc -l 102-tree 
2 102-tree
julien@ubuntu:/tmp/h$ head -1 102-tree 
#!/bin/bash
julien@ubuntu:/tmp/h$ tr -cd ' ' < 102-tree | wc -c # you do not have to understand this yet, but the result should be 2, 1 or 0
2
julien@ubuntu:/tmp/h$ ./102-tree 
julien@ubuntu:/tmp/h$ ls
102-tree  welcome
julien@ubuntu:/tmp/h$ ls welcome/
to
julien@ubuntu:/tmp/h$ ls -l welcome/to
total 4
drwxrwxr-x 2 julien julien 4096 Sep 20 12:11 school
julien@ubuntu:/tmp/h$
```
## [103-commas](103-commas)
Write a command that lists all the files and directories of the current directory, separated by commas (,).

- Directory names should end with a slash (/)
- Files and directories starting with a dot (.) should be listed
- The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
- Only digits and letters are used to sort; Digits should come first
- You can assume that all the files we will test with will have at least one letter or one digit
- The listing should end with a new line
```
ubuntu@ubuntu:~/$ ls -a

.  ..  0-commas  0-commas-checks  1-empty_casks  2-gifs  3-directories  4-zeros  5-rot13  6-odd  7-sort_rot13  Makefile  quote  .test  test_dir  test.var

ubuntu@ubuntu:~/$ ./103-commas

./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var

ubuntu@ubuntu:~/$
```
### Flags breakdown:
`-m` – list files comma-separated, horizontally

`-a` – show all files, including hidden ones (starting with .)

`-p` – append / to directory names to show they're folders
## [school.mgc](school.mgc)
Create a magic file `school.mgc` that can be used with the command `file` to detect `School` data files. `School` data files always contain the string `SCHOOL` at offset 0.
```
ubuntu@ip-172-31-63-244:/tmp/magic$ cp /bin/ls .
ubuntu@ip-172-31-63-244:/tmp/magic$ ls -la
total 268
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 02:44 .
drwxrwxrwt 11 root   root   139264 Sep 20 02:44 ..
-rw-r--r--  1 ubuntu ubuntu    496 Sep 20 02:42 school.mgc
-rwxr-xr-x  1 ubuntu ubuntu 110080 Sep 20 02:43 ls
-rw-rw-r--  1 ubuntu ubuntu     50 Sep 20 02:06 thisisaschoolfile
-rw-rw-r--  1 ubuntu ubuntu     30 Sep 20 02:16 thisisatextfile
ubuntu@ip-172-31-63-244:/tmp/magic$ file --mime-type -m school.mgc *
school.mgc:         application/octet-stream
ls:                    application/octet-stream
thisisaschoolfile: School
thisisatextfile:       text/plain
ubuntu@ip-172-31-63-244:/tmp/magic$ file -m school.mgc *
school.mgc:         data
ls:                    data
thisisaschoolfile: School data
thisisatextfile:       ASCII text
ubuntu@ip-172-31-63-244:/tmp/magic$
```

### Creating the magic file
1. create a plain text file called `school` with the contents
```
0 string SCHOOL School data
```
2. Then compile it into a magic file with:
```
file -C -m school
```
`0` → The offset in the file (in bytes). This means: look at byte 0, the very start of the file.

`string` → The data type to check for at that offset. In this case, a plain ASCII string.

`SCHOOL` → The expected value found at that offset. If the file starts with this exact string, it matches.

`School data` → The description to display if the file matches. This is what file will output.

