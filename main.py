from flask import Flask, render_template, request, send_file
import pyqrcode
import png
from pyqrcode import QRCode

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home_render():
  if request.method == "GET":
    return render_template("home.html")

  elif request.method == "POST":
    head = request.form['heading']
    body = request.form['body']
    link = request.form['link']
    split_list = link.split('.')
    source = split_list[1] + "." + split_list[2].split('/')[0]
    url = pyqrcode.create(link)
    url.png('./static/tech.png', scale=6)
    return render_template("result.html",
                           heading_text=head,
                           body_content=body,
                           source_info=source)


if __name__ == "__main__":
  app.run(debug=False, port='3000', host='0.0.0.0') 
