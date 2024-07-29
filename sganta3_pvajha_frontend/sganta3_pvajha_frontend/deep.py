from language_translation_function import translate
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/form')
# def form():
#     return render_template('form.html')

@app.route('/first', methods=['POST'])
def translate_text():
    if request.method == 'POST':
        input_sentence = request.form['query']
        translated_df = translate(input_sentence)
        print(translated_df)
        return render_template('first_page.html', translated_df=translated_df)

if __name__ == '__main__':
    print("Hello world")
    app.run(debug=True)