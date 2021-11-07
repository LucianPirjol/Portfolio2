from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('/index.html')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writter = csv.writer(database2, delimiter=',' , quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writter.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('/thank.html')
    else:
        return 'something went wrong'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
