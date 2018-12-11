from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", input_data=dropdown,
                           output="You're a wizard %s." % name)
#change the example select title favorite chicken nugget spot
#favorie sauces in Example multiple select
# change the example selects to chicken nugget spots
# change example multiple selects to sauces
# change example text area to tell us more about your love for chicken nuggets
#change youre a Wizard to dif things based on answer chick-fil-a and
