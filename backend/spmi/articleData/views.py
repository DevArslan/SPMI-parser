from django.shortcuts import render
from rest_framework import viewsets
from .models import articleData
from .serializers import articleDataSerializer
import requests
import re
from personalData.models import personalData
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from sqlalchemy import create_engine

class articleDataViewSet(viewsets.ModelViewSet):
    queryset = articleData.objects.all().order_by('spmiProfileLink','rsciID','spinID','scopusID','researcherID','orcidID','rsciProfileLink','scopusProfileLink','publonsProfileLink','orcidProfileLink','researchProfileLink','scholarProfileLink')
    serializer_class = articleDataSerializer

    def updateLinks():
        personalLinkList = []
        personalLink = list(personalData.objects.all().order_by('link'))
        for item in personalLink:
            personalLinkList.append(item.link)

        MAIN_INFO = 'div.man_main_info > div.large-5'

        URL_BASE = 'http://personalii.spmi.ru'

        def extract_text(results):
            return results[0].text
        
        def extract(results, attr):
            if results:
                if type(attr) == int:
                    res = results[0].contents[attr]
                    return res if type(res) == bs4.element.NavigableString else res.text
                if type(attr) == str:
                    return results[0].get(attr)
            return None
        # def filtrate(df,field,partial_text):
        #     df = df.fillna('')
        #     return df[df[field].str.contains(partial_text)]

        def check(res):
            if res:
                if type(res) == str:
                    return res
                return res[0]
            return 'Empty'

        # def extract_info_from_personal_page(link) -> pd.Series:
        def extract_info_from_personal_page(link):
            articleDataItem = articleData()
            soup = BeautifulSoup(requests.get(URL_BASE+link).text, 'html')
            main = soup.select(MAIN_INFO)
            txt = extract_text(main)
            articleDataItem.spmiProfileLink = link
            articleDataItem.rsciID = check(re.findall(r'РИНЦ Author ID: ([0-9]+)',txt))
            articleDataItem.spinID = check(re.findall(r'SPIN-код: ([0-9-]+)',txt))
            articleDataItem.scopusID = check(re.findall(r'\BAuthor ID: ([0-9]+)',txt))
            articleDataItem.researcherID = check(re.findall(r'ResearcherID: ([A-Z0-9-]+)',txt))
            articleDataItem.orcidID = check(re.findall(r'ORCID ID: ([0-9-]+)',txt))
            articleDataItem.rsciProfileLink = check(extract(soup.select('a:contains("Профиль автора в РИНЦ")'), 'href'))
            articleDataItem.scopusProfileLink = check(extract(soup.select('a:contains("Профиль автора в Scopus")'), 'href'))
            articleDataItem.publonsProfileLink = check(extract(soup.select('a:contains("Профиль автора в Publons (WoS)")'), 'href'))
            articleDataItem.orcidProfileLink = check(extract(soup.select('a:contains("Профиль автора в ORCID")'), 'href'))
            articleDataItem.researchProfileLink = check(extract(soup.select('a:contains("Профиль автора в ResearchGate")'), 'href'))
            articleDataItem.scholarProfileLink = check(extract(soup.select('a:contains("Профиль автора в Google Scholar")'), 'href'))
            # return pd.Series([link, Author_ID, SPIN, Scopus_ID, Researcher_ID, ORCID_ID, rinc_link, scopus_link, publons_link,
            #                 orcid_link, research_gate_link, google_link], index = COLUMNS_EXT)
            articleDataItem.save()

        def personal_page_parse(links):
            m = len(links)
            n = 0
            print('[', end = '')
            for link in links:
                # extract_info_from_personal_page(link)
                try:
                    extract_info_from_personal_page(link)
                    n += 1
                    if n/m > 0.05:
                        n = 0
                        print('-', end = '')
                except:
                    print('что-то не так с записью ', link)
            print('] [OK]')

        personal_page_parse((personalLinkList))

    updateLinks()