# Importing essential libararies and modules

from flask import Flask, render_template

# ------------------------------------ FLASK APP -------------------------------------------------

app =Flask(__name__)

#home page

@app.route('/')
def home():
  title = 'Kruषक - Home'
  return render_template('index.html', title=title)

# render crop recommendation form page


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Kruषक - Crop Recommendation'
    return render_template('crop.html', title=title)

# render fertilizer recommendation form page


@ app.route('/fertilizer')
def fertilizer_recommendation():
    title = 'Kruषक - Fertilizer Suggestion'

    return render_template('fertilizer.html', title=title)
# ===============================================================================================

if __name__ == '__main__':
  app.run(debug=False)

