from django.contrib import admin
from django.conf import settings
from .models import *
from django.contrib.auth.models import Group, User
from django.utils.safestring import mark_safe  


admin.site.unregister(Group)
admin.site.unregister(User) 


@admin.register(Modal)
class ModalAdmin(admin.ModelAdmin):
    list_display = [
        'button_title',
        'get_button_text',
        'slug',
        'get_content', 
    ]  

    def get_content(self, obj):
        html = f"""{obj.content}"""
        return mark_safe(html)
    
    get_content.short_description = "Content"


    def get_button_text(self, obj):
        html = ""
        if obj.button_text:
            html = f"{obj.button_text}"
        return mark_safe(html)

    get_button_text.short_description = "Button text"


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'get_preview',
        'pdf',
    ]  

    def get_preview(self, obj):
        html = ""
        if obj.preview and obj.preview.url:
                html = f"""
                <img src="{obj.preview.url}" style="width:25em;">
            """
        return mark_safe(html)

    get_preview.short_description = "Preview"
    
    
@admin.register(ProductVideo)
class ProductVideoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'get_video',
        'get_link',
    ]   


    def get_video(self, obj):
        params = f"""controls preload="auto" poster='{obj.preview.url}' """
        params += """data-setup='{"aspectRatio":"1280:600", "playbackRates": [1, 1.25, 1.5, 1.75, 2], "techOrder": ["youtube"], sources": [{ "type": "video/youtube", "src":"""
        params += f""" "{obj.youtube_link}" """ + "}]'" 
        html = f"""
            <link rel="stylesheet" type="text/css" href="https://vjs.zencdn.net/7.15.4/video-js.css">
            <link rel="stylesheet" type="text/css" href="https://vjs.zencdn.net/7.15.4/video-js.min.css"> 
            <video class="video-js vjs-default-skin vjs-big-play-centered video-clip" {params}></video>  
            """
        html+= """
            <script src="https://vjs.zencdn.net/7.17.0/video.min.js"></script>
            <script type="text/javascript" src="{% static 'js/video/youtube.min.js' %}?v=5"></script>
        """ 
        return mark_safe(html)

    get_video.short_description = "Video"


    def get_link(self, obj):
        html = f"""
            <a target="_blank" href="{obj.youtube_link}">{obj.youtube_link}</a>
        """
        return mark_safe(html)

    get_link.short_description = "Youtube"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'order',
        'slug',
        'get_description1',
        'get_modals',
        'get_videos',
        'get_catalogs',
    ]  
 
    ordering = ['order']

    def get_description1(self, obj):
        html = ""
        if obj.description1:
            html = f"""{obj.description1}"""
        return mark_safe(html)

    get_description1.short_description = "Description 1"

 
    def get_modals(self, obj):
        styles = """
            <style> 
                .edit-link {font-size:1.25em;color:black !important;font-weight:800;}
                .edit-link:hover {color:cornflowerblue !important;opacity:0.6;}
            </style>
        """
        html = f'{styles}<div style="display:flex;flex-direction:column;flex-wrap:wrap;">'
        for modal in obj.modals.all():
            html += f'''
                <a class="edit-link" href="/admin/{modal._meta.app_label}/{modal._meta.model_name}/{modal.pk}/change">
                {modal.button_title}
                </a>
            '''
        html+= "</div>"  
        return mark_safe(html)

    get_modals.short_description = "Modals"



    def get_videos(self, obj): 
        html = f'<div style="display:flex;flex-direction:column;flex-wrap:wrap;">'
        for video in obj.videos.all():
            html += f'''
                <a class="edit-link" href="/admin/{video._meta.app_label}/{video._meta.model_name}/{video.pk}/change"> 
                    <p>{video.title}</p>
                    <img style="width:15em;" src="{video.preview.url if video.preview and video.preview.url else ''}">
                </a>
            '''
        html+= "</div>"  
        return mark_safe(html)

    get_videos.short_description = "Videos"


    def get_catalogs(self, obj): 
        html = f'<div style="display:flex;position:relative;flex-wrap:wrap;width:70em;">'
        for catalog in obj.catalogs.all():
            html += f'''
                <a style="display:block;margin:2em;" class="edit-link" href="/admin/{catalog._meta.app_label}/{catalog._meta.model_name}/{catalog.pk}/change">  
                    <p>{catalog.name}</p> 
                    <img style="width:10em;" src="{catalog.preview.url if catalog.preview and catalog.preview.url else ''}">
                </a>  
            '''
        html+= "</div>"  
        return mark_safe(html)

    get_catalogs.short_description = "Catalogs"

    
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'get_region', 
    ] 


    def get_region(self, obj):
        html = ""
        if obj.region != None:
            styles = """
                <style> 
                    .edit-link {font-size:1.25em;color:black !important;font-weight:800;}
                    .edit-link:hover {color:cornflowerblue !important;opacity:0.6;}
                </style>
            """
            html = f""" 
                {styles}
                <div style="display:flex;align-items:center;"> 
                    <a class="edit-link" href="/admin/{obj.region._meta.app_label}/{obj.region._meta.model_name}/{obj.region.pk}/change">
                    {obj.region.name}
                    </a>
                    <div style="border:0.2em solid black;margin:0.5em;width:2em;height:2em;background-color:{obj.region.color};"></div>
                </div>
            """
        return mark_safe(html)

    get_region.short_description = "Region"

    
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = [
        'get_name_and_color', 
        'slug',
        'get_states',
    ] 


    def get_name_and_color(self, obj):
        html = f""" 
            <div style="display:flex;align-items:center;">
                <p>{obj.name}</p>
                <div style="border:0.2em solid black;margin:0.5em;width:2em;height:2em;background-color:{obj.color};"></div>
            </div>
        """
        return mark_safe(html)

    get_name_and_color.short_description = "Name"


    def get_states(self, obj):
        styles = """
            <style> 
                .edit-link {font-size:1.25em;color:black !important;font-weight:800;}
                .edit-link:hover {color:cornflowerblue !important;opacity:0.6;}
            </style>
        """
        html = f'{styles}<div style="display:flex;flex-direction:column;flex-wrap:wrap;">'
        for state in State.objects.filter(region=obj):
            html += f'''
                <a class="edit-link" href="/admin/{state._meta.app_label}/{state._meta.model_name}/{state.pk}/change">
                {state.name} ({state.slug})
                </a>
            '''
        html+= "</div>"  
        return mark_safe(html)

    get_states.short_description = "States"

    
