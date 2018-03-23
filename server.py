# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)
app.config['DEBUG'] = True

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    indv_file=request.form['indv_file']
    cm_file=request.form['cm_file']
    n=request.form['number']
    out_dir=request.form['out_dir']
    stats = benchmark.testing(int(n), indv_file, cm_file, out_dir)
    return render_template('form_action.html', 
        n_indv=stats[0], 
        n_cmte=stats[1],
        n_can_all=stats[2],
        n_can_ne=stats[3],
        n_com_all=stats[4],
        n_com_ne=stats[5],
        n_spac_all=stats[6],
        n_spac_ne=stats[7]
    )

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("80")
  )
