from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.conf import settings
from django.http import FileResponse
from xlsx2html import xlsx2html 
from pytils.translit import slugify 
from .models import Catalog, Product, ContactPerson, TimeTable
from .slideshows import SLIDESHOWS


def index(request):
    return render(
        request,
        template_name="electrical/index.html",
        context={
            'image_slideshow':SLIDESHOWS['image_slideshow'],
            'text_slideshow':SLIDESHOWS['text_slideshow'],
        }
    )
    

class CatalogListView(ListView):
    model = Catalog
    template_name="electrical/catalogs.html"
    context_object_name = 'catalogs'


class CatalogDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        pdf_file = f'{settings.BASE_DIR}{Catalog.objects.get(slug=kwargs["catalog_slug"]).pdf.url}'

        return FileResponse(open(pdf_file, 'rb'), content_type='application/pdf' )


class ContactListView(TemplateView):
    model = ContactPerson
    template_name="electrical/contacts.html"


    def get_queryset(self):
        return self.model.objects.all()


    def get(self, request, *args, **kwargs):
        contacts_dict = {}
        for contact in self.get_queryset():
            slugified_city = slugify(contact.city)
            if slugified_city not in contacts_dict:
                contacts_dict[slugified_city] = []
            contacts_dict[slugified_city].append(contact)

        context={
            "current_city":kwargs["city"],
            "contacts":contacts_dict[kwargs["city"]]
        }
        return self.render_to_response(context)


class ProductDetailView(DetailView):
    model = Product
    template_name="electrical/product.html"

    def get(self, *args, **kwargs):
        context={
            'product': Product.objects.get(slug=kwargs['product_slug'])
        }
        return self.render_to_response(context)


def seminars_timetable(request, **kwargs):
    try:
        timetable = list(TimeTable.objects.all())[0]
        table_path = f'{settings.BASE_DIR}{timetable.table.url}'
        html_path = f'{settings.BASE_DIR}/electrical/templates/electrical/tables/timetable_file.html'
    
        xlsx2html(table_path, html_path) 
        
        file = open(html_path, 'r', encoding="utf8")  
        html = f"""
            <link rel="stylesheet" type="text/css" href="/static/css/timetable.css"> 
            {file.read()}
        """
        file.close() 

        file = open(html_path, 'w',encoding='utf8')
        file.write(html)
        file.close() 
    except (FileNotFoundError, IndexError):
        html_path = ''

    
    return render(
        request,
        template_name=f'electrical/timetable.html',
        context={   
            'html_table_path':html_path,
        }
    )  


class RegionsView(TemplateView):
    model=ContactPerson
    template_name="electrical/regions.html"

    def get_queryset(self):
        return self.model.objects.all()


    def get(self, request, *args, **kwargs):
        contacts_dict = {}
        for contact in self.get_queryset():
            slugified_city = slugify(contact.city)
            if slugified_city not in contacts_dict:
                contacts_dict[slugified_city] = []
            contacts_dict[slugified_city].append(contact)

        context={
            "contacts":contacts_dict,
        }
        return self.render_to_response(context)


def stop_activity(request, **kwargs): 
    return render(
        request,
        template_name="electrical/stop_activity.html"
    )  


def page_not_found(request, exception):
    return render(
        request,
        template_name='page_not_found.html'
    )
