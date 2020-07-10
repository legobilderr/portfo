from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def myhome():
    return render_template('index.html')


def write_too_file(data):
    with open('database.txt', mode='a') as databese:
        email = data['email']
        subject = data['subject']
        message = data['message']
        databese.write(f'\n{email},{subject},{message}')


def write_too_csv(data):
    with open('database.csv', newline='', mode='a') as databese2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # databese2.write(f'\n{email},{subject},{message}')
        csv_writer = csv.writer(databese2, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/<string:page_name>')
def dainamek(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_too_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'
