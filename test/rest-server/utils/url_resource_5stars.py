import requests
import json

url_rdf = "http://landregistry.data.gov.uk/data/ppi/transaction/D92BCBED-19E1-4060-916F-88EAB4372520.rdf"

#'content-type': 'text/csv'
url_csv = "https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/230872/hocs_senior_March_13.csv"

# 'content-type': 'application/json'
url_json = "http://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592&date=2011-08" 

url_http = "http://www.police.uk/data"

url_api = "http://landregistry.data.gov.uk/def/ppi"

url_pdf = "https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/60516/150k-decision-notice.pdf"

url_zip  = "http://dclgapps.communities.gov.uk/publicdata/hca_nrosh_extract/NROSH_Data_Extract_30052013_Part1.zip"

url_doc = 'http://81.17.70.199/carparks/111018%20Public%20Car%20Park%20Data%20-%20user%20guide%20v0%203.doc'

url_ppt = "http://webarchive.nationalarchives.gov.uk/+/http://www.fco.gov.uk/resources/en/power-point/publications/transparency/fco-london-staff-organogram-june-2010"

url_xls = "http://www.insolvencydirect.bis.gov.uk/otherinformation/statistics/201402/alltables.xlsx"

url_xml = "http://ratings.food.gov.uk/OpenDataFiles/FHRS501en-GB.xml"

url_ods = "https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/255629/ODS_Football-related_arrests_and_banning_order_statistics.ods"



url = url_rdf

print "URL: " + url
r = requests.get(url)
print r.status_code
print r.headers
#print r.content



