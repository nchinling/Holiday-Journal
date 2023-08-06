# Holiday Journal

This is the repository for the "Holiday Journal" project, where users can create and manage their travel destinations and journal entries.

## Distinctiveness


## Complexity


## Features

- [x] User registration form
- [x] SQL database using four models: `Destination`,`City`,`Photo`,`MapImage`
- [x] User authentication: login and logout functionality
- [x] Edit functionality for destinations
- [ ] Implemented search functionality based on city
- [ ] ...

## Description of each file


## How to run the application

## Project Progress

### 18 Jul

- Created a basic working form for users to submit their travel destinations and journal entries.
- Set up the SQL database with two models: `Destination` to store destination details and `City` to store city names.
- Implemented user authentication with login and logout functionality.

### 19 Jul

- Added the edit functionality, allowing users to update their travel destinations.
- Added in photo upload, allowing users to upload photos.

### 20 Jul

- Added multiple image upload
- Displayed images at index page
- Implemented Lightbox.js
- implemented multiple images upload and deletion
- attempted new user registration

### 21 Jul

- Created new user registration page
- Lightbox for all pages with images
- Stylised form
- Stylised index page
- Implemented delete journal entry
- Implemented leaflet.js map
- Implement my destinations page

### 22 Jul

- Implemented Geocode
- Labels and Zoom level for Geocode


### 23 Jul

- Saved Geocoded image in SQL and displayed it
- Created post filter




## How to Use

1. Clone the repository: `git clone https://github.com/your_username/holiday-journal.git`
<!-- 2. Install the required dependencies: `pip install -r requirements.txt` -->
3. Set up the database: `python manage.py migrate`
4. Run the development server: `python manage.py runserver`
5. Access the application in your web browser at `http://localhost:8000/`

