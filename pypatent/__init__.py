# coding: utf-8

from bs4 import BeautifulSoup
import requests
import re

class patent:
    def __init__(self, url):
        self.url = url
        
        r = requests.get(url).text
        s = BeautifulSoup(r, 'html.parser')

        try:
            self.patent_num = s.find(string='United States Patent ').find_next().text
        except:
            self.patent_num = None
        
        try:
            self.patent_date = s.find_all(align='right', width='50%')[-1].text
        except:
            self.patent_date = None
        
        try:
            abstract = s.find(string='Abstract').find_next().text.replace('\n', '').strip()
            self.abstract = re.sub(' +',' ', abstract)
        except:
            self.abstract = None
        
        try:
            inventors = s.find(string='Inventors:').find_next().text.replace('\n', '').split('),')
            inventors = [t.split(';') for t in inventors]
            inventors = [[i.split('(') for i in j] for j in inventors]
            self.inventors = []
            for person in inventors:
                lname = person[0][0].strip()
                fname = person[1][0].strip()
                loc = person[1][1].strip().replace(')', '')
                d = [fname, lname, loc]
                self.inventors.append(d)
        except:
            self.inventors = None

        try:
            self.applicant_name = s.find(string=re.compile('Applicant:')).find_next().find('td').text.strip()
        except:
            self.applicant_name = None
        
        try:
            rem_applicant_data = s.find(string=re.compile('Applicant:')).find_next().find('td').find_next_siblings()
            try:
                self.applicant_city = rem_applicant_data[0].text.strip()
            except:
                self.applicant_city = None
            try:
                self.applicant_state = rem_applicant_data[1].text.strip()
            except:
                self.applicant_state = None
            try:
                self.applicant_country = rem_applicant_data[2].text.strip()
            except:
                self.applicant_country = None
        except:
            self.applicant_city = None
            self.applicant_state = None
            self.applicant_country = None
        
        try:
            assignee_raw = s.find(string=re.compile('Assignee:')).find_next().text.replace('\n', '')
            assignee_data = assignee_raw.split('(')
            try:
                self.assignee_name = assignee_data[0].strip()
            except:
                self.assignee_name = None
            try:
                self.assignee_loc = assignee_data[1].strip().replace(')', '')
            except:
                self.assignee_loc = None
        except:
            self.assignee_name = None
            self.assignee_loc = None
        
        try:
            self.family_id = s.find(string=re.compile('Family ID:')).find_next().text
        except:
            self.family_id = None

        try:
            self.applicant_num = s.find(string=re.compile('Appl. No.:')).find_next().text
        except:
            self.applicant_num = None
        
        try:
            self.file_date = s.find(string=re.compile('Filed:')).find_next().text
        except:
            self.file_date = None

        try:
            claims = s.find(string=re.compile('Claims')).find_all_next(string=True)
            claims = claims[:claims.index('Description')]
            self.claims = [i.replace('\n', '').strip() for i in claims if i.replace('\n', '').strip() != '']
        except:
            self.claims = None
        
        try:
            description = s.find(string=re.compile('Description')).find_all_next(string=True)
            self.description = [i.replace('\n', '').strip() for i in description if i.replace('\n', '').strip() not in ['', '* * * * *']]
        except:
            self.description = None

def search(string=None, results_limit=50, pn=None, isd=None, ttl=None, abst=None, aclm=None, spec=None, ccl=None, cpc=None, cpcl=None, icl=None, apn=None, apd=None, apt=None, govt=None, fmid=None, parn=None, rlap=None, rlfd=None, prir=None, prad=None, pct=None, ptad=None, pt3d=None, pppd=None, reis=None, rpaf=None, afff=None, afft=None, in_=None, ic=None, is_=None, icn=None, aanm=None, aaci=None, aast=None, aaco=None, aaat=None, lrep=None, an=None, ac=None, as_=None, acn=None, exp=None, exa=None, ref=None, fref=None, oref=None, cofc=None, reex=None, ptab=None, sec=None, ilrn=None, ilrd=None, ilpd=None, ilfd=None):
    args = {k:str(v).replace(' ', '-') for k,v in locals().items() if v is not None}
    searchstring = ' AND '.join(['%s/%s' % (key, value) for (key, value) in args.items() if key not in ['results_limit']])
    searchstring = searchstring.replace('string/', '')
    searchstring = searchstring.replace(' ', '+')
    
    replace_dict = {'/':'%2F'}
    
    for k,v in replace_dict.items():
        searchstring = searchstring.replace(k, v)
    
    base_url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&p=1&f=S&l=50&Query='
    
    url = base_url + searchstring + '&d=PTXT'
    
    r = requests.get(url).text
    s = BeautifulSoup(r, 'html.parser')
    total_results = int(s.find(string=re.compile('out of')).find_next().text.strip())
    
    patents = get_patents_from_results(url)
    
    num_results_fetched = len(patents)
    
    list_num = 2

    base_url_nextpgs = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&f=S&l=50&d=PTXT'
    
    url_pre = base_url_nextpgs + '&OS=' + searchstring + '&RS=' + searchstring + '&Query=' + searchstring + '&TD=' + str(total_results) + '&Srch1=' + searchstring + '&NextList'
    url_post = '=Next+50+Hits'
    
    while (num_results_fetched < total_results) and (num_results_fetched < results_limit):
        this_url = url_pre + str(list_num) + url_post
        thispatents = get_patents_from_results(this_url)
        patents.extend(thispatents)

        num_results_fetched = len(patents)

        if num_results_fetched >= results_limit:
            patents = patents[:results_limit]
            return patents

        list_num += 1

    return patents

def get_patents_from_results(url):
    r = requests.get(url).text
    s = BeautifulSoup(r, 'html.parser')
    patents_raw = s.find_all('a', href=re.compile('netacgi'))
    patents_base_url = 'http://patft.uspto.gov'
    patents_raw_list = [[i.text.replace('\n', '').strip(), patents_base_url + i['href']] for i in patents_raw if i.text.replace('\n', '').strip() != '']

    patents = []

    for patent_num_idx in range(0, len(patents_raw_list), 2):
        patent_num = patents_raw_list[patent_num_idx][0]
        patent_title = patents_raw_list[patent_num_idx+1][0]
        patent_title = re.sub(' +',' ', patent_title)
        patent_link = patents_raw_list[patent_num_idx][1]
        patents.append([patent_num, patent_title, patent_link])
    
    return patents
