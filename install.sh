#!/usr/bin/sh

sudo curl https://raw.githubusercontent.com/nerdthatnoonelikes/gameoflife-py/master/main.py -o /usr/bin/gameoflife
sudo chmod a+rx /usr/bin/gameoflife

echo "Installed Successfully"
