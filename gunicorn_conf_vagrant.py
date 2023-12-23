preload = True
timeout = 120
worker_class = 'uvicorn.workers.UvicornWorker'
bind = '0.0.0.0:8000'

# Logging Options
loglevel = 'debug'
accesslog = '/vagrant/workspaces/osiconl/osiconl/logs/access.log'
errorlog = '/vagrant/workspaces/osiconl/osiconl/logs/error.log'

capture_output = True
