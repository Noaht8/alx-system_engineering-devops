# 0x02. Shell, I/O Redirections and filters

![Image link](https://blog.eduonix.com/wp-content/uploads/2015/09/Linux-Shell-Scripting-11.png)

## Author:
* **Noah Tsegay** <[Noaht8](https://github.com/Noaht8)>  &#128511;



## Contents
___

This repository contains the following files:

|File| Description|
|:---------|:---------|
|[0-hello_world](0-hello_world)| Script that prints “Hello, World”, followed by a new line to the standard output|
|[1-confused_smiley](1-confused_smiley)| Script that displays a confused smiley "(Ôo)'|
|[2-hellofile](2-hellofile)| Display the content of the /etc/passwd file.|
|[3-twofiles](3-twofiles)| Display the content of /etc/passwd and /etc/hosts|
|[4-lastlines](4-lastlines)| Display the last 10 lines of /etc/passwd|
|[5-firstlines](5-firstlines)| Display the first 10 lines of /etc/passwd|
|[6-third_line](6-third_line)| Script that displays the third line of the file iacta|
|[7-file](7-file)| Script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line|
|[8-cwd_state](8-cwd_state)| Script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it|
|[9-duplicate_last_line](9-duplicate_last_line)| Script that duplicates the last line of the file iacta|
|[10-no_more_js](10-no_more_js)| Script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders|
|[11-directories](11-directories)| Script that counts the number of directories and sub-directories in the current directory<br><li>The current and parent directories should not be taken into account<br><li>Hidden directories should be counted|
|[12-newest_files](12-newest_files)| Script that displays the 10 newest files in the current directory<br>Requirements:<br><li>One file per line<br><li>Sorted from the newest to the oldest|
|[13-unique](13-unique)| Script that takes a list of words as input and prints only words that appear exactly once<br><li>Input format: One line, one word<br><li>Output format: One line, one word<br><li>Words should be sorted|
|[14-findthatword](14-findthatword)| Display lines containing the pattern “root” from the file /etc/passwd|
|[15-countthatword](15-countthatword)| Display the number of lines that contain the pattern “bin” in the file /etc/passwd|
|[16-whatsnext](16-whatsnext)| Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd|
|[17-hidethisword](17-hidethisword)| Display all the lines in the file /etc/passwd that do not contain the pattern “bin”|
|[18-letteronly](18-letteronly)| Display all lines of the file /etc/ssh/sshd_config starting with a letter<br><li>include capital letters as well|
|[19-AZ](19-AZ)| Replace all characters A and c from input to Z and e respectively|
|[20-hiago](20-hiago)| Script that removes all letters c and C from input|
|[21-reverse](21-reverse)| Script that reverse its input|
|[22-users_and_homes](22-users_and_homes)| Script that displays all users and their home directories, sorted by users<br><li>Based on the the /etc/passwd file|
|[100-empty_casks](100-empty_casks)| Command that finds all empty files and directories in the current directory and all sub-directories<br><li>Only the names of the files and directories should be displayed (not the entire path)<br><li>Hidden files should be listed<br><li>One file name per line<br><li>The listing should end with a new line<br><li>You are not allowed to use basename, grep, egrep, fgrep or rgrep|
|[101-gifs](101-gifs)| Script that lists all the files with a .gif extension in the current directory and all its sub-directories<br><li>Hidden files should be listed<br><li>Only regular files (not directories) should be listed<br><li>The names of the files should be displayed without their extensions<br><li>The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)<br><li>One file name per line<br><li>The listing should end with a new line<br><li>You are not allowed to use basename, grep, egrep, fgrep or rgrep|
|[102-acrostic](102-acrostic)| Script that decodes acrostics that use the first letter of each line<br><li>The ‘decoded’ message has to end with a new line<br><li>You are not allowed to use grep, egrep, fgrep or rgrep|
|[103-the_biggest_fan](103-the_biggest_fan)| Script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests<br><li>Order by number of requests, most active host or IP at the top<br><li>You are not allowed to use grep, egrep, fgrep or rgrep|
