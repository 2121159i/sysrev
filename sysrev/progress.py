from sysrev.models import *

# Functions for calculating progress on
# abstract/document evaluation

def get_progress(review, stage):

    # Try getting the paper instances
    try:
        papers_all = len(Paper.objects.filter(review=review))

        # Check which progress bar we wish to calculate
        if stage == "abstract":
            papers_done = len(Paper.objects.filter(review=review, abstract_rev="Yes"))
        elif stage == "document":
            papers_done = len(Paper.objects.filter(review=review, document_rev="Yes"))
        else:
            raise Exception("Invalid review stage provided")

        return (papers_done*100/papers_all)

    # If a DB issue occurs
    except:
        print "Unable to get papers"
