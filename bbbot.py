from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chatbot.html')

symptoms_dict = {
     "Influenza (flu)": ["fever", "cough", "sore throat", "muscle aches", "fatigue", "headache"],
    "Strep throat": ["sore throat", "fever", "swollen Glands in the Neck", "difficulty swallowing"],
    "Ear infection": ["ear Pain", "fever", "drainage from the ear", "hearing Loss"],
    "Bronchitis": ["cough", "Wheezing", "chest tightness", "shortness of breath"],
    "Pneumonia": ["fever", "cough", "shortness of breath", "chest Pain"],
    "Gastroenteritis (stomach flu)": ["Nausea", "Vomiting", "diarrhea", "stomach cramps"],
    "Urinary tract infection (UTI)": ["frequent Urination", "burning Pain during Urination", "cloudy Urine"],
    "Sinusitis": ["facial Pain", "Pressure", "congestion", "Runny Nose", "Post-Nasal drip"],
    "Tuberculosis (TB)": ["cough", "fever", "Night sweats", "Weight Loss", "Loss of appetite"],
    "Malaria": ["fever", "headache", "chills", "Muscle aches", "fatigue"],
    "HIV/AIDS": ["fatigue", "Weight Loss", "fever", "Night sweats", "swollen Glands"]
}

disease_names = [
        "Influenza (flu)",
    "Strep throat",
    "Ear infection",
    "Bronchitis",
    "Pneumonia",
    "Gastroenteritis (stomach flu)",
    "Urinary tract infection (UTI)",
    "Sinusitis",
    "Tuberculosis (TB)",
    "Malaria",
    "HIV/AIDS"
]

dis = "Influenza (flu)"
first_interaction = True  # Flag to track the first interaction

def mapquestion():
    global dis

    if symptoms_dict[dis]:
        return f"Do you have {symptoms_dict[dis].pop(0)}?"
    else:
        disease_names.remove(dis)
        if disease_names:
            dis = disease_names[0]
            return f"Do you have {symptoms_dict[dis].pop(0)}?"
        else:
            return f"You may have {dis}. Please consult a doctor."
x=0
current_dis=[]
@app.route('/get', methods=['POST'])
def get_response():
    global dis, first_interaction,x

    user_message = request.form.get('msg').lower()

    if first_interaction:
        first_interaction = False
        return jsonify({"bot_response": "Welcome to diagnosis!<br> Answer honestly for an accurate result!!! <br> Type 'start' to begin the test."})

    if user_message == 'start':
        return jsonify({"bot_response": f"Do you have {symptoms_dict[dis][x]}?"})
    elif user_message == 'yes':
        current_dis.append(symptoms_dict[dis][x])
    
        if x==len(symptoms_dict[dis])-1:
            return jsonify({"bot_response": f"You have "+dis})
        else:
            x+=1
            return jsonify({"bot_response": f"Do you have {symptoms_dict[dis][x]}?"})
    elif user_message == 'no':
        disease_names.remove(dis)
        if disease_names:
            dis = disease_names[0]
            x=0
            return jsonify({"bot_response": f"Do you have {symptoms_dict[dis][x]}?"})
        else:
            return jsonify({"bot_response": "You may have a disease. Please consult a doctor."})
    else:
        return jsonify({"bot_response": "Invalid input"})

if __name__ == '__main__':
    app.run(debug=True)