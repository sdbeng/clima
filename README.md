# clima
Dockerized django App to check the weather(clima).

##docker-compose up
Note: your localhost won't work here because docker has its own network so,
in order to run the server for the first time, run:

`docker-compose up`

that command will run the server with the prev command:port configured in the current docker-compose.yml file.

After that, go to settings and add 0.0.0.0 to the allowed_hosts config list.

## render home page
i can start backwards:
go to app.urls, add an entry/route to urlpatterns list, 
- prev `import include`
- path('', include('weather.urls')) #which i need to create

Then create weather/urls.py and add the corresponding path:
`path('', views.index, name='home')`
don't forget to import views


