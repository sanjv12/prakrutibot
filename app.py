from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    x=0
    return render_template('chatbot.html')
questions=[[1,0,0,0],
    ['What is your body frame?<br>A. Thin and lean body frame<br>B. Medium build<br>C. Large and sturdy build'],
    ['What is your skin type?<br>A. Dry skin<br>B. Oily skin<br>C. Oily and thick skin'],
    ['What is your hair type?<br>A. Dry hair<br>B. Oily hair<br>C. Oily and thick hair'],
    ['What is your complexion?<br>Complexion: The natural colour and quality of the skin on your face.<br>A. Fair complexion<br>B. Medium complexion<br>C. Dark complexion'],
    ['What is your body weight?<br>A.UnderWeight<br>B.Normal Weight<br>C.Overweight'],
    ['What is your energy level?<br>A. Variable energy level<br>B. Moderate level<br>C. Steady  level'],
    ['What is your appetite like?<br>Appetite: Desire for food<br>A. Irregular appetite<br>B. Strong appetite<br>C. Regular appetite'],
    ['What is your Speed/Style of speaking?<br>A. Quick and Variable<br>B. Quick and Accurate<br>C. Slow and Deliberate.'],
    ['What is your tolerance to heat and cold?<br>A. Sensitive to cold<br>B. Sensitive to heat<br>C. Tolerant of both heat and cold'],
    ['What is your temperament?<br>A. Calm and gentle temperament<br>B. Active and competitive temperament<br>C. Calm and easygoing temperament'],
    ['What is your learning style?<br>A. Fast learner, but may forget quickly<br>B. Good learner and memory<br>C. Slow learner, but retains information well'],
    ['What is your memory like?<br>A. Moderately<br>B. Quickely<br>C. Slowly'],
    ['What is your concentration like?<br>A. Poor concentration<br>B. moderate concentration<br>C.Steady concentration'],
    ['What is your stress level like?<br>A.Low stress level<br>B. Medium stress level<br>C. High stress level'],
    ['What are your emotional tendencies?<br>A. Happy and cheerful disposition<br>B. Intelligent and ambitious disposition<br>C. Gentle and compassionate disposition'],
    ['what is your diet like?<br>A.Light diet<br>B.Heavy diet<br>C.Irregular diet'],
    ['what is your exercise routine like?<br>A.Irregular exercise routine<br>B.Regular exercise routine<br>C.Variable'],
    ['what is your sleep schedule like?<br>A.Irregular sleep schedule<br>B.Regular sleep schedule<br>C.Variable'],
    ['Do you have any specific cravings or aversions?<br>A.Cravings for sweet ans salty foods<br>B.Cravings for bitter and sour foods<br>C.Cravings for sweet and fatty foods'],
    ['Are you sensitive to certain foods,weather conditions,or other environmental factors?<br>A.Aversion to cold and windy weather<br>B.Aversion to hot and windy weather<br>C.Aversion to cold and windy weather'],
    ['How frequently do you fall ill?<br>A.Frequently<br>B.Rarely<br>C.Moderately'],
    ['Amount of speaking<br>A.Excessive<br>B.Less<br>C,Moderately'],
    ['How frequently do you feel tired?<br>A.On doing routine work<br>B.After doing routine work/heavy work<br>C.Not even after heavy work'],
    ['How about your perspiration (Sweating)? <br>A.Profuse<br>B.Moderate<br>C.Less'],
    ['How much quantity of can you consume?<br>A.Low<br>B.Medium<br>C.High variable'],
    ['What is your body temperature?<br>A.High compared to others<br>B.Low compared to others<br>C.Average'],
    ['How about your sleep?<br>A.Less sleep(<6 hrs)<br>B.Moderate sleep(6-8 hrs)<br>C.Heavy sleep(>8 hrs)'],
    ['Do you have a body odour?<br>A.Strong<br>B.Mild<br>C.Very mild'],
    ['How about changes in your body weight?<br>A.Gain weight easily and loose easily<br>B.Difficulty in gaining weight<br>C.Gain weight easily but loose with difficulty'],
    ['Do you like to..<br>A.Move around and interact with people and explore<br>B.Be seated and keep confined to own work<br>C.Move around moderately and not sit for very long hours']
    ]

answers=[]
def prakriti():
    vata=questions[0][1]
    pita=questions[0][2]
    kapha=questions[0][3]
    print(vata,pita,kapha)
    if vata>kapha and vata>pita:
        return "Vata<br>Diet: Eat warm, cooked, and nourishing foods. Include sweet, sour, and salty tastes. Avoid cold and dry foods. <br> Health Concerns: Watch out for anxiety, constipation, insomnia, and joint issues. Maintain balance to prevent these.<br>Lifestyle: Establish a regular routine, get enough rest, and practice relaxation techniques like meditation. Stay warm and hydrated.<br>Emotional Well-being: Nurture creativity, manage stress, and create a calm environment."
    elif pita>vata and pita>kapha:
        return "Pita<br>Diet: Opt for cooling and hydrating foods. Include bitter, sweet, and astringent tastes. Avoid spicy, oily, and hot foods.Diet: Opt for cooling and hydrating foods. Include bitter, sweet, and astringent tastes. Avoid spicy, oily, and hot foods.<rb>Health Concerns: Watch out for acidity, inflammation, skin irritations, and anger issues. Maintain balance to prevent these.<br>Lifestyle: Maintain a balanced routine, avoid excessive heat, and engage in calming activities like swimming or meditation.<br>Emotional Well-being: Manage stress and avoid situations that provoke anger or frustration."
    elif kapha>vata and kapha>pita:
        return "Kapha<br>Diet: Choose warm, light, and spicy foods. Emphasize pungent, bitter, and astringent tastes. Limit heavy, oily, and sweet foods.<br>Health Concerns: Watch out for weight gain, lethargy, congestion, and excessive mucus production. Maintain balance to prevent these.<br>Lifestyle: Stay active with regular exercise and avoid excessive sleep. Engage in activities that stimulate both the body and mind.<br>Emotional Well-being: Cultivate enthusiasm and motivation. Seek variety and avoid becoming too complacent or routine-oriented."
    elif vata==pita and pita==kapha:
        return "Tridosha<br>Vata Dosha: Vata is associated with the elements of air and space (ether). It governs functions related to movement, such as circulation, respiration, and nerve impulses. When Vata is in balance, individuals are creative, energetic, and adaptable. Imbalances can lead to anxiety, insomnia, and digestive issues.<br>Pitta Dosha: Pitta is associated with the elements of fire and water. It governs functions related to digestion, metabolism, and body temperature regulation. Balanced Pitta individuals are intelligent, focused, and have good digestion. Imbalances can lead to anger, inflammation, and skin problems.<br>Kapha Dosha: Kapha is associated with the elements of earth and water. It governs functions related to structure, stability, and lubrication in the body. Balanced Kapha individuals are calm, nurturing, and physically strong. Imbalances can lead to weight gain, congestion, and lethargy."
    elif vata==pita:
        return "Vata-Pita<br>Diet: Opt for warm, nourishing foods with a balance of cooling elements. Include sweet, bitter, and astringent tastes while avoiding overly spicy or excessively oily foods.<br>Health Concerns: Be mindful of imbalances related to both Vata and Pitta, such as digestive issues, anxiety, and skin problems. Focus on balancing both doshas.<br>Lifestyle: Establish a consistent routine that includes both relaxation and physical activity. Yoga and meditation can be beneficial.<br>Emotional Well-being: Manage stress and anxiety effectively. Strive for a balance between creativity and structure in daily life."
    elif vata==kapha:
        return "Vata-Kapha<br>Diet: Focus on a warm, light, and nourishing diet. Include foods with pungent, bitter, and astringent tastes while avoiding heavy, cold, and oily foods.<br>Health Concerns: Be mindful of potential imbalances related to both Kapha and Vata, such as weight gain, congestion, anxiety, and dryness. Strive for a balance between the two doshas.<br>Health Concerns: Be mindful of potential imbalances related to both Kapha and Vata, such as weight gain, congestion, anxiety, and dryness. Strive for a balance between the two doshas.<br>Lifestyle: Maintain a routine that incorporates both physical activity and relaxation. Engage in gentle exercises like yoga and prioritize regularity.<br>Emotional Well-being: Cultivate a sense of balance and adaptability. Manage stress effectively and seek activities that promote mental and emotional equilibrium."
    elif kapha==pita:
        return "Pita-Kapha<br>Diet: Focus on a diet that is cooling and moderately spiced. Include foods with sweet, bitter, and astringent tastes while avoiding overly spicy, oily, or heavy foods.<br>Health Concerns: Be aware of potential imbalances related to both Pitta and Kapha, such as digestive issues, weight gain, and skin problems. Aim for balance between the two doshas.<br>Lifestyle: Maintain a balanced routine that includes both physical activity and relaxation. Engage in activities that stimulate both the body and mind.<br>Emotional Well-being: Cultivate a sense of calm and emotional stability. Manage stress effectively, and strive for a harmonious balance between ambition and contentment."
   
@app.route('/get', methods=['POST'])
def get_response():
    user_message = request.form.get('msg')
    if not user_message:
        # Send a welcome message as the initial response
        welcome_message = "Welcome to prakriti assesment!<br> Your answer honestly for accurate result!!! <br> enter start to begin assesment"
        return jsonify({"bot_response" : welcome_message})
    elif user_message.lower()=='start':
        bot_response=questions[questions[0][0]]
        questions[0][0]+=1                           
        return jsonify({"bot_response" : bot_response})
    elif user_message.lower()=='a':
            questions[0][1]+=1
    elif user_message.lower()=='b':
            questions[0][2]+=1
    elif user_message.lower()=='c':
            questions[0][3]+=1
    else:
        qn=questions[questions[0][0]]
        return jsonify({"bot_response" : "Invalid Option"})
    bot_response=questions[questions[0][0]]
    if questions[0][0]==len(questions)-1:
        bot_response = prakriti()
    questions[0][0]+=1
    return jsonify({"bot_response" : bot_response})

if __name__ == '__main__':
    app.run(debug=True)    