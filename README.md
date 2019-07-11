# GitHub Multi-Repo Management Monolith

This is sample code for a OSCON 2019 tutorial: https://conferences.oreilly.com/oscon/oscon-or/public/schedule/detail/76039

## Installation

```bash
git clone https://github.com/thinkingserious/github-monolith.git
cd github-monolith
```

* Update `.env_sample`.
* Open `examples/*` and update the repos in `all_repos`.
* Open `examples/send_emails` and update the email in the `send_email` function.
* Open `examples/send_sms` and update the to and from phone numbers in the `send_sms` function.

```bash
mv ./.env_sample ./.env
source .env
docker-machine create -d virtualbox github-manager-monolith
eval "$(docker-machine env github-manager-monolith)"
export GITHUB_MANAGER_IP="$(docker-machine ip github-manager-monolith)"
docker-compose -f docker-compose-dev.yml up -d --build
curl http://$GITHUB_MANAGER_IP
```

## Quickstart

Go to `http://<$GITHUB_MANAGER_IP>` in your browser.

```bash
python examples/get_all_issues.py
python examples/get_all_prs.py
python examples/send_email.py
python examples/send_sms.py
```

# References
* https://github.com/sendgrid/github-automation
* https://github.com/sendgrid/dx-automator
* https://github.com/miguelgrinberg
* https://github.com/testdrivenio/testdriven-app-2.5
* https://github.com/realpython/orchestrating-docker
* http://flask.pocoo.org/docs/1.0
