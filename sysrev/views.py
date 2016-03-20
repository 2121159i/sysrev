from django.shortcuts import render
from sysrev.forms import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from sysrev.query_pubmed import *
from django.contrib.auth.models import User

# Old Rango views (delete if no reference is needed)

def about(request):
    context_dict = {'boldmessage': "Hello from about bold"}

    if request.session.get('visits'):
        count = request.session.get('visits')
    else:
        count = 0

    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).seconds > 5:
            count += 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = count

    context_dict['visits'] = count

    return render(request, 'sysrev/about.html', context_dict)


def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = ResearcherForm(data=request.POST)

        # If the two forms are valid...
        username = request.POST.get('username')
        try:
            checkUser = User.objects.get(username=username)
            if checkUser:
                print 9999999
                return render(request, 'registration/register.html',
                              {'user_form': user_form, 'profile_form': profile_form, 'register_error': True,
                               'error_type': 'The username is already taken'})
        except Exception as e:
            None

        if user_form.is_valid() and profile_form.is_valid():

            password = request.POST.get('password')
            repeatPassword = request.POST.get('repeatPassword')
            email = request.POST.get('email')

            try:
                check_email = User.objects.get(email=email)
                if check_email:
                    return render(request, 'registration/register.html',
                                  {'user_form': user_form, 'profile_form': profile_form, 'register_error': True,
                                   'error_type': 'The email is already taken'})
            except Exception as v:
                None
            if (password != repeatPassword):
                return render(request, 'registration/register.html',
                              {'user_form': user_form, 'profile_form': profile_form, 'register_error': True,
                               'error_type': 'The passwords don\'t match'})


            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True


        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = ResearcherForm()

    # Render the template depending on the context.
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    logged_in_error = False;
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
        # because the request.POST.get('<variable>') returns None, if the value does not exist,
        # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')


        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/sysrev/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your sysrev account is disabled.")
        else:
            logged_in_error = True;
            # Bad login details were provided. So we can't log the user in.
            # print "Invalid login details: {0}, {1}".format(username, password)
            #return HttpResponseRedirect("/sysrev/login")
            return render(request, 'registration/login.html', {'logged_in_error': logged_in_error})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'registration/login.html', {'logged_in_error': logged_in_error})


@login_required
def user_logout(request):
    # Use the login_required() decorator to ensure only those logged in can access the view.
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/sysrev/')


def category(request, category_name_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        context_dict['category_name_slug'] = category.slug

        context_dict['testData'] = {
        {'title': 'title of the document',
         'description': 'description of the data'},
        {'title': 'another title of the document',
         'description': 'another description of the data'}
        }
        context_dict['testNumberofDocumentsLeft'] = 500

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'sysrev/category.html', context_dict)


def viewed_documents(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'sysrev/viewed_documents.html', context_dict)


def track_url(request):
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']

            form = CategoryForm(page_id)

            # Have we been provided with a valid form?
            if form.is_valid():
                # Save the new category to the database.
                form.save(commit=True)

                # Now call the index() view.
                # The user will be shown the homepage.
                return index(request)
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors

    return HttpResponseRedirect('/sysrev/')


# ----- Sysrev views -----

def index(request):
    # If the user is logged in - redirect to dashboard
    if request.user.username:
        return HttpResponseRedirect('/sysrev/dashboard/')

    return HttpResponseRedirect('/sysrev/login/')


@login_required
def dashboard(request):
    context_dict = {}

    user = Researcher.objects.get(user__username=request.user.username)

    reviews = Review.objects.filter(user=user)

    context_dict['reviews'] = []

    for review in reviews:
        local_dict = {}
        local_dict['id'] = review.id
        local_dict['title'] = review.title
        local_dict['description'] = review.description
        local_dict['query_string'] = review.query_string

        # local_dict['documents_left'] = 10000
        # local_dict['abstracts_kept'] = 10
        # local_dict['documents_kept'] = 10
        # local_dict['documents_discarded'] = 10
        #
        # local_dict['kept_perc'] = 10
        # local_dict['documents_discarded'] = 30
        # local_dict['discarded_perc'] = 30
        # local_dict['documents_left'] = 10000-10-300
        # local_dict['left_perc'] = ((10000-10-300)/10000)*100

        local_dict['documents_all'] = 10000
        local_dict['abstracts_done'] = 100
        local_dict['documents_done'] = 20

        context_dict['reviews'].append(local_dict)

    response = render(request, 'sysrev/dashboard.html', context_dict)

    return response


def review(request, id):
    return_dict = {}

    # Try and find the review
    try:
        review = Review.objects.get(id=id)
        print review
        return_dict['title'] = review.title
        return_dict['description'] = review.description
        return_dict['query_string'] = review.query_string
        print "Review found"
    except:
        return JsonResponse({"message": "Cannot find review with id " + str(id)})

    papers = Paper.objects.filter(review=review, abstract_rev=None)

    # If there are unevaluated abstracts
    if len(papers) != 0:
        return_dict['stage'] = "abstract"
        return_dict['papers'] = papers
        for paper in papers:
            print type(paper.abstract)
        print "Found papers with abstract_rev=None"
        return render(request, 'sysrev/review.html', return_dict)

    # If all abstracts have been evaluated
    else:
        papers = Paper.objects.filter(review=review, abstract_rev=True, document_rev=None)

        # If there are unevaluated documents
        if len(papers) != 0:
            return_dict['stage'] = "document"
            return_dict['papers'] = papers
            print "Found papers with document_rev=None"
            return render(request, 'sysrev/review.html', return_dict)

        # Else, the review is completed
        else:
            papers = Paper.objects.filter(
                review=review,
                abstract_rev=True,
                document_rev=True
            )
            return_dict['stage'] = "done"
            return_dict['papers'] = papers
            print "Review completed"
            return render(request, 'sysrev/review.html', return_dict)


# Rename this to 'add_review' or 'create_review' when possible
@login_required
def add_category(request):
    # Rename this to 'add_review' or 'create_review' when possible

    # Check if a new review is posted
    if request.method == 'POST':

        title = request.POST['title']
        description = request.POST['description']
        query_string = request.POST['query_string']

        user = User.objects.get(username=request.user)
        researcher = Researcher.objects.get(user=user)

        # Make a new Review and save it
        review = Review(
            user=researcher,
            title=title,
            description=description,
            query_string=query_string
        )
        review.save()

        # Query PubMed to get a list of paper IDs
        id_list = get_id_list(query_string)
        print id_list

        # Count the number of bad pages
        # (some papers may get excluded if their links are not found)
        count_bad = 0
        count_good = 0
        count_total = 0

        # Loop through each ID
        for id in id_list['Id']:
            count_total += 1
            paper_dict = {}
            paper_dict = get_paper_info(id)

            # We may fail getting the paper URL
            # If that's the case - skip this document
            paper_url = get_paper_url(id)
            if paper_url == None:
                print "Unable to get URL for:", id
                count_bad += 1
                continue


            abstract = str(get_paper_abstract(paper_dict))

            # print "Abstract:", type(abstract)
            # print "Abstract:", abstract

            if abstract == "":
                print "Unable to get abstract for:", id
                count_bad += 1
                continue

            paper = Paper(
                review=review,
                title=get_paper_title(paper_dict),
                authors=get_paper_author(paper_dict),
                abstract=abstract,
                paper_url=paper_url
            )
            paper.save()
            count_good += 1
            print "Saved ID", id

        print "All:", count_total
        print "Good:", count_good
        print "Bad:", count_bad

        # Yay, it works up to here! Go back to main page
        return HttpResponseRedirect('/sysrev/')

    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'sysrev/add_category.html', {'form': form})


@login_required
def delete_review(request, id):
    # Delete a review

    try:
        # First, delete all papers associated with the review
        review = Review.objects.filter(id=id)
        Paper.objects.filter(review=review).delete()

        # Then get rid of the review itself
        review.delete()
        return HttpResponseRedirect('/sysrev/dashboard')

    except:
        return JsonResponse({"message": "Unable to delete review"})


@login_required
def mark_abstract(request, id, rel):
    # Parameters are passed as strings
    if rel == "1":
        rel = True
    else:
        rel = False

    try:
        # Mark the paper abstract as (not)relevant
        paper = Paper.objects.get(id=id)
        paper.abstract_rev = rel
        paper.save()

        return HttpResponseRedirect('/sysrev/review/' + str(paper.review.id))

    except:
        return JsonResponse({"message": "Something went wrong"})


@login_required
def mark_document(request, id, rel):
    print "mark_document()"

    # Parameters are passed as strings
    if rel == "1":
        rel = True
    else:
        rel = False

    try:
        # Mark the document as (not)relevant
        paper = Paper.objects.get(id=id)
        paper.document_rev = rel
        paper.save()
        print "Marked paper as relevant:", paper

        return HttpResponseRedirect('/sysrev/review/' + str(paper.review.id))

    except:
        return JsonResponse({"message": "Something went wrong"})


def final(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'sysrev/final.html', context_dict)


def done(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'sysrev/done.html', context_dict)


def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'sysrev/add_page.html', context_dict)


def get_doc_count(request):
    # Make sure it's a Get request with a 'query' parameter
    if request.method != 'GET':
        return "/get_document_count must be a GET request"

    if not request.GET['query']:
        return "No 'query' parameter"

    query = request.GET['query']
    print query
    count = get_document_count(query)

    print "got " + str(count)

    return JsonResponse({"count": count})


def update_password(request):
# If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        # If the two forms are valid...
        password = request.POST.get('password')
        repeatPassword = request.POST.get('repeatPassword')
        try:
            user = User.objects.get(id = request.user.id)
        except Exception as v:
            return render(request, 'sysrev/update_password.html', {'update_success': False , 'update_error': True, 'error_type': 'Unexpected error, please try again later'})


        if (password != repeatPassword):
            return render(request, 'sysrev/update_password.html', {'update_success': False , 'update_error': True, 'error_type': 'The passwords don\'t match'})
		# Now we hash the password with the set_password method.
		# Once hashed, we can update the user object.
        user.set_password(password)
        user.save()
        return render(request, 'sysrev/update_password.html', {'update_success': True , 'update_error': False, 'error_type': ''})
    else:
        # Render the template depending on the context.
        return render(request, 'sysrev/update_password.html', {'update_success': False , 'update_error': False, 'error_type': ''})


def update_email(request):
    try:
        user = User.objects.get(id=request.user.id)
    except Exception as v:
        return render(request, 'sysrev/update_password.html', {'update_success': False , 'update_error': True, 'error_type': 'Unexpected error, please try again later'})

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        email = request.POST.get('email')


		# Now we hash the password with the set_password method.
		# Once hashed, we can update the user object.
        user.email = email
        user.save()
        return render(request, 'sysrev/update_email.html', {'update_success': True , 'update_error': False, 'error_type': '' , 'email':user.email})
    # Render the template depending on the context.
    return render(request, 'sysrev/update_email.html', {'update_success': False , 'update_error': False, 'error_type': '' , 'email':user.email})


def update_profile(request):
    return render(request, 'sysrev/update_profile.html', {})
