from flask import Flask, request, jsonify
from sending_emails import send_email_with_csv_summary
from dyanmodb_data_for_alerts import add_to_dynamodb
from aws_credentials import get_aws_credentials
from get_public_ip import get_public_ip
import requests

app = Flask(__name__)

@app.route('/subscribe-alert', methods=['POST'])
def subscribe_alert():
    try:
        data = request.json
        keyword = data.get("keyword")
        location = data.get("location")
        email = data.get("email")
        
        if not keyword or not location or not email:
            return jsonify({"error": "Missing keyword, location, or email"}), 400
        
        user_data = {
            'keyword': keyword,
            'location': location,
            'email': email
        }
        aws_creds = get_aws_credentials()
        access,secret,region,instance_id=aws_creds
        public_ip=get_public_ip(instance_id,region,access,secret)
        ec2_url = f"http://{public_ip}:5000/job-search"
        email_user = 'your_email@gmail.com'
        app_password = 'your_password'

        # Send to EC2 and get raw CSVs
        ec2_success, csv_data = send_to_ec2_and_get_csv(keyword, location, ec2_url)
        if not ec2_success:
            return jsonify({"error": "Failed to retrieve job data from EC2"}), 500
        
        # Send email with summary only (no attachments)
        email_success = send_email_with_csv_summary(email, keyword, location, csv_data, email_user, app_password)
        if not email_success:
            return jsonify({"error": "Failed to send email"}), 500
        
        # Store in DynamoDB
        
        table_name = 'Job_Alerts'
        db_success, subscription_id = add_to_dynamodb(aws_creds, table_name, user_data)
        
        return jsonify({
            "message": "Subscription successful",
            "subscription_id": subscription_id,
            "email_sent": email_success,
            "db_saved": db_success
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def send_to_ec2_and_get_csv(keyword, location, ec2_url):
    try:
        job_data = {
            "name": "Siddhant",
            "college": "VIT",
            "branch": "CSE",
            "keyword": keyword,
            "location": location,
            "experience": 1,
            "job_type": "fulltime",
            "remote": "on-site",
            "date_posted": "1 week",
            "company": "",
            "industry": "",
            "ctc_filters": "",
            "radius": "10",
            "Job_Alert": True
        }

        response = requests.post(ec2_url, json=job_data)

        if response.status_code == 200:
            try:
                return True, response.json()  # return raw CSVs
            except Exception:
                return False, None
        else:
            return False, None
    except Exception:
        return False, None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
