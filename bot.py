from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    x = 0
    return render_template('chatbot.html')
tempqns=["Do you have fever?<br>","Do you have cough?","Are you suffering from sore throat?","Do you have difficuly in swallowing food?","Do you have sowllen glands in the neck?","Do you have chest pain?","You have INFLUENZA (FLU)"]
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
prev = ""
dis = "Influenza (flu)"
symptom_index = 0
x=0
def mapquestion(x):
    global dis, symptom_index

    if x in symptoms_dict[dis]:
        symptom_index = symptoms_dict[dis].index(x)
        if symptom_index + 1 < len(symptoms_dict[dis]):
            next_symptom = symptoms_dict[dis][symptom_index + 1]
            return f"Do you have {next_symptom}?"
        else:
            provided_diseases.append(dis)
            provided_symptoms.append(x)
            disease_names.remove(dis)
            if disease_names:
                dis = disease_names[0]
                symptom_index = 0
                return f"Do you have {symptoms_dict[dis][0]}?"
            else:
                return f"You may have {', '.join(provided_diseases)}. Please consult a doctor."
    else:
        return "Invalid input"

symptomslist = ['chest tightness', 'ear pain', 'nausea', 'cough', 'fever', 'runny or stuffy nose', 'fever', 'headache', 'vomiting', 'muscle aches', 'cough', 'sore throat', 'chest pain', 'hearing loss', 'difficulty swallowing', 'wheezing', 'sore throat', 'fatigue', 'shortness of breath', 'drainage from the ear', 'sneezing', 'swollen glands in the neck', 'stomach cramps', 'diarrhea']
provided_diseases = []
provided_symptoms= []
symptoms = ['chest tightness', 'ear pain', 'nausea', 'cough', 'fever', 'runny or stuffy nose', 'fever', 'headache', 'vomiting', 'muscle aches', 'cough', 'sore throat', 'chest pain', 'hearing loss', 'difficulty swallowing', 'wheezing', 'sore throat', 'fatigue', 'shortness of breath', 'drainage from the ear', 'sneezing', 'swollen glands in the neck', 'stomach cramps', 'diarrhea']
ind=-1
@app.route('/get', methods=['POST'])
def get_response():
    global dis, symptom_index,prev,ind
    user_message = request.form.get('msg')

    if not user_message:
        welcome_message = "Welcome to diagnosis!<br> Answer honestly for an accurate result!!! <br> Type 'start' to begin the test.<br>Answer yes or no to the questions"
        return jsonify({"bot_response": welcome_message})
    elif user_message.lower() == 'start' or user_message.lower()=="yes":
        ind+=1
        if user_message.lower()=="yes":
            provided_symptoms.append(tempqns[ind-1])
        return jsonify({"bot_response": tempqns[ind]})
    elif user_message.lower() == 'no':
        ind+=1
        return jsonify({"bot_response": tempqns[ind]})
    else:
        return {"bot_response": "Invalid input"}
    #     return jsonify({"bot_response": f"Do you have {symptoms_dict[dis][0]}?"})
    # elif user_message.lower() == 'yes':  # Handle "yes" response
    #     return jsonify({"bot_response": mapquestion(prev)})
    # elif user_message.lower() == 'no':  # Handle "no" response
    #     if symptom_index + 1 < len(symptoms_dict[dis]):
    #         next_symptom = symptoms_dict[dis][symptom_index + 1]
    #         return jsonify({"bot_response": f"Do you have {next_symptom}?"})
    #     else:
    #         if disease_names:
    #             dis = disease_names[0]
    #             symptom_index = 0
    #             return jsonify({"bot_response": f"Do you have {symptoms_dict[dis][0]}?"})
    #         else:
    #             return jsonify({"bot_response": f"You may have {', '.join(provided_diseases)}. Please consult a doctor."})
    # elif user_message in symptomslist:
    #     prev = user_message
    #     return jsonify({"bot_response": mapquestion(user_message)})
    # else:
    #     return jsonify({"bot_response": "Invalid input"})

if __name__ == '__main__':
    app.run(debug=True)
