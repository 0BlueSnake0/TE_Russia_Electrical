from django.conf import settings 

TABLES = {
    "timetable_2020": {
        "xlsx_path":f"{settings.BASE_DIR}/static/main/tables/timetable_2020.xlsx",
        "html_path":f"{settings.BASE_DIR}/electrical/templates/electrical/tables/timetable_2020.html",
        "styles": """
            {% load static %}  
            <link rel="stylesheet" type="text/css" href="{% static 'main/css/timetable.css' %}"> 
        """
    }
}