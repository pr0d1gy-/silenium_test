# [Instagram test] #

**Before cloning** the project - make sure that you have installed all of the packages.

`sudo apt-get install -y build-essential g++ git python3.5 python3.5-dev python3-psycopg2 libxml2-dev python3-pip libffi-dev`

You need to install `Chrome` for run Chrome browser. Follow the instruction by this [LINK](https://askubuntu.com/questions/79280/how-to-install-chrome-browser-properly-via-command-line). Also you can try to use application with virtual display if you working on the server: `xvfb`. 

And clone the repo.

**After cloning** the repo you must setup environment in project dir.

Enter in you bash shell: `virtualenv .env -p /usr/bin/python3.5`.

Activate the environment `source .env/bin/activate`.

Next you must install requirement libraries: `pip3 install -r requirements.txt`.

Make execute permission for the `main.py` python file: `chmod +x main.py`.

Now you can execute application: `./main.py -h`.
