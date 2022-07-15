from django.conf import settings 

TABLES = {
    "seminars_timetable": {
        "xlsx_path":f"{settings.BASE_DIR}/static/tables/timetable_2022.xlsx",
        "html_file":"exceltable.html",
        "html_path":f'{settings.BASE_DIR}/electrical/templates/electrical/tables/timetable_file.html',
        "styles": """
            <link rel="stylesheet" type="text/css" href="/static/css/timetable.css"> 
        """
    },
}