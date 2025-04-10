from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
import requests
import random
import argparse

app = Flask(__name__)

DBHOST = os.environ.get("DBHOST") or "localhost"
DBUSER = os.environ.get("DBUSER") or "root"
DBPWD = os.environ.get("DBPWD") or "wordpass"
DATABASE = os.environ.get("DATABASE") or "employees"
COLOR_FROM_ENV = os.environ.get('APP_COLOR') or "lime"
DBPORT = int(os.environ.get("DBPORT"))

# Amazon S3 Bucket URL (replace with your actual S3 URL or image path)
S3_BUCKET_URL = "https://clo835-project-s3.s3.us-east-1.amazonaws.com/JGibson.jpg" # Check URL after creation
# S3_BUCKET_URL = 'https://clo835-project-s3.s3.us-east-1.amazonaws.com/JGibson.jpg?response-content-disposition=inline&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLWVhc3QtMSJHMEUCIE0xPu0ryRBoMDLC84p%2FQioSbyQvvPJFDAnMZLs3GrLJAiEArGZwpDV6y4qmu6ZoHHggZbuEQ89A8XggGv1T1IPMBrwq2gMIfRABGgwxMzQ5ODY4MDA5MzgiDCq2qn8nX8sVoGcWTiq3AyNEZp7hduVJ%2BMPCTN4%2F%2FTEg%2FBJJGmxCEO0m8HOlu3stPLUzGlI%2B5jl3NrbuJj1c5k3ImLea%2BPsd4Y%2FSCla3CmRkKKys8aOrdVwZYBVFHyGx%2Bm65Xk10l%2F5EuPDWo8LNU5uFQ6qsfK5dXWM8og1MtuhEZnVpttKKpHqyLclRt32b0UcbZfKcPVoQLAfheH941x6qgUgBNh%2FWO33cowhBqYOkgLElz9sQFfruWHlDnZU0MddRcVdDf%2FudW0zwNPjqkzRjozA66gz4orZsG%2FaTlcxVdCVe6XEalaghzzBxULnQ1pG8l%2Bhm8uJJX9HkZDuGlajdTifUqaYe%2Fx2ke1chQvMneTfG0nG8%2Fsu0Z9YgEtYm3zJnhk1dOcugc8%2Bvb8fHHj4qSId%2F2IYIZwDSaknx7UJdOaPuzZqNcmNzHCFaUEuVtIV9GyEPWcjsSLQTMAspjbbc9KxfPZk1vJQsy7K1c6Ok%2B4cWSmiwbYOuxaYI0mVENvPpFYhui%2BLqjc%2BADWuadvivJv2Q9%2FBG1V0KJYqb0%2FgDNEyBgozrYeS%2FwFKamTQXt3tPNyyIPH4M6Txlkvz4phx3vdUNuEEwg%2FHVvwY6twKtJoEsMC5sI%2FZFx%2FVhhpv%2Fsq3RUDs4ohE6l9w5vglSaKTiOlFHRKVAe9BN%2BoblNvWMmR2dCUHu6Mx1yyhMyaLmQtIH39gCsg%2B%2FcU9GZHcWl6fDB0tC3n7Dt149AcDSE2Givz1aZl1zGXwrY8fwmGEBr6LUGOSx8tB89ZVXWJQw0wAwPwHZCCTNyNK3cNmd3uFJ%2BgrcpgDYDcXupz%2B0hIqiNvhqjTUtGHljskuc4%2FOVFxEhBmDsVc%2FYXPN2aoO0J8JDTCWEvYwD%2FaWpGeVS5TiGWPl3mwSTNdXsnRcr3PpOpWXOWhWJWhYO71sBd%2FLGM1WedmcyTg2ckRYxu%2FaCjWPELYHB08DH44tG4kAiOALTvQMWKaGBXOXvScxHOxxjJ84dJ1iz%2BanGVIIOg8wsYDhCNtA1%2BFDQvQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAR63OXD4VLNRTGNDY%2F20250408%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250408T200643Z&X-Amz-Expires=43200&X-Amz-SignedHeaders=host&X-Amz-Signature=dfee176fb7af830078eae4465ae04c4f0d18f4d16046334e29cc84ca201f00ff'

# s3 = boto3.client('s3')

# bucket_name = 'clo835-project-s3'
# object_key = 'JGibson.jpg'

# response = s3.get_object(Bucket=bucket_name, Key=object_key)

# image_data = response['Body'].read()

# with open('downloaded_test.jpg', 'wb') as f:
#     f.write(image_data)

# print("Image downloaded successfully!")

# TEST CODE

# Retrieve the S3 URL from the environment variable
# s3_image_url = os.getenv('S3_BUCKET_URL')
# s3_image_url = S3_BUCKET_URL

# # Example: Fetch the image from S3 using requests
# response = requests.get(s3_image_url)

# if response.status_code == 200:
#     with open('JGibson.jpg', 'wb') as f:
#         f.write(response.content)
# else:
#     print(f"Failed to fetch image: {response.status_code}")

# TEST CODE END

# Create a connection to the MySQL database
db_conn = connections.Connection(
    host= DBHOST,
    port=DBPORT,
    user= DBUSER,
    password= DBPWD, 
    db= DATABASE
)

output = {}
table = 'employee'

@app.route("/", methods=['GET', 'POST'])
def home():
    # Pass S3 URL instead of color
    return render_template('addemp.html', background_image=S3_BUCKET_URL)

@app.route("/about", methods=['GET', 'POST'])
def about():
    # Pass S3 URL instead of color
    return render_template('about.html', background_image=S3_BUCKET_URL)

@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    primary_skill = request.form['primary_skill']
    location = request.form['location']

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    try:
        cursor.execute(insert_sql, (emp_id, first_name, last_name, primary_skill, location))
        db_conn.commit()
        emp_name = "" + first_name + " " + last_name

    finally:
        cursor.close()

    return render_template('addempoutput.html', name=emp_name, background_image=S3_BUCKET_URL)

@app.route("/getemp", methods=['GET', 'POST'])
def GetEmp():
    return render_template("getemp.html", background_image=S3_BUCKET_URL)

@app.route("/fetchdata", methods=['GET', 'POST'])
def FetchData():
    emp_id = request.form['emp_id']
    output = {}
    select_sql = "SELECT emp_id, first_name, last_name, primary_skill, location from employee where emp_id=%s"
    cursor = db_conn.cursor()

    try:
        cursor.execute(select_sql, (emp_id))
        result = cursor.fetchone()

        output["emp_id"] = result[0]
        output["first_name"] = result[1]
        output["last_name"] = result[2]
        output["primary_skills"] = result[3]
        output["location"] = result[4]

    except Exception as e:
        print(e)

    finally:
        cursor.close()

    return render_template("getempoutput.html", id=output["emp_id"], fname=output["first_name"],
                           lname=output["last_name"], interest=output["primary_skills"], location=output["location"],
                           background_image=S3_BUCKET_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)