# 0x18. Webstack monitoring

![Image link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png)

## Author:
* **Noah Tsegay** <[Noaht8](https://github.com/Noaht8)>  &#128511;

## Directory Contents
___

## Task 0

Sign up for Datadog - Please make sure you are using the US website of Datadog (.com)<br>
Install ```datadog-agent``` on ```web-01```<br>
Create an ```application key```<br>
Copy-paste in your Intranet user profile your DataDog ```API key``` and your DataDog ```application key```.<br>
Your server ```web-01``` should be visible in Datadog under the host name ```XX-web-01```<br>
* You can validate it by using datadog API<br>
* If needed, you will need to update the hostname of your server

![Datadog host](Task_0.jpg)

## Task 1

### Set up a monitor that checks the number of read requests issued to the device per second.
![Read Monitor](Task_1_Read.png)

### Set up a monitor that checks the number of write requests issued to the device per second.
![Write Monitor](Task_1_Write.png)

## Task 2

### Dashboard with different metrics displayed in order to get a few different visualizations.
![Noah's Dashboard](Task_2.png)

