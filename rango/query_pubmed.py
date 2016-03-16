import sys              # For command-line arguments
import urllib
import urllib2          # For querying pubmed
import xmltodict        # For transforming XML responses to dictionaries

def query_pubmed_urllib2(search_terms):

    # PubMed wants all spaces to be replaced with pluses
    url_term = search_terms.replace(" ", "+")
    print url_term

    # API docs: http://www.ncbi.nlm.nih.gov/home/api.shtml
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='+url_term
    results_per_page = 10
    offset = 0

    # Create a 'password manager' which handles authentication for us.
    # password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # password_mgr.add_password(None, search_url, username, BING_API_KEY)

    results = []

    try:
        # Prepare for connecting to Bing's servers.
        # handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        # opener = urllib2.build_opener(handler)
        # urllib2.install_opener(opener)

        # Connect to the server and read the response
        response_xml = urllib2.urlopen(url).read()

        # Convert the response to a Python dictionary
        response_dict = xmltodict.parse(response_xml)

        # Keys: "Count", "RetMax", "RetStart", "IdList"
        #       "TranslationSet", "TranslationStack"
        #       "QueryTranslation"
        print response_dict["eSearchResult"].keys()
        print response_dict["eSearchResult"]["Count"]

        '''stringIO = xml.dom.minidom.parseString(response)
        resultset = stringIO.getElementByTagName('http://www.inktomi.com/', 'resultset_web')
        rs = resultset[0]
        response.total_results = rs.getAttributes('totalhits')'''


        # Convert the string response to a Python dictionary object.
        # json_response = json.loads(response)

        # Loop through each page returned, populating out results list.
        '''
        for result in json_response['d']['results']:
            results.append({
                'title': result['Title'],
                'link': result['Url'],
                'summary': result['Description']
            })
        '''

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error using urllib2", e

    # Return the list of results to the calling function.
    return results


def main():

    if len(sys.argv) != 2:
        print "Error: I need ONE string as a query parameter"
        return

    search_terms = sys.argv[1]
    results = query_pubmed_urllib2(search_terms)
    print results



if __name__ == '__main__':
    main()