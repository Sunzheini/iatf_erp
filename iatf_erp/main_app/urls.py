from django.urls import path
from iatf_erp.main_app.views import index, process_list, process_map, process_description

urlpatterns = (
    # http://127.0.0.1:8000/
    path('', index, name='index'),
    # http://127.0.0.1:8000/process-list/
    path('process-list/', process_list, name='process-list'),
    # http://127.0.0.1:8000/process-map/
    path('process-map/', process_map, name='process-map'),
    # http://127.0.0.1:8000/3/process_description/
    path('<process_id>/process_description/', process_description, name='process-map'),
)
