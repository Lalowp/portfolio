from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email_1 = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email_1},{subject},{message}')

def write_to_csv(data):
    with open('datbase.csv', mode='a') as database2:
        email_1 = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',' ,quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email_1,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_info():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return redirect('/failmsg.html')

