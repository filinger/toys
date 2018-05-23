# toys

## Pre-requisites
This project uses mostly standard libraries, here's the checklist:
* Python 3
  * sqlite3
  * bottle

### Installation
To install `bottle` simply run `pip3 install bottle`.

## Server
Web server can be launched by running Python interpreter against **server.py**:
`python3 server.py`. 
This will also populate database with a sample dataset for the sake of demo.

## App
Web application has simple GUI written in *HTML5* + *Bootstrap4*.
It can be accessed by <http://localhost:8080> after launching the **Server**.
It has three pages: **Add**, **Select** and **Result**.

#### Add
This page allows to add new toys to the database.

#### Select
Here you can query toys with specified parameters.

#### Result
This page is a simple table where rows correspond to selected toys.

## Database
All data is written into SQLite database file: `db/toys.db`.
To start anew simply delete the file.
