from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [
        'get_preview',  
        'get_filename',
    ]


    def get_preview(self, obj): 
        styles = """
            <style>  
                .video-link-img:hover {opacity:0.8;} 
                .title {
                    width:300px;overflow:auto;word-wrap:break-word;
                    font-family:Sans-serif;font-size:1em;color:rgba(0,0,0,0.5);
                    margin-top:0.5em;
                }
            </style>
        """ 
        preview = f"""
            {styles}
            <video class="video-js video-link-img" poster="{obj.preview.url if obj.preview else ""}" controls style="width:300px;height:200px;" >
                <source class="video-link-img" src="{obj.file.url}">
            </video>    
            <p class="title">{obj.uploaded_at.strftime("%d.%m.%Y %H:%M")}</p>    
            <script src="https://vjs.zencdn.net/7.15.4/video.min.js"></script>
            <p class="title">{obj.title}</p> 
        """  


        return mark_safe(preview)

    def get_filename(self, obj): 
        styles = """
            <style>  
                .filename {
                    max-width:120px;overflow:auto;word-wrap:break-word;
                    font-family:Sans-serif;font-size:1em;
                    color:rgba(0,0,0,0.5);
                    margin-top:0.5em;font-weight:800;
                } 
            </style>
        """
        file = f"""{styles}<p class="filename">{obj.file.url}</a>"""
        return mark_safe(file)

    get_preview.short_description = "Preview"
    get_filename.short_description = "File"