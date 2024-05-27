# Meta Back-End Developer Capstone

## MySQL installation on Mac with homebrew

`$ brew install mysql`

## To activate virtual environment inside the directory

`$ pipenv shell`

## To install dependencies

`$ pipenv install django`  
`$ pipenv install djangorestframework`  
`$ pipenv install djoser`  
`$ pipenv install mysqlclient`
  
----------------------------------------------------------------------------

## Install MySQL and create a database and user for the project

login to mysql

`$ mysql -u root -p`

`$ create database littlelemon;`

`$ CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!';`

`$ GRANT ALL PRIVILEGES ON littlelemon.* TO 'admindjango'@'localhost';`

exit mysql

----------------------------------------------------------------------------

## Apply migration commands

`$ python3 manage.py makemigrations`

`$ python3 manage.py migrate`

## To run server

`$ python3 manage.py runserver`

## Go to url homepage "http://localhost:8000/api/menu/". Success!


## API endpoints to test
| Description           | Method | Path                       |
|-----------------------|--------|----------------------------|
| Load static home page | GET    | /api/menu/                 |
| View menu items       | GET    | /api/menu/items/           |
| View single menu item | GET    | /api/menu/items/<<int:pk>> |
| Add a menu item       | POST   | /api/menu/items/           |
| Update a menu item    | PUT    | /api/menu/items/<<int:pk>> |
| Delete a menu item    | DELETE | /api/menu/items/<<int:pk>> |
| Obtain authtoken      | POST   | /api/menu/api-token-auth/  |
| View table bookings   | GET    | /api/booking/              |


