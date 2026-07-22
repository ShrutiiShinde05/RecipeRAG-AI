import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")


@app.route("/")
def index():
    """Render the Visualization Dashboard Agent page."""
    config = {
        "host_url":          os.getenv("WXO_HOST_URL", "https://au-syd.watson-orchestrate.cloud.ibm.com"),
        "agent_id":          os.getenv("WXO_AGENT_ID", ""),
        "crn":               os.getenv("WXO_CRN", ""),
        "orchestration_id":  os.getenv("WXO_ORCHESTRATION_ID", "undefined"),
        "deployment":        os.getenv("WXO_DEPLOYMENT_PLATFORM", "ibmcloud"),
    }
    return render_template("index.html", config=config)


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    port  = int(os.getenv("PORT", 5000))
    app.run(debug=debug, port=port)
