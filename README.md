# pypatent
Search for and retrieve US Patent and Trademark Office Patent Data

[PyPI page](https://pypi.python.org/pypi/pypatent)

## Requirements
Python 3, BeautifulSoup, requests, re

## Installation

```
pip install pypatent
```

## Searching for Patents
The search function works similarly to the [Advanced Search at the USPTO](http://patft.uspto.gov/netahtml/PTO/search-adv.htm)

```python
def search(string=None, results_limit=50, pn=None, isd=None, ttl=None, abst=None, aclm=None, spec=None, ccl=None, cpc=None, cpcl=None, icl=None, apn=None, apd=None, apt=None, govt=None, fmid=None, parn=None, rlap=None, rlfd=None, prir=None, prad=None, pct=None, ptad=None, pt3d=None, pppd=None, reis=None, rpaf=None, afff=None, afft=None, in_=None, ic=None, is_=None, icn=None, aanm=None, aaci=None, aast=None, aaco=None, aaat=None, lrep=None, an=None, ac=None, as_=None, acn=None, exp=None, exa=None, ref=None, fref=None, oref=None, cofc=None, reex=None, ptab=None, sec=None, ilrn=None, ilrd=None, ilpd=None, ilfd=None)
```

You may specify just the string argument to search for a certain string in all fields. For example:

```python
search('microsoft') # Will return results matching 'microsoft' in any field
```
You may also use the string argument to specify complex search criteria as demonstrated on the [USPTO site](http://patft.uspto.gov/netahtml/PTO/help/helpadv.htm). For example:

```python
search('TTL/(tennis AND (racquet OR racket))')
```

Alternatively (or in conjunction with the string criteria as described below), you can specify one or more Field Code arguments to search within the specified fields. Multiple Field Code arguments will create a search with AND logic. OR logic can be used within a single argument. For more complex logic, use a custom string.

```python
search(pn='adobe', ttl='software') # Equivalent to search('PN/adobe AND TTL/software')
search(pn=('adobe or macromedia'), ttl='software') # Equivalent to search('PN/(adobe or macromedia) AND TTL/software')
```

String criteria can be used in conjunction with Field Code arguments:

```python
search('acrobat', pn='adobe', ttl='software') # Equivalent to search('acrobat AND PN/adobe AND TTL/software')
```

The Field Code arguments have the same meaning as on the [USPTO site](http://patft.uspto.gov/netahtml/PTO/search-adv.htm).

The `results_limit` argument lets you change how many patent results are retrieved. The default is 50, equivalent to one page of results.

Search results are returned as a list of patent numbers, patent titles, and links:

```python
[[patent_number_1, patent_title_1, patent_link_1], ..., [patent_number_n, patent_title_n, patent_link_n]]
```

## Retrieving Patent Details: The patent Class
Use the patent class to retrieve patent details for a given patent URL.

```python
this_patent = patent('http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=4&p=1&f=G&l=50&d=PTXT&S1=aaa&OS=aaa&RS=aaa')
```

The following attributes are retrieved:

* patent_num: Patent Number
* patent_date: Issue Date
* abstract: Abstract
* inventors: List of Names of Inventors and Their Locations
* applicant_name: Applicant Name
* applicant_city: Applicant City
* applicant_state: Applicant State
* applicant_country: Applicant Country
* assignee_name: Assignee Name
* assignee_loc: Assignee Location
* family_id: Family ID
* applicant_num: Applicant Number
* file_date: Filing date
* claims: Claims Description (as a list)
* description: Patent Description (as a list)

### Field Code Arguments for Search Function
* PN: Patent Number
* ISD: Issue Date
* TTL: Title
* ABST: Abstract
* ACLM: Claim(s)
* SPEC: Description/Specification
* CCL: Current US Classification
* CPC: Current CPC Classification
* CPCL: Current CPC Classification Class
* ICL: International Classification
* APN: Application Serial Number
* APD: Application Date
* APT: Application Type
* GOVT: Government Interest
* FMID: Patent Family ID
* PARN: Parent Case Information
* RLAP: Related US App. Data
* RLFD: Related Application Filing Date
* PRIR: Foreign Priority
* PRAD: Priority Filing Date
* PCT: PCT Information
* PTAD: PCT Filing Date
* PT3D: PCT 371 Date
* PPPD: Prior Published Document Date
* REIS: Reissue Data
* RPAF Reissued Patent Application Filing Date
* AFFF: 130(b) Affirmation Flag
* AFFT: 130(b) Affirmation Statement
* IN: Inventor Name
* IC: Inventor City
* IS: Inventor State
* ICN: Inventor Country
* AANM: Applicant Name
* AACI: Applicant City
* AAST: Applicant State
* AACO: Applicant Country
* AAAT: Applicant Type
* LREP: Attorney or agent
* AN: Assignee Name
* AC: Assignee City
* AS: Assignee State
* ACN: Assignee Country
* EXP: Primary Examiner
* EXA: Assistant Examiner
* REF: Referenced By
* FREF: Foreign References
* OREF: Other References
* COFC: Certificate of Correction
* REEX: Re-Examination Certificate
* PTAB: PTAB Trial Certificate
* SEC: Supplemental Exam Certificate
* ILRN: International Registration Number
* ILRD: International Registration Date
* ILPD: International Registration Publication Date
* ILFD: Hague International Filing Date
