# photogaler


#### A online Photo Gallery  , {Date Nov 28 2021}

## Description.
This is a digitalized gallery built with Django python framework.

## Check out the website

https://photogaler.herokuapp.com/
## Setup/Installation Requirements

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/sling254/photogaler
$ cd photogaler
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv name-of-the-env
$ source env/bin/activate
```
Note to use the above command that is { virtualenv} you must have virtualenv installed you can do that by:--
```sh
$ pip install virtualenv 

```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


# Behaviour Driven Development
1. Provides a dropdown button to select location
    INPUT: Click on location option
2. OUTPUT: Photos belonging to that particular location displayed in the page
    Provides a search form
3. INPUT: Category keyword entered in the search field
    OUTPUT: Photos belonging to that category is displayed in the page
4. Show photo details
    INPUT: Image is clicked
5. OUTPUT: A modal pop up with image details
    Provides a copy function for image URL
6. INPUT: Photo URL is clicked
    OUTPUT: The image link copied to machine clipboard
## Known Bugs
- There is no known bug at the time of the first release

## Technologies Used
- HTML CSS Bootsrap -- front-end
- Python-Django -- backend

## Support and contact details
- Github  --Sling254

### License
* see [License](https://github.com/sling254/photogaler/blob/main/LICENSE)  file
Copyright (c) {2021}



# Website Design :link:
* see [Website Design](https://www.figma.com/file/FkJ8zy5BR120eW0pkAN3W5/PhotoGaler?node-id=1%3A2) file


# Admin Dashboard :link:
* see [Website Design](https://www.figma.com/file/1PLCxPvvePTHQtPcYm1x2J/PhotoGaleradmin?node-id=1%3A2) file
