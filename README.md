# ShLoWin
A shell to use Windows command on your Linux-on-Windows, written in Python 3

Put the `winsrv.py` file on your computer (Windows part).

Then start a bash command line :

```bash
cd # to go in your home directory
mkdir bin
cd bin
nano cwin.py
# copy and paste cwin.py
#> copy cwin.py, then right clic in nano to paste it
#> CTRL X, O, RETURN
cd
nano .profile
# change those lines :
# # set PATH so it includes user's private bin if it exists
# if [ -d "$HOME/bin" ] ; then
#     PATH="CHANGE:$PATH"
# fi
# remove CHANGE and put /home/YOURNAME/bin
#> CTRL X, O, RETURN
nano .bashrc
# add : alias python=python3
#> CTRL X, O, RETURN
source ~/.profile
source ~/.bashrc
```

Now you can type `cwin.py` everywhere, it will launch the script.

Note that you must start the server before starting `cwin.py`

Type `q` to exit

Type `w` before w windows command to send it to the server on Windows
