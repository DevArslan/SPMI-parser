from django.shortcuts import render
from rest_framework import viewsets
from .models import scopusData
from .serializers import scopusDataSerializer
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from articleData.models import articleData
import requests
import pandas as pd
from sqlalchemy import create_engine

class scopusDataViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated,]
    queryset = scopusData.objects.all().order_by('author','creator','title','journal','date','volume','issue','pages','doi')
    serializer_class = scopusDataSerializer

    def SCOPUS():

        scopusIDs = list(articleData.objects.all().order_by('scopusID'))
        COLUMNS = ['author','creator','title','journal','date','volume','issue','pages','doi']
        API_KEY = 'd7fa32bafd2d65c4af983a7ad735b051'
        df = pd.DataFrame(columns = COLUMNS)

        def search_request(author_id):
            return f'https://api.elsevier.com/content/search/scopus?query=au-id({author_id})&apiKey={API_KEY}&date=2019'

        # def get_df_with_publics(author, json):
        #     df = pd.DataFrame(columns = COLUMNS)
        #     for entry in json['search-results']['entry']:
        #         df = df.append(get_series_from_entry(author, entry), ignore_index=True)
        #     return df
        def get_df_with_publics(author, json):
            for entry in json['search-results']['entry']:
                get_series_from_entry(author, entry)


        def get_series_from_entry(author, entry):
            scopusDataItem = scopusData()
            scopusDataItem.author = author
            scopusDataItem.creator = entry.get('dc:creator')
            scopusDataItem.title = entry.get('dc:title')
            scopusDataItem.journal = entry.get('prism:publicationName')
            scopusDataItem.date = entry.get('prism:coverDate')
            scopusDataItem.volume = entry.get('prism:volume','') 
            scopusDataItem.issue = entry.get('prism:issueIdentifier','')
            scopusDataItem.pages = entry.get('prism:pageRange','') 
            scopusDataItem.doi = entry.get('prism:doi')
            scopusDataItem.save()
            # return pd.Series([author, creator, title, journal, date, volume, issue, pages, doi], index = COLUMNS)

        for i in range(10):

            response = requests.get(search_request(scopusIDs[i].scopusID))
            json = response.json()

            df_author = get_df_with_publics(scopusIDs[i].scopusID, json)
            df = pd.concat([df, df_author])

    # SCOPUS()
