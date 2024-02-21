questions=[['What is your body frame?<br>A. Thin and lean body frame<br>B. Medium build<br>C. Large and sturdy build'],
    ['What is your skin type?<br>A. Dry skin<br>B. Oily skin<br>C. Oily and thick skin'],
    ['What is your hair type?<br>A. Dry hair<br>B. Oily hair<br>C. Oily and thick hair'],
    ['What is your complexion?<br>A. Fair complexion<br>B. Medium complexion<br>C. Dark complexion'],
    ['What is your body weight?<br>A.UnderWeight<br>B.Normal Weight<br>C.Overweight'],
    ['What is your energy level?<br>A. Low energy level<br>B. High energy level<br>C. Medium energy level'],
    ['What is your digestion like?<br>A. Weak digestion<br>B. Strong digestion<br>C. Strong digestion'],
    ['What is your appetite like?<br>A. Irregular appetite<br>B. Strong appetite<br>C. Regular appetite'],
    ['What is your sleep pattern like?<br>A. Light and disturbed sleep<br>B. Deep and restful sleep',	'C. Deep and restful sleep'],
    ['What is your tolerance to heat and cold?<br>A. Sensitive to cold<br>B. Sensitive to heat<br>C. Tolerant of both heat and cold'],
    ['What is your temperament?<br>A. Calm and gentle temperament<br>B. Active and competitive temperament<br>C. Calm and easygoing temperament'],
    ['What is your learning style?<br>A. Fast learner, but may forget quickly<br>B. Good learner and memory<br>C. Slow learner, but retains information well'],
    ['What is your memory like?<br>A. Moderately<br>B. Quickely<br>C. Slowly'],
    ['What is your concentration like?<br>A. Good concentration<br>B. Good concentration<br>C.Poor concentration'],
    ['What is your stress level like?<br>A.Low stress level<br>B. Medium stress level<br>C. High stress level'],
    ['What are your emotional tendencies?<br>A. Happy and cheerful disposition<br>B. Intelligent and ambitious disposition<br>C. Gentle and compassionate disposition'],
    ['what is your diet like?<br>A.Light diet<br>B.Heavy diet<br>C.Irregular diet'],
    ['what is your exercise routine like?<br>A.Irregular exercise routine<br>B.Regular exercise routine<br>C.None'],
    ['what is your sleep schedule like?<br>A.Irregular sleep schedule<br>B.Regular sleep schedule<br>C.None'],
    ['Do you have any specific cravings or aversions?<br>A.Cravings for sweet ans salty foods<br>B.Cravings for bitter and sour foods<br>C.Cravings for sweet and fatty foods'],
    ['Are you sensitive to certain foods,weather conditions,or other environmental factors?<br>A.Aversion to cold and windy weather<br>B.Aversion to hot and windy weather<br>C.Aversion to cold and windy weather'],
    ['How frequently do you fall ill?<br>A.Frequently<br>B.Rarely<br>C.Moderately'],
    ['Do you tend to have<br>A.Constipation<br>B.Loose motions<br>C.None'],
    ['Amount of speaking<br>A.Excessive<br>B.Less<br>C,Moderately'],
    ['How frequently do you feel tired?<br>A.On doing routine work<br>B.After doing routine work/heavy work<br>C.Not even after heavy work'],
    ['How about your perspiration?<br>A.Profuse<br>B.Moderate<br>C.Less'],
    ['How much quantity of can you consume?<br>A.Low<br>B.Medium<br>C.High variable'],
    ['What is your body temperature?<br>A.High compared to others<br>B.Low compared to others<br>C.Average'],
    ['How about your sleep?<br>A.Less sleep(<6 hrs)<br>B.Moderate sleep(6-8 hrs)<br>C.Heavy sleep(>8 hrs)'],
    ['Do you have a body odour?<br>A.Strong<br>B.Mild<br>C.Very mild']]
vata=0
pita=0
kapha=0
x=0
answers=[]
while(True):
    print(x)
    for i in questions[x]:
        print(i)
    ans=input().strip()
    ans.lower()
    if ans=='a':
        vata+=1
        answers.append(questions[x][1])
    elif ans=='b':
        pita+=1
        answers.append(questions[x][2])
    elif ans=='c':
        kapha+=1
        answers.append(questions[x][3])
    else:
        print("INVALID OPTION")
        continue
    if x==len(questions)-1:
        break
    x+=1
    
if vata>kapha and vata>pita:
    print("VATA")
elif pita>vata and pita>kapha:
    print("PITA")
elif kapha>vata and kapha>pita:
    print("KHAPA")
elif vata==pita and pita==kapha:
    print("Tridosha")
elif vata==pita:
    print("vata pita")
elif vata==kapha:
    print("vata kapha")
elif kapha==pita:
    print("kapha pita")
