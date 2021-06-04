cd /usr/bin
wget https://raw.githubusercontent.com/nerdthatnoonelikes/gameoflife-py/master/main.py
sudo mv main.py gameoflife
sudo chmod +x ./gameoflife
sudo chown $USER ./gameoflife

echo "Installed successfully"