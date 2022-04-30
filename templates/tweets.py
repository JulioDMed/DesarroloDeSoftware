from flask import Flask, request ,render_template, make_response

app = Flask(__name__,template_folder="template")

tweets = []

@app.route("/")
def form():
    return render_template("tweet.html")

# vulnerable a XSS 
@app.route('/tweet_feed_insecure', methods=['GET', 'POST'])
def tweet_feed_insecure():
    if request.method == 'POST':
        tweet = request.form['tweet']
        tweets.append(tweet)
        html = "<title>Aqui estan tus mensajes</title>"
        for tweet in tweets:
            hmtl = html + "<h1>" + tweet + "<h1>"
            html = html + "<a href'" + tweet + "'>&#128147;</a>"
    return

# XSS mitigando usando Jinja2 
@app.route('/tweet_feed', methods=['GET','POST'])
def tweet_feed():
    if request.method == 'POST':
        tweet = request.form['tweet']
        tweets.append(tweet)
    Response = make_response(render_template('tweet_feed.html', tweets=tweets))
    Response.headers['Content-Security-Policy'] = "default-src 'self'"
    return Response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)