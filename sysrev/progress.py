from sysrev.models import *

# Functions for calculating progress on
# abstract/document evaluation

def get_progress(review, stage):

    try:
        papers_all = len(Paper.objects.filter(review=review))

        if stage == "abstract":
            papers_done = len(Paper.objects.filter(review=review, abstract_rev="Yes"))
        elif stage == "document":
            papers_done = len(Paper.objects.filter(review=review, document_rev="Yes"))
        else:
            raise Exception("Invalid review stage provided")

        print papers_all
        print papers_done

        return (papers_done*100/papers_all)

    except:
        print "Unable to get papers"
