
# This is the "generate_concept_HTML" function 
# which will take a list of concepts (each of which is itself a list)
# and will return the appropriate string of HTML.
# I added h3, and would like to add h1 and h2, but first need to
# figure out the loop to happen only when needed.

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        <h3>''' + concept_title
    html_text_2 = '''</h3>
    </div>
    <div class="concept-description">
        <p>
        ''' + concept_description
    html_text_3 = '''
        </p>
    </div>
</div>
'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

# The make_HTML function
def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

# This is a list of concepts; note that you can have a list with three quotes.
EXAMPLE_LIST_OF_CONCEPTS = [ ['Python (this is h3)', """
    'Python is a Programming Language'<br>
    'I'd like to have a loop to add h1 and h2 only when needed.'<br>
    "section" is h1<br>
    "subsection" is h2<br>
    "concept" is h3<br>
    I also want to add my notes into this procedure;<br>
    however it will be a lot of work to reformat everything.<br>
"""],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]

# This is where you define how to add many concepts.
# This is their code; notice how elegant (mine didn't work):
def make_HTML_for_many_concepts(list_of_concepts):

    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML


print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
# The following is an example of the output.
"""
<div class="concept">
    <div class="concept-title">
        Python
    </div>
    <div class="concept-description">
        Python is a Programming Language
    </div>
</div>
<div class="concept">
    <div class="concept-title">
        For Loop
    </div>
    <div class="concept-description">
        For Loops allow you to iterate over lists
    </div>
</div>
<div class="concept">
    <div class="concept-title">
        Lists
    </div>
    <div class="concept-description">
        Lists are sequences of data
    </div>
</div>
"""

