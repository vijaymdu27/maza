from django.shortcuts import render,HttpResponse
from top.models import ApiVieu
import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ApiVieuSerializer
from .filters import ApiVieuFilters
from rest_framework import filters
from rest_framework import generics


@api_view(['GET','POST'])
def index(request):
    '''collect the data from url and convert it to normal text format
    then post it to db and particular url using index function'''
    response = requests.get("https://jobs.github.com/positions.json")
    data = json.loads(response.text)
    objs = [
        ApiVieu(
            id=job['id'],
            type=job['type'],
            url=job['url'],
            created_at=job['created_at'],
            company=job['company'],
            company_url=job['company_url'],
            location=job['location'],
            title=job['title'],
            description=job['description'],
        )
        for job in data

    ]

    datas = ApiVieu.objects.bulk_create(objs=objs)
    db = requests.post('http://127.0.0.1:8000/index', data=datas)
    return HttpResponse("created")


@api_view(['GET'])
def about(request):
    '''from db list out the particular field(title) using values_list in api view '''
    dood = ApiVieu.objects.values_list('title')
    return Response(dood)


@api_view(['GET'])
def expect(request):
    '''using expect function to view the whole data which is stored in db in api view'''
    task=ApiVieu.objects.all()
    return Response(task)


@api_view(['GET'])
def unable(request,**args):
    '''from db we can filter the data from particular field
    so here we using -> unable/?id= for filter the id field from db in api view'''
    ids=request.GET.get('id')
    mod=ApiVieu.objects.filter(id=ids)
    serializer=ApiVieuSerializer(mod,many=True)
    return Response(serializer.data)


def possible(request):
    '''from db we can filter the data from multiple fields
    so here we using title and location for filter the data in json view (function base)'''
    f = ApiVieuFilters(request.GET, queryset=ApiVieu.objects.all())
    return render(request,'template.html', {'filter': f})


class UserListView(generics.ListAPIView):
    '''from db we can filter the data from multiple fields
    so here we using title and location for filter the data in json view (class base)'''
    queryset = ApiVieu.objects.all()
    serializer_class = ApiVieuSerializer
    filter_backends = [filters.SearchFilter]
    search_fields  = ['title', 'location']
