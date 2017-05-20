ps aux |grep gunicorn |grep views | awk '{ print $2 }' |xargs kill -HUP

gunicorn -w 3 -k gevent   --daemon -b 127.0.0.1:5000 application:app

