# The Project & Goal #

This project is a full-stack blog that was built with Python using the Django library and framework. The blog has a couple main features: 

1. Data/Post CRUD
2. User authentication
3. Filter by Tags, Author, and Title
4. Admin page to manage tags and posts
5. Deployment through Railway

The tags and posts are created using the Django models.

# Development Process #

The first task was to create the models, as the rest of the project would revolve around them, given the Django framework. Once the models and their respective attributes were defined, I then worked in order of importance, starting with the list view ('/' path), as well as the admin page to create tags, as well as manually delete posts. Next, I added base.html - the file that the rest of the html files would extend. Then I added basic CRUD operations for the psots as well as started the authentication for users login. I then returned to the list view to add filtering, and fixed issues with the authentication that would have allowed any user to edit a post. Finally, I deployed it to Railway.

# How to run locally #

    ```git clone https://github.com/maxrcobl/tamid-blog```
    ```cd tamid-blog```
    ```python -m venv venv```
    ```venv\Scripts\activate```
    ```pip install -r requirements.txt```
    ```python manage.py migrate```
    ```python manage.py runserver```

# Challenges in the process #

1. URL Recursion error
    blog/urls/py was including itself which cause infinite recursion and crashed the server
2. Queryset filtering bug
    When filtering posts, calling queryset.filter(...) the queryset had to be reassigned to ensure that the selections are applied
3. Product Migrations
    After deploying to Railway, the app crashed with a 500 error because the databse tables didn't exist yet

# Future Improvements #

Given more time, I would have liked to implement:

1. Profile views for each user
2. Detailed text editor (WYSIWYG) using a service such as Quill
3. More detailed UI and robust login system