from flask import Flask, render_template
from cloudshell.api.cloudshell_api import CloudShellAPISession


app = Flask(__name__)

# cloudshell api details
user = "admin"
password = "admin"
host = "localhost"
domain = "Global"


def get_domain_blueprints(api, domain):
    """
    take api session and get blueprint details
    :param CloudShellAPISession api:
    :param domain:
    :return:
    """
    return api.GetDomainDetails(domain).Topologies

@app.route('/')
def sanity():
    return "Cloudshell Demo Service is online!"


@app.route("/domain/<domain>")
def show_blueprints_per_domain(domain):
    """
    make cloudshell api call to get domain info
    :param domain:
    :return:
    """
    api = CloudShellAPISession(host=host, username=user, password=password, domain=domain)
    blueprint_data = get_domain_blueprints(api, domain)
    return render_template('index.html', blueprints=blueprint_data, domain=domain)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8900, debug=True)