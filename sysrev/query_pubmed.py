import sys              # For command-line arguments
import urllib
import urllib2          # For querying pubmed
import xmltodict        # For transforming XML responses to dictionaries

# Query PubMed and return the entire result as a dictionary
def query_pubmed(search_terms):

    # Format the terms to be included in the URL
    url_term = urllib.quote(search_terms)

    # API docs: http://www.ncbi.nlm.nih.gov/home/api.shtml
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='+url_term
    # results_per_page = 10
    # offset = 0

    results = []

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


# Query PubMed for info on a particular paper
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


# Get paper URL (PubMed, why?)
def get_paper_url():

    return None



# Main function for testing
def main():

    if len(sys.argv) != 2:
        print "Error: I need ONE string as a query parameter"
        return

    id = sys.argv[1]
    # print get_document_count(search_terms)
    print get_paper_info(id)




if __name__ == '__main__':
    main()