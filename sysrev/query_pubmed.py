import sys              # For command-line arguments
import urllib
import urllib2          # For querying pubmed
import xmltodict        # For transforming XML responses to dictionaries

# Query PubMed and return the entire result as a dictionary
def query_pubmed(search_terms):

    # Format the terms to be included in the URL
    url_term = urllib.quote(search_terms)

    # API docs: http://www.ncbi.nlm.nih.gov/home/api.shtml
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax=1000&term='+url_term

    try:
        # Connect to the server and read the response
        response_xml = urllib2.urlopen(url).read()

        # Convert the response to a Python dictionary
        response_dict = xmltodict.parse(response_xml)

        # Keys: "Count", "RetMax", "RetStart", "IdList"
        #       "TranslationSet", "TranslationStack"
        #       "QueryTranslation"
        # print response_dict["eSearchResult"].keys()
        # print response_dict["eSearchResult"]["Count"]

        # Return the entire dictionary
        return response_dict

    # If connection fails
    except urllib2.URLError as e:
        print "Error making request: ", e


# Query PubMed and return the number of docs for a search term
def get_document_count(search_terms):

    res = query_pubmed(search_terms)
    return res["eSearchResult"]["Count"]


# Query PubMed for a list of paper IDs
def get_id_list(search_terms):

    res = query_pubmed(search_terms)
    return res["eSearchResult"]["IdList"]


# Get all info for a particular paper
def get_paper_info(id):
    id = urllib.quote(id)

    # API docs: http://www.ncbi.nlm.nih.gov/home/api.shtml
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&rettype=abstract&id='+str(id)

    try:
        response_xml = urllib2.urlopen(url).read()
        response_dict = xmltodict.parse(response_xml)
        return response_dict

    # If connection fails
    except urllib2.URLError as e:
        print "Error making request: ", e


def get_paper_url(id):
    # Sadly, the paper URL is not contained with the title, author and abstract
    # So we need an entirely new query to go get it

    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&cmd=prlinks&id='+id

    try:
        response_xml = urllib2.urlopen(url).read()
        response_dict = xmltodict.parse(response_xml)
        return response_dict['eLinkResult']['LinkSet']['IdUrlList']['IdUrlSet']['ObjUrl']['Url']

    except:
        # Oddly, some pages may not have links.
        # If that's the case we return None.
        # This will cancel the creation of a Page.
        return None


def get_paper_title(paper_dict):
    return paper_dict['PubmedArticleSet']['PubmedArticle']['MedlineCitation']['Article']['Journal']['Title']


def get_paper_abstract(paper_dict):

    try:
        text = paper_dict['PubmedArticleSet']['PubmedArticle']['MedlineCitation']['Article']['Abstract']['AbstractText']
        return text

    except:
        # Django likes empty string for char fields more than nulls
        return ""

def get_paper_author(paper_dict):
    # print "Author: ", paper_dict['PubmedArticleSet']['PubmedArticle']['MedlineCitation']['Article']['AuthorList']['Author']
    # print

    # XML in different formats ;(
    # We have to try getting the author in a few different ways

    try:
        forename = paper_dict['PubmedArticleSet']['PubmedArticle']['MedlineCitation']['Article']['AuthorList']['Author'][0]['ForeName']
        surname = paper_dict['PubmedArticleSet']['PubmedArticle']['MedlineCitation']['Article']['AuthorList']['Author'][0]['LastName']
        return forename+" "+surname

    except:
        pass

    try:
        forename = paper_dict['PubmedArticleSet']['PubmedArticle']['MedlineCitation']['Article']['AuthorList']['Author']['ForeName']
        surname = paper_dict['PubmedArticleSet']['PubmedArticle']['MedlineCitation']['Article']['AuthorList']['Author']['LastName']
        return forename+" "+surname

    except:
        pass

    # Django docs recommend saving empty strings
    # instead of nulls in charfields
    return ""


# Main function for testing
def main():

    if len(sys.argv) != 2:
        print "Error: I need ONE string as a query parameter"
        return

    id = sys.argv[1]
    # print get_document_count(search_terms)
    # print get_paper_url(id)
    print get_paper_abstract(id)




if __name__ == '__main__':
    main()