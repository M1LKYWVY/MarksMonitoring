# MarksMonitoring
Telegram bot which allows you to have your marks ready at hand.

Scraping data from [de.ifmo](https://de.ifmo.ru/) using [selenium webdriver](http://selenium-python.readthedocs.io/).

Program uses single-file no-sql data base [vedis](https://github.com/coleifer/vedis-python) instead of .json files.

##

### Install dependencies

```sh
python -m pip install -r requirements.txt
```
or in case lack of rules
```sh
sudo python -m pip install -r requirements.txt
```

### Build

```sh
pyinstaller --onefile main.py
```

### Run

```sh
main.exe
```

##

### Features

* file "configs.ini" should be located in the same directory as .pyz package. 

* file "database.vdb" should be located in the same directory as .pyz package.

##

### configs.ini

file stores information about token of telegram bot. Token can be received from [BotFather](https://t.me/BotFather).

### database.vdb

file is a single-file no-sql data base. Used to store information about users in .json format.

