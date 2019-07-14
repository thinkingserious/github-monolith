import os
from flask import Blueprint, jsonify, current_app, request, render_template
from github import Github
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/', methods=['GET'])
def hello_cold_monolith_world():
    return render_template('index.html', title='OSCON 2019')

@routes_blueprint.route('/github/prs', methods=['GET'])
def get_prs():
    prs = []
    repo = request.args.get('repo', type=str)
    g = Github(current_app.config['GITHUB_TOKEN'])
    repo = g.get_repo(repo)
    pulls = repo.get_pulls(state='open', sort='created')
    for pr in pulls:
        prs.append({"number": pr.number,"url": pr.url, "title": pr.title})
    return jsonify(prs), 200

@routes_blueprint.route('/github/issues', methods=['GET'])
def get_issues():
    items = []
    repo = request.args.get('repo', type=str)
    g = Github(current_app.config['GITHUB_TOKEN'])
    repo = g.get_repo(repo)
    issues = repo.get_issues(state='open', sort='created')
    for issue in issues:
        items.append({"number": issue.number,"url": issue.url, "title": issue.title})
    return jsonify(items), 200

@routes_blueprint.route('/email', methods=['POST'])
def send_email():
    r = request.get_json()
    message = Mail(
        from_email=r['from_email'],
        to_emails=r['to_email'],
        subject=r['subject'],
        html_content=r['content'])
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        return jsonify([{"message": str(e)}]), 500
    return jsonify([{"message": "success"}]), 200

@routes_blueprint.route('/sms', methods=['POST'])
def send_sms():
    r = request.get_json()
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    try:
        message = client.messages \
                        .create(
                            body=r['body'],
                            from_=r['from_number'],
                            to=r['to_number']
                        )
    except Exception as e:
        return jsonify([{"message": str(e)}]), 500
    return jsonify([{"message": "success"}]), 200
