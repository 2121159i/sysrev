import json
import urllib, urllib2
import unirest
import xmltodict, json      # For transforming XML responses to dictionaries

# Query PubMEd with the given search terms
def query_pubmed_unirest(search_terms):

    search_terms = 'science[journal]+AND+breast+cancer+AND+2009[pdat]'

    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='+search_terms
    results_per_page = 10
    offset = 0

    try:
        print "Making request"
        response = unirest.get(url
            # , headers = { "Accept": "application/json" }
        )

        # print response.code # The HTTP status code
        # print response.headers # The HTTP headers
        # print response.body # The parsed response
        # print response.raw_body # The unparsed response

        return response.body

    except:
        print "Uh oh - could not make request"


def query_pubmed_urllib2(search_terms):

    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='+search_terms
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

    # query = raw_input('Enter query: ')

    # results = query_pubmed_unirest("cancer")
    results = query_pubmed_urllib2("cancer")
    print results



if __name__ == '__main__':
    main()