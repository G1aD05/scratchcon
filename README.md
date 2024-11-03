# scratchcon
## How to use
**First, run this command in your terminal (make sure you have a venv activated): `python3 -m pip install scratchcon`**\
**Then create a python file and type:**
```python
import scratchcon as con

conn = con.conn.Connect()
```

**This sets up the connection class, here are some things you can connect:**
```python
# Connect a project
conn.conect_project() # Enter the project ID as an integer

# Connect a studio
conn.connect_studio() # Enter a studio ID as an integer

# Connect a user
conn.connect_user() # Enter the username as a string
```
**Here are some things you can do with the `connect_project` function:**
```python
project = con.project.Project()

project.get_title() # Returns the title of the project

project.get_description() # Returns the description of the project

project.get_instructions() # Returns the instructions of the project

project.get_author() # Returns the author of the project

project.get_author_id() # Returns the author's id

project.get_creation_date() # Returns the creation date of the project

project.get_share_date() # Returns the share date of the project

project.get_love_count() # Returns the love count of the project

project.get_view_count() # Returns the view count of the project

project.get_favorite_count() # Returns the favorite count of the project

project.get_remix_count() # Returns the remix count of the project

project.get_remixes() # Returns all the remixes of the project in a list
```

**Here are some things you can do with the `connect_studio` function:**
```python
studio = con.studio.Studio()

studio.get_description() # Returns the description of the studio

studio.get_curators() # Returns a list of all the curators in the studio

studio.get_title() # Returns the title of the studio

studio.get_creation_date() # Returns the creation date of the studio

studio.get_project_amount() # Returns the amount of projects in the studio

studio.get_follower_amount() # Returns the amount of followers of the studio

studio.get_managers() # Returns a list of managers in the studio

studio.get_comment_amount() # Returns the amount of comments

studio.get_comments() # Returns a list of comments in the studio

studio.get_projects() # Returns a list of projects in the studio

studio.get_activity() # Returns a list of the activity in the studio
```

**Here are some things you can do with the `connect_user` function**
```python
user = con.user.User()

user.get_status() # Returns the status of the user

user.get_message_count() # Returns the message count of the user

user.get_id() # Returns the ID of the user

user.get_bio() # Returns the bio of the user

user.get_country() # Returns the country of the user

user.get_username() # Returns the username of the user

user.get_join_date() # Returns the join date of the user

user.is_st() # Returns if the user is scratch team
```

## Requirements
```
Python 3
requests
```
