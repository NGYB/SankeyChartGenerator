from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('sankey.html')
#	return render_template('index.html')
#	return render_template('vor_map.html')


if __name__ == "__main__":
#	app.run(host='0.0.0.0')
	app.run()
