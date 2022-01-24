from django.conf import settings 

TABLES = {
    "seminars_timetable": {
        "xlsx_path":f"{settings.BASE_DIR}/static/main/tables/timetable_2022.xlsx",
        "html_file":"exceltable.html",
        "html_path":f"{settings.BASE_DIR}/electrical/templates/electrical/tables/exceltable.html",
        "styles": """
            {% load static %}  
            <link rel="stylesheet" type="text/css" href="{% static 'main/css/timetable.css' %}"> 
        """
    },
}