# Importing essential libararies and modules

from flask import Flask, render_template

# ------------------------------------ FLASK APP -------------------------------------------------

app =Flask(__name__)

#home page

@app.route('/')
def home():
  title = 'Kruषक - Home'
  return render_template('index.html', title=title)

# ===============================================================================================

if __name__ == '__main__':
  app.run(debug=False)

