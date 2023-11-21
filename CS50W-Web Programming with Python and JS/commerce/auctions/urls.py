from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create",views.create,name="create"),
    path('listing/<int:id>/', views.listing, name='listing'),
    path('bid/<int:id>/',views.bid,name='bid'),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>",views.category,name="category"),
    path('mylistings',views.mylistings,name='mylistings'),
    path('close/<int:id>/',views.close,name='close'),
    path('add_to_watchlist/<int:id>/',views.add_to_watchlist,name="add_to_watchlist"),
    path('remove_from_watchlist/<int:id>/',views.remove_from_watchlist,name="remove_from_watchlist"),
    path('watchlist/<int:user_id>/',views.watchlist,name="watchlist")
    
]