@admin.register(ContactPerson)
class ContactPersonAdmin(admin.ModelAdmin):
    list_display = [
        'get_info',
        'city',
        'get_region',
        'get_states',
    ] 


    def get_info(self, obj):
        styles = """
            <style> 
                h1 {
                    color:black;
                    font-size:1.5em;
                    font-weight:800;
                }
                h1:hover {
                    color:gray;
                }
            </style>
        """
        html = f""" 
            {styles}
            <div>
                <h1>{obj.first_name} {obj.last_name}</h1>
                <p style="color:black;">{obj.position}</p>
                <p style="color:gray;">{obj.organization}</p>
                <p style="color:gray;">{obj.address if obj.address else ''}</p>
                
                <div style="display:flex;align-items:center;">
                    <p style="color:#e98300;">TEL</p>
                    <a target="_blank" href="tel:{obj.mobile}">{obj.mobile}</a>
                    <p style="color:gray;">{'доб. ' + obj.extended_number if obj.extended_number else ''}</p> 
                </div>
                <div style="display:flex;align-items:center;">
                    <p style="color:#e98300;">MOBILE</p>
                    <a target="_blank" href="tel:{obj.tel}">{obj.tel}</a>
                </div>
                <div style="display:flex;align-items:center;"> 
                    <img style="width:2em;margin:0.5em;" src="/static/images/icons/@-email-2.png">
                    <a target="_blank" href="mailto:{obj.email}">{obj.email}</a>
                </div>
            </div> 
        """
        return mark_safe(html)
 
    get_info.short_description = "Person"
    

    def get_region(self, obj): 
        html = ""
        if obj.region:
            styles = """
                <style> 
                    .edit-link {font-size:1.25em;color:black !important;font-weight:800;}
                    .edit-link:hover {color:cornflowerblue !important;opacity:0.6;}
                </style>
            """
            html = f""" 
                {styles}
                <div style="display:flex;align-items:center;"> 
                    <a class="edit-link" href="/admin/{obj.region._meta.app_label}/{obj.region._meta.model_name}/{obj.region.pk}/change">
                    {obj.region.name}
                    </a>
                    <div style="border:0.2em solid black;margin:0.5em;width:2em;height:2em;background-color:{obj.region.color};"></div>
                </div>
            """
        return mark_safe(html)

    get_region.short_description = "Region"


    def get_states(self, obj):
        styles = """
            <style> 
                .edit-link {font-size:1.25em;color:black !important;font-weight:800;}
                .edit-link:hover {color:cornflowerblue !important;opacity:0.6;}
            </style>
        """
        html = f'{styles}<div style="display:flex;flex-direction:column;flex-wrap:wrap;">'
        for state in State.objects.filter(region=obj.region):
            html += f'''
                <a class="edit-link" href="/admin/{state._meta.app_label}/{state._meta.model_name}/{state.pk}/change">
                {state.name} ({state.slug})
                </a>
            '''
        html+= "</div>"  
        return mark_safe(html)

    get_states.short_description = "States"

    
@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = [
        'get_table'
    ] 


    def get_table(self, obj):
        with open(f'{settings.BASE_DIR}/electrical/templates/electrical/tables/timetable_file.html', 'r') as html_table_file:
            html = html_table_file.read()
            return mark_safe(html) 
    
    get_table.short_description = "Table"
