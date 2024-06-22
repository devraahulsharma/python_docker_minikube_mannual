from flask import Flask

app = Flask(__name__)
# app.run(host='0.0.0.0', port=5000)


@app.route('/')
def hello_world():
    return 'How to Create Kubernetes Deployments and Services using YAML files and Kubectl'

if __name__ == '__main__':
    app.run(debug=True)
