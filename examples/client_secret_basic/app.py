from idpartner import IDPartner
from authlib.integrations.flask_client import OAuth
from flask import Flask, render_template, request, redirect, session, jsonify
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

app = Flask(__name__)
app.secret_key = config.get("cookie_secret")

oauth = OAuth(app)
id_partner = IDPartner(
    oauth,
    {
        "client_id": config.get("client_id"),
        "client_secret": config.get("client_secret"),
        "account_selector_service_url": "http://localhost:9002",
        "redirect_uri": config.get("redirect_uri"),
    },
)


@app.route("/")
def index():
    title = "RP Client Secret Example"
    return render_template("index.html", title=title, config=config)


@app.route("/jwks")
def jwks():
    return jsonify(id_partner.jwks())


@app.route("/button/oauth")
def oauth():
    scope = config["scope"]
    proofs = id_partner.generate_proofs()
    session["proofs"] = proofs
    query_params = request.args.to_dict()
    return redirect(id_partner.get_authorization_url(query_params, proofs, scope))


@app.route("/button/oauth/callback")
def oauth_callback():
    query_params = request.args.to_dict()
    token = id_partner.token(query_params, session.get("proofs"))
    userinfo = id_partner.userinfo(token)
    return jsonify(userinfo)


if __name__ == "__main__":
    app.run(port=config.get("port"), debug=True)
