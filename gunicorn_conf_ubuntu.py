preload = True
timeout = 120
worker_class = 'uvicorn.workers.UvicornWorker'
bind = '0.0.0.0:8000'

# Logging Options
loglevel = 'debug'
accesslog = '/home/ubuntu/workspaces/osiconl/osiconl/logs/access.log'
errorlog = '/home/ubuntu/workspaces/osiconl/osiconl/logs/error.log'

capture_output = True
