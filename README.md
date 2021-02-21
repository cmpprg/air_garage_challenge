# Lowest Rated Parking Lots Coding Challenge

Thes Instructions will be for MacOS
## Prerequisites:
- [>=npm 7.5.3](https://www.npmjs.com/get-npm)
- [>=Python 3.7.7](https://www.python.org/downloads/release/python-377/)
  - This is the version I built the project with. If you use this version or greater you should be good.

## Setup:
- Please open your terminal and clone down the project
```
git clone git@github.com:cmpprg/air_garage_challenge.git
```
  - __Alternatively__, if you don't have SSH setup on your Github
```
git clone https://github.com/cmpprg/air_garage_challenge.git
```
- navigate into folder structure
```
cd air_garage_challenge
```
<br />

### React
- Navigate into the _bad-parking_ folder
```
cd bad-parking
```
- Install all necessary packages
```
npm install
```
- Start the development server
```
npm start
```

### Django
- First you must open a new tab using _cmd+t_, this should open a tab in the same terminal location
- Navigate to _bad_parking_be_ folder
```
cd ../bad_parking_be 
```
- Create new python environment 
```
python3 -m venv .env
```
- Activate python environment
```
source .env/bin/activate
```
- Install all necessary dependencies
```
pip install -r requirements.txt
```
- Start local Django Server
```
python manage.py runserver
```
<br />

### If it is not already open you should now be able to go to [http://localhost:3000/](http://localhost:3000/), put in your location, submit and see results. It's not the most beautiful things, but it gets the job done.
