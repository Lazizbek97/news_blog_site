from flask import Flask, render_template, request
import requests
import smtplib

my_email = "email@gamil.com"
my_password = "passowrd"

blog_content_api = "https://api.npoint.io/433c872e6ed17e732d59"

app = Flask(__name__)

@app.route('/')
def home_page():
    response = requests.get(url=blog_content_api)
    content = response.json()
    return render_template("index.html", articles = content)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact', methods = ["GET", "POST"])
def contact_page():
    if request.method == "POST":
        email = request.form["email"]
        text = request.form["message_text"]
        server = smtplib.SMTP("smtp.gmail.com")
        server.starttls()
        server.login(my_email, my_email)
        server.sendmail(from_addr=my_email, to_addrs="email@gmail.com", msg=f"{email}.\n message: {text}")
        print(email, text)
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")


@app.route('/post')
def post_page():
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True)



























