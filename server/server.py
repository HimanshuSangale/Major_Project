from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

import BERT

# import your_bert_module
# import your_keybert_module

app = Flask(__name__)
CORS(app)
bert = BERT.Bert()


@app.route("/process_query", methods=["POST"])
def process_query():
    # query = request.args.get("query")
    data = request.get_json()
    query = data["query"]
    print(query)
    # print(query)
    # answer = ["Hey there!", "I am himanshu", "Trial test"]
    # Process the query using your BERT model
    # processed_query = your_bert_module.process(query)

    answer = bert.get_query(query)

    # Generate keywords using KeyBERT

    # Return the results as JSON

    # return query
    print(answer)
    return jsonify(answer)
    # return "<h1> Server is working fine! </h1>"


@app.route("/")
def index():
    return "<h1> Server is working fine! </h1>"


if __name__ == "__main__":
    app.run(debug=True)
