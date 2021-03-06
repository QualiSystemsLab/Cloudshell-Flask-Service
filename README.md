# Cloudshell Flask Service
- Python Flask sample running as a windows service. 
- The general use case is to have a simple utility server to accept HTTP requests from emails or other clients and run custom api operations against cloudshell
- the example code included shows outputting cloudshell blueprint data per domain
    - run flask server
    - navigate to `http://localhost:8900` to test sanity
    - navigate to `http://localhost:8900/<domain>` to see blueprints listed per domain

### Requirements.txt
  * pywin32, flask, waitress
  * Python 3.7.1 

### Run Flask in debug
- install python requirements
- run `python myapp.py`

### To Create Windows Service
  * Pip Install Requirements to python environment (version 3.7.1)
  * Add path of python executable and pywin32_system32 package to **System** environment Variables (not just user variables)
  - C:\Users\Administrator\AppData\Local\Programs\Python\Python37
  - C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\pywin32_system32
  * In service class,  modify  name, display name, and description
  * admin cmd open
  * service install: `python service_name.py install`
  * check service: `sc query svc_name`
  * update service: `python service_name.py update`
  * Start service: `sc start svc_name` or `python service_name.py start`
  * Stop service: `sc stop svc_name` or `python service_name.py stop`
  * If you want to delete this service: `sc delete svc_name`

### Reference Links
- https://www.thepythoncorner.com/2018/08/how-to-create-a-windows-service-in-python/
- https://gist.github.com/ddelpero/7812e1baac86733fe61dea1c3350cd1f
- https://stackoverflow.com/questions/41200068/python-windows-service-error-starting-service-the-service-did-not-respond-to-t