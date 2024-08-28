from flask import Flask, render_template, jsonify
import boto3

app = Flask(__name__)

# Configurar boto3 para acceder a S3
s3 = boto3.client('s3')

@app.route('/')
def list_buckets():
    # Obtener la lista de buckets
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return render_template('buckets.html', buckets=buckets)

@app.route('/api/buckets')
def api_list_buckets():
    # Obtener la lista de buckets
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return jsonify(buckets)

if __name__ == '__main__':
    app.run(debug=True)