from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import os

app = Flask(__name__, static_url_path='/static')

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'ra_pipe.pkl')
try:
    pipe = pickle.load(open(model_path, 'rb'))
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def predict():
    batting_team = ''
    bowling_team = ''
    win_probability = 0
    loss_probability = 0
    
    if request.method == 'POST':
        try:
            batting_team = request.form['batting_team']
            bowling_team = request.form['bowling_team']
            selected_city = request.form['selected_city']
            
            target = int(request.form['target'])
            score = int(request.form['score'])
            balls_left = int(request.form['balls_left'])
            wickets = int(request.form['wickets'])

            runs_left = target - score
            wickets_remaining = 10 - wickets
            overs_completed = (120 - balls_left) / 6
            crr = score / overs_completed if overs_completed > 0 else 0
            rrr = runs_left / (balls_left / 6) if balls_left > 0 else 0

            input_data = pd.DataFrame({
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'city': [selected_city],
                'runs_left': [runs_left],
                'balls_left': [balls_left],
                'wickets_remaining': [wickets_remaining],
                'total_run_x': [target],
                'crr': [crr],
                'rrr': [rrr]
            })
            
            result = pipe.predict_proba(input_data)

            win_probability = round(result[0][1] * 100)
            loss_probability = round(result[0][0] *  100)

            return render_template('result.html', 
                                   batting_team=batting_team, 
                                   bowling_team=bowling_team, 
                                   win_probability=win_probability, 
                                   loss_probability=loss_probability)
        except FileNotFoundError:
          return render_template('error.html', error_message='Model file not found.')
        except Exception as e:
          return render_template('error.html', error_message=f'Error loading model: {e}') 
    else:
        return render_template('result.html', batting_team='', 
                               bowling_team='', 
                               win_probability=0, 
                               loss_probability=0)

if __name__ == '__main__':
    app.run(debug=True)
