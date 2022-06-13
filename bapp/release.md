### from local machine
push to production branch


### on remote machine
> git pull origin production && pkill gunicorn &&  gunicorn --bind 0.0.0.0:8000 --name riphah --workers=1 bapp.wsgi --deamon --reload