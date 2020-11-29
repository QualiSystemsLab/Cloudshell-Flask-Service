from flask import Flask, request, jsonify, render_template, Response
from cloudshell.api.cloudshell_api import CloudShellAPISession
import json
from time import sleep

app = Flask(__name__)

# cloudshell api details
user = "admin"
password = "admin"
host = "localhost"
domain = "Global"


@app.route('/')
def sanity():
    return "Cloudshell Demo Service is online!"


@app.route("/<domain>")
def show_blueprints_per_domain(domain):
    return render_template('index.html', domain=domain)


@app.route("/<domain>/blueprint")
def get_domain_blueprints(domain):
    """
    get blueprint data from api and send back as JSON
    to be consumed by AJAX request from client
    """
    # simulate mock command time
    sleep(3)
    try:
        api = CloudShellAPISession(host=host, username=user, password=password, domain=domain)
        blueprints_data = api.GetDomainDetails(domain).Topologies
    except Exception as e:
        exc_msg = "Error occurred making cloudshell api call: {}".format(str(e))
        response_data = {"msg": exc_msg, "code": 400}
        json_response_data = json.dumps(response_data)
        return Response(json_response_data, status=400, mimetype='application/json')

    blueprints_data_dicts = [obj.__dict__ for obj in blueprints_data]
    return jsonify(blueprints_data_dicts)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8900, debug=True)