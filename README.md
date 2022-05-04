# Create new APP (a.k.a Component, Module)
- `py manage.py startapp "name of the APP"`
- add newly created app to `INSTALLED_APPS`in pytoolbox/settings.xml
  - create urls.py in newly created app
    - content (make sure you created the view which will be handled from this uri): 
    - ```python
      from . import views
      
      urlpatterns = [
        path('', views.index, name='index'),
      ]
      ```
  - update the pytoolbox/urls.py with newly created urls.py file
    - ````python
          path('calculator/', include('<name of your app>.urls')),
      ````
