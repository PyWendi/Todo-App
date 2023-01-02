from django.urls import path
from . import views as v

app_name = "todo"
urlpatterns = [
    path('', v.IndexView.as_view(), name="index"),
    path('signup/', v.signup, name="signup"),
    path('login/',v.login,name="login"),
    path('todoIndex/',v.todoIndex,name="todo-index"),
    path('addTask/',v.addtask,name="todo-add"),
    path('editTask/<int:task_id>',v.edittask, name="todo-edit"),
    path('deleteTask/<int:task_id>',v.deletetask,name="todo-delete"),
    path('logout',v.logout,name="logout")
]
