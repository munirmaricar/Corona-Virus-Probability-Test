### Dictionary for all nodes
# Level 1
met_diagnosed_person = {"T" : 0.99955, "F" : 0.00045}
visited = {"T" : 0.845, "F" : 0.155}
fever = {"T" : 0.3, "F" : 0.7}

# Level 2
fatigue = {"TT": 0.6, "TF": 0.4,        # Fever - Cold
           "FT": 0.5, "FF": 0.3}

cold = {"T": 0.5, "F": 0.2}     # Fever               

# Level 3
short_breath = {"T": 0.5, "F": 0.5}    # Fatigue

# Level 4
cough = {"T": 0.75, "F": 0.375}   # Short breath

# # Level 5
corona = {"TTT": 0.95, "TTF": 0.85,       #  Cough - Met - Visit
          "TFT": 0.75, "TFF": 0.4,
          "FTT": 0.9, "FTF": 0.8,
          "FFT": 0.7, "FFF": 0.05,
          "X": 1}

nodes = [fever, cold, fatigue, short_breath, cough, met_diagnosed_person,  visited]

def get_parent(child):
    if(child == "FATIGUE"):
        return {nodes[0], nodes[3]}
    elif(child == "COLD"):
        return {nodes[0]}
    elif(child == "SHORT_BREATH"):
        return {nodes[4]}
    elif(child == "DRY_COUGH"):
        return {nodes[5]}
    elif(child == "CORONA"):
        return {nodes[6], nodes[1], nodes[2]}
        
def inference(symptoms):
    result = 0

    all_known = True

    for i in symptoms:
        if(all_known and i == "X"):
            all_known = False
            break
    
    if(all_known):
        corona_string = symptoms[4] + symptoms[5] + symptoms[6]
        result = corona[corona_string]
        return result
    else:
        symptoms_dict = {"fever":symptoms[0], "cold":symptoms[1], "fatigue":symptoms[2], "short_breath":symptoms[3],
                         "cough":symptoms[4], "met_diagnosed_person":symptoms[5], "visited":symptoms[6]}
        value = ["T", "F"]
        array_result = []
        array_length = 0

        for i in symptoms_dict:
            if symptoms_dict[i] == "X":
                array_result.append(value)
            else:
                array_result.append([symptoms_dict[i]])

        # print(array_result)
        for i in range(len(array_result[0])):                                   # fever T, F
            for j in range(len(array_result[1])):                               # cold  T, F
                for k in range(len(array_result[2])):                           # fatigue   TT, TF, FT, FF
                    for l in range(len(array_result[3])):                       # short breath  T, F
                        for m in range(len(array_result[4])):                   # cough T, F
                            for n in range(len(array_result[5])):               # met   T, F
                                for o in range(len(array_result[6])):           # visit T, F
                                    # print(array_result[0][i] + array_result[1][j] + array_result[2][k] + array_result[3][l] + array_result[4][m] + array_result[5][n] + array_result[6][o])
                                    # P(fever)
                                    fever_value = fever[array_result[0][i]]         

                                    # P(cold|fever)
                                    if(array_result[1][j] == "T"):
                                        cold_value = cold[array_result[0][i]]           
                                    else:
                                        cold_value = 1 - cold[array_result[0][i]]
                                    
                                    # P(fatigue|fever, cold)
                                    if(array_result[2][k] == "T"):
                                        fatigue_value = fatigue[array_result[0][i] + array_result[1][j]]
                                    else:
                                        fatigue_value = 1 - fatigue[array_result[0][i] + array_result[1][j]]

                                    # P(short_breath|fatigue)
                                    if(array_result[3][l] == "T"):
                                        short_breath_value = short_breath[array_result[2][k]]
                                    else:
                                        short_breath_value = 1 - short_breath[array_result[2][k]]
                                    
                                    # P(cough|short_breath)
                                    if(array_result[4][m] == "T"):
                                        cough_value = cough[array_result[3][l]]
                                    else:
                                        cough_value = 1 - cough[array_result[3][l]]
                                    
                                    # P(met)
                                    met_value = met_diagnosed_person[array_result[5][n]]
                                    
                                    # P(visit)
                                    visit_value = visited[array_result[6][o]]
                                    
                                    # P(corona|cough, met, visit)
                                    result += fever_value * cold_value * fatigue_value * short_breath_value * cough_value * met_value * visit_value                       
    return result