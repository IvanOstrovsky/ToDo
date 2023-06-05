from django.urls import path
from django.contrib import admin
from todo.views import todo
from todo.views import category
from todo.views import redirect_view
 
urlpatterns = [
	path('', redirect_view ),
	path('admin/', admin.site.urls),
	path('todo/', todo, name="todo"),
	path('category/', category, name="category"),
]