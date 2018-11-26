# pypatent

pypatent is a tiny Python package to easily search for and scrape US Patent and Trademark Office Patent Data.

[PyPI page](https://pypi.python.org/pypi/pypatent)

*New in version 1.1:*

This version makes searching and storing patent data easier:
* Simplified to 2 objects: `Search` and `Patent`
* A `Search` object searches the USPTO site and can output the results as a DataFrame or list. It can scrape the details of each patent, or just get the patent title and URL. Most users will only need to use this object.
* A `Patent` object fetches and holds a single patent's info. Fetching the patent's details is now optional. This object should only be used when you already have the patent URL and aren't conducting a search.

## Requirements

Python 3, BeautifulSoup, requests, pandas, re

## Installation

```
pip install pypatent
```

## Searching for patents

The Search object works similarly to the [Advanced Search at the USPTO](http://patft.uspto.gov/netahtml/PTO/search-adv.htm), with additional options.

### Specifying patent criteria for your search

There are two methods to specify your search criteria, and you can use one or both.

#### Search Method 1: Using a custom string

You may search for a certain string in all fields of the patent:
```python
pypatent.Search('microsoft') # Will return results matching 'microsoft' in any field
```

You may also specify complex search criteria as demonstrated on the [USPTO site](http://patft.uspto.gov/netahtml/PTO/help/helpadv.htm):
```python
pypatent.Search('TTL/(tennis AND (racquet OR racket))')
```

#### Search Method 2: Specify USPTO search fields (see Field Codes below)

Alternatively, you can specify one or more Field Code arguments to search within the specified fields. Multiple Field Code arguments will create a search with AND logic. OR logic can be used within a single argument. For more complex logic, use a custom string.
```python
pypatent.Search(pn='adobe', ttl='software') # Equivalent to search('PN/adobe AND TTL/software')
pypatent.Search(pn=('adobe or macromedia'), ttl='software') # Equivalent to search('PN/(adobe or macromedia) AND TTL/software')
```

#### Combining search methods 1 and 2

String criteria can be used in conjunction with Field Code arguments:
```python
pypatent.Search('acrobat', pn='adobe', ttl='software') # Equivalent to search('acrobat AND PN/adobe AND TTL/software')
```

The Field Code arguments have the same meaning as on the [USPTO site](http://patft.uspto.gov/netahtml/PTO/search-adv.htm).

### Additional search options

#### Limit the number of results

The `results_limit` argument lets you change how many patent results are retrieved. The default is 50, equivalent to one page of results.

```python
pypatent.Search('microsoft', results_limit=10) # Fetch 10 results only
```

#### Specify whether to fetch details for each patent

By default, pypatent retrieves the details of every patent by visiting each patent's URL from the search results.
This can take a long time since each page has to be scraped.
If you just need the patent titles and URLs from the search results, set `get_patent_details` to `False`:

```python
pypatent.Search('microsoft', get_patent_details=False) # Fetch patent numbers and titles only
```

### Formatting your search results

pypatent has convenience methods to format the Search object into either a Pandas DataFrame or list of dicts.

#### Format as Pandas DataFrame:
```python
pypatent.Search('microsoft').as_dataframe()
```

#### Format as list of dicts:
```python
pypatent.Search('microsoft', get_patent_details=False).as_list()
```

Sample result (without patent details):
```
[{
     'title': 'Electronic device',
      'url': 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=1&p=1&f=G&l=50&d=PTXT&S1=microsoft&OS=microsoft&RS=microsoft'
 },
 
 {'title': 'Portable electric device', ... }
```

## The Patent class
The `Search` class uses the `Patent` class to retrieve and store patent details for a given patent URL.
You can use it directly if you already know the patent URL (e.g. you ran a Search with `get_patent_details=False`)

```python
# Create a Patent object
this_patent = pypatent.Patent(title='Base station device, first location management device, terminal device, communication control method, and communication system',
                              url='http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=4&p=1&f=G&l=50&d=PTXT&S1=aaa&OS=aaa&RS=aaa')

# Fetch the details
this_patent.fetch_details()
```

### Patent Attributes Retrieved:

*Note, not all fields from the patent page are scraped. I hope to add more, and pull requests are appreciated :)*

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
