# t1ru
school management system

### Steps for starting application
1. Clone this project and change directory to be `t1ru`.

        $ cd t1ru/
   
2. Update python pip to the current version

        $ python -m pip install --upgrade pip
   
3. Install virtualenv

        $ pip install virtualenv
     
4. Create virtual environment directory using this command.

        $ virtualenv venv

5. Activate virtual environment due to your os.

   For Window:
    
        $ venv\Scripts\activate
        
    For Mac/Linux:
    
        $ source venv/bin/activate

6. Install modules in [requirements.txt](requirements.txt) using 
  
        $ pip install -r requirements.txt
        
7. Use mysite/sample.env as a template, then create/edit your own
.env file and set their values.

       DEBUG=True
       TEMPLATE_DEBUG=True
       SECRET_KEY=Your-Secret-Key

        
   * You can login to t1ru by creating a super user
     follow to the instruction in Note below

8. Create initial migration, then apply the change 
       
       $ python manage.py makemigrations
       $ python manage.py migrate
       
9. Run this command to run the server

       $ python manage.py runserver
       
Note!:

* When finished running server, deactivate virtual environment using this command

    ```$ deactivate```
    
* To create super user

    ```$ python manage.py createsuperuser```
