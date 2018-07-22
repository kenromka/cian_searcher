# cian_searcher
Search for new flats with criterias
***
## Info
The program is made for **private purposes**.
It searches for new rental housing variants with the certain criterias cian.ru has and sends these links to some vk users
***
## Usage
Write down the following info to "cian_info.txt" (there's an example in the current folder):
  * *1st line*: first part of the link to the saved page with search criterias (finishing with "p=")
  * *2nd line*: remaining part of the appropriate link
  * *3rd+ lines*: usernames' domains in vk.com (who should get messages about changes in the list of flats). domain per line

If there are variants of flats already watched, add their quantity and their links to "cian_flats.txt" (number/link per line).

Run this program and wait for notifications:)

P.S. if program works OK, terminal's output will be in "Updated on: %time%" format.
***
## TO_DO
1) make code pretty
2) add comments
3) add vk api error handling
***
## Authors
  * [Roman Kenig](https://github.com/kenromka)
