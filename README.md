# Holiday Journal

Holiday Journal is a platform that enables travel enthusiasts to embark on an unforgettable journey of memories and exploration. Designed with a deep understanding of the traveler's heart, it enables users to cherish and share their most cherished moments from around the globe. Whether you've roamed the bustling markets of Marrakech or wandered through the serene landscapes of Kyoto, this platform preserves the magic of your journeys.

## Distinctiveness and Complexity

- Unleash Your Travel Stories:

Holiday Journal empowers users to create captivating travel journals for each city they visit. Every location holds a unique place in the users' heart which can be captured with rich, descriptive journal entries.

- Captivating Visuals:

Users can complement their journals with a stunning array of photographs. The images are elegantly displayed with the support of the Lightbox JavaScript library, which creates an immersive album-like experience. The image files are stored in the project media folder, while the path directories are stored in a SQL model.

- City Maps for Every Journal Entry:

City maps are automatically generated using Leaflet and its image plugin. The application generates maps for each holiday journal entry. These maps help uses reminisce about their journeys and allows them to visualise their adventures alongside other entries.

- A Journey Through Memories:

Filter through personal holiday entries to relive those happy moments. The platform makes it easy for users to embark on a nostalgic journey through their travel stories.

- Inspire Future Adventures:

Users can seek inspiration for their next holiday. The search field allows users to explore new destinations effortlessly which have been posted by other users. 

- Seamless User Experience:

Alongside an intuitive and visually appealing design, the application offers essential features like new user registration, login, and logout functionality. Users can also edit and delete their journal entries, ensuring that every memory is captured just the way they want.

## Description of each file
- add.html
For users to add holiday journal entries. Users may add images. A map of the city visited is automatically generated as well. 

- destination.html
For users to view the details of the holiday journal entry. The entry owner may edit the journal. (edit button will be made visible). The images are complemented with Lightbox. 

- edit.html
For entry owners to edit the content of their holiday journal. Users can also delete the entry on this page. 

- index.html
The main page which displays all entries. Each entry contains the country, city, date visited, date posted, holiday photos and city map. 

- layout.html
Template page

- login.html
User login page. (requires username and password)

- register.html
New user registration page

- static folder
Contains images for map markers and lightbox buttons. It also contains javascript libraries and the app CSS file. 

- admin.py
for admin page management.

- forms.py
This code contains a class called NewUserForm, which is used for user registration on a web application. The form extends Django's UserCreationForm. 

- models.py
Has four models; Destination, City, Photo and MapImage

- urls.py
Holds the code for urlpatterns

- views.py
It houses the codes which implements the features of the web application. They are new user registration, index page redirection, destination page redirection, personal page filter, filter by city / country, login, logout, edit, delete photo, delete destination and add destination. 

- holiday folder
Contains the files of the root project 

- media folder
Contains images uploaded by users

- node_modules
To house javascript libraries

- requirements.txt
Not used



## How to run the application
1. Clone the repository: `git clone https://github.com/your_username/holiday-journal.git`
2. Set up the database: `python manage.py migrate`
3. Run the development server: `python manage.py runserver`
4. Access the application in your web browser at `http://localhost:8000/`
<!-- 2. Install the required dependencies: `pip install -r requirements.txt` -->

