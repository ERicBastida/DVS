from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from images import views


urlpatterns = [


    #path('function1/', views.Home.as_view(), name='function1'),
    #path('listing_files/', views.files_list, name='files_list'),
    # Primer funcion, andando con el previzualizador en otra pantalla
    # path('files/<int:pk>', views.detail_file, name='class_preview_files'),
    # path('files/<int:pk>', views.PreviewFiles.as_view(), name='class_preview_files'),
    # path('function1/', views.upload_and_list_files, name='upload_and_list_files'),
    # path('delete/<int:pk>/', views.DeleteFileView.as_view(), name='class_delete_file'),
    # path('listing_files/', views.FilesListView.as_view(), name='class_list_files'),

    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),

    path('function1/', views.UploadFileView.as_view(),  name='class_upload_file'),
    path('function2/', views.UploadFileView2.as_view(), name='class_upload_file2'),
    path('function3/', views.UploadFileView3.as_view(), name='class_upload_file3'),

    path('function-output1/', views.OutputFileView.as_view(),  name='class_output_file'),
    path('function-output2/', views.OutputFileView2.as_view(), name='class_output_file2'),
    path('function-output3/', views.OutputFileView3.as_view(), name='class_output_file3'),

    path('process-file/', views.process_file, name='process'),


    path('admin/', admin.site.urls),

    path('files/<int:pk>/', views.delete_file, name='delete_file'),
    path('files2/<int:pk>/', views.delete_file2, name='delete_file2'),
    path('files3/<int:pk>/', views.delete_file3, name='delete_file3'),

    path('filesOutput/<int:pk>/', views.delete_file_output, name='delete_file_output'),
    path('filesOutput2/<int:pk>/', views.delete_file2_output, name='delete_file2_output'),
    path('filesOutput3/<int:pk>/', views.delete_file3_output, name='delete_file3_output'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
