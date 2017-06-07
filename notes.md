# OpenRA analysis

> we have a lot of potentially interesting info in our master sqlite database, but no proper ways to visualise or mine it.  It would be awesome if you could write a jupyter notebook that pulled out some useful stats, and then if that works out we could pull out the popular (not necessarily the same as useful!) stats into a script that runs on a cron job to output a json file that we can then plot as part of http://www.openra.net/players/

> There are two main tables with the most interesting data:

> `finished`: holds the records of completed multiplayer matches.  From this it would be good to get a handle on the most popular servers partitioned by mod and host (people usually host multiple on one machine or multiple vms with similar ips), and something like the most popular maps this week / month / release would be great for the public stats page.  Info on a map can be queried from its id using http://resource.openra.net/map/hash/<map hash>.

> `sysinfo` holds all the data from our system information survey.  The boring but most useful stuff would be to aggregate stats on mono/.net and GL versions, plus screen resolutions and display scales. Will need to do some ugly parsing to get just the useful parts out of the version strings.  The OS share would be another good stat for the players page, as well as the number of people who have launched the game in the last <time>.

* Integrate stats from github

## Previous work

Stats are only available when users submit information, which is what we have.

* OS split (windows/mac/linux)
* Cumulative number of players
* Language settings
* Most popular mod
* Most popular mod by language setting
* Most popular map
* Match length

vim: ft=markdown:tw=0:wrap
