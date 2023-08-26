# registertration
# step 1 create virtual enverment
    
# step 2 activate virtual env
# step 3 run requerment.txt file
    pip install -r requirements.txt
# step 4 migrate table 
      python manage.py migrate
# step 5 run django server
    python manage.py runserver
# step 6 run celary
  celery -A ezyschoolingtask worker --loglevel=info
# step7 make sure redis server in running condition
  redis-server
# step8 call api url
  http://localhost:8000/register/
# step 9 call using front end
  http://localhost:8000/
