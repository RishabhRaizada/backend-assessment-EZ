from django.urls import path
from .views import SignupView, LoginView, UploadFileView, DownloadFileView, ListFilesView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('upload-file/', UploadFileView.as_view(), name='upload-file'),
    path('download-file/<str:file_id>/', DownloadFileView.as_view(), name='download-file'), 
    path('list-files/', ListFilesView.as_view(), name='list-files'),
    
]
