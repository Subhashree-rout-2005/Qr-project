from flask import Flask, request, render_template_string
from analyzer import analyze_url

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>URL Safety Analyzer</title>
    <style>
        body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; }
        input[type=text] { width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box; }
        input[type=submit] { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; border: 1px solid #ccc; }
        .safe { background: #d4edda; }
        .suspicious { background: #fff3cd; }
        .dangerous { background: #f8d7da; }
        .error { background: #f8d7da; color: #721c24; }
        ul { margin: 10px 0 0; padding-left: 20px; }
    </style>
</head>
<body>
    <h2>URL Safety Analyzer - IBM Project</h2>
    <form method=post>
        <input type=text name=url placeholder="https://example.com" value="{{ url or '' }}" required>
        <input type=submit value="Analyze URL">
    </form>

    {% if error %}
    <div class="error">{{ error }}</div>
    {% endif %}

    {% if result %}
    <div class="result {{ result.verdict|lower }}">
        <h3>Verdict: {{ result.verdict }}</h3>
        <p><b>Risk Score:</b> {{ result.score }}/100</p>
        <p><b>Reasons:</b></p>
        <ul>
            {% for reason in result.reasons %}
            <li>{{ reason }}</li>
            {% endfor %}
        </ul>
    </div>
    {% endif %}
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None
    url = ''

    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        if not url:
            error = 'Please enter a URL.'
        else:
            result = analyze_url(url)

    return render_template_string(HTML, result=result, error=error, url=url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
