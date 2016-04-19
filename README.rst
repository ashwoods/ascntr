
ASCNTR- Another Simplfied Cron Next Task Reader
===============================================

ASCNTR is a small command line utility that can read a ASC File and output the next time
 of execution of the each command.


Install
-------

Install into your python environment of choice using pip from the parent folder:

pip install -e ./


Usage
-----

Invoke the command by piping a config:

cat /path/to/config | ascntr CURRENT_TIME [HH:SS]


