from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import tempfile
import json

app = Flask(__name__)
CORS(app)

PROJECT_DIR = r"C:\Users\1\Desktop\Object"
MVN = r"C:\apache-maven-3.9.16\bin\mvn.cmd"

@app.route('/scan', methods=['POST'])
def scan():
    code = request.json.get('code', '')
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.java', delete=False, encoding='utf-8') as f:
        f.write(code)
        tmpfile = f.name
    
    try:
        result = subprocess.run(
            [MVN, 'exec:java', '-Dexec.mainClass=com.scanner.core.Main', 
             '-Dexec.args=' + tmpfile, '-q'],
            cwd=PROJECT_DIR,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = result.stdout.strip()
        if output.startswith('['):
            return jsonify(json.loads(output))
        return jsonify([])
    except Exception as e:
        return jsonify([])
    finally:
        os.unlink(tmpfile)

if __name__ == '__main__':
    app.run(debug=True, port=5000)