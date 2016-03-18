Requirements:
- Create account and profile ✓
- Edit/update profile
- Create/edit/delete systematic review topics
- Construct boolean based queries:
	- Standard query box (expert mode)
	- Structural/Visual querying interface (novice mode)
- Show total number or hits a query would return
- Save/Edit/Delete queries
- Add/Remove results from a query/from the abstract pool
- Update abstract pool based on the set or queries
	- Warn the user about documents to be removed
- Show abstract pool of documents
- Judge abstracts in abstract pool
- View document pool
- View document through external link
- Finally mark document as relevant 
- View final set of relevant documents

PubMed API:
http://www.ncbi.nlm.nih.gov/home/api.shtml



Models to implement:
- Researcher
	- username
	- password
	- email
- Review
	- user 
	- title
	- description
	- date_started
	- query_string
	- pool_size
	- abstracts_judged
	- document_judged
- Paper
	- review
	- title
	- authors
	- abstract
	- publish_date
	- paper_url
	- abstract_relevance (boolean)
	- document_relevance (boolean)
- Query (optional, tie to Review)
	- review
	- string

Group Members:
1. Domantas Jurkus : Domantas Jurkus  2141380j
2. 2121159i        : Alex Irikov  2121159i
3. Panagiotis916   : Panagiotis Antoniou  2077368a
4. eliriel         : Borislav Hristov

Instructions:
 instructions on how to setup and run your application. Especially if you have some strange config,
 i.e. how to git clone, what to install for you ve, what population script to run, the names of users in the populations script, etc.