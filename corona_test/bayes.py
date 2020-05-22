### Dictionary for all nodes
# Level 1
met_diagnosed_person = {"T" : 0.00045, "F" : 0.99955, "X" : 1}
visited = {"T" : 0.845, "F" : 0.155, "X" : 1}
fever = {"T" : 0.3, "F" : 0.7, "X" : 1}

# Level 2
fatigue = {"TT": 0.6, "TF": 0.4,        # Fever - Cold
           "FT": 0.5, "FF": 0.3,
           "X": 1}

cold = {"T": 0.5, "F": 0.2, "X": 1}     # Fever               

# Level 3
short_breath = {"T": 0.5, "F": 0.5, "X": 1}    # Fatigue

# Level 4
cough = {"T": 0.75, "F": 0.375, "X": 1}   # Short breath

# # Level 5
# corona = {"TTT": 0.95, "TTF": 0.85,       #  Cough - Met - Visit
#           "TFT": 0.75, "TFF": 0.4,
#           "FTT": 0.9, "FTF": 0.8,
#           "FFT": 0.7, "FFF": 0.05,
#           "X": 1}

nodes = [fever, cold, fatigue, short_breath, cough, met_diagnosed_perso,  visited corona]
    
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

    ## FEVER
    result *= fever.get(symptoms[0].upper())

    ## COLD
    if(symptoms[1].upper() == "X"):                    
        result *= 1
    else:
        if((symptoms[0].upper() == "T") & (symptoms[1].upper() == "T")):
            result *= cold.get("T")
        elif((symptoms[0].upper() == "F") & (symptoms[1].upper() == "T")):
            result *= cold.get("F")
        elif((symptoms[0].upper() == "T") & (symptoms[1].upper() == "F")):
            temp = 1 - cold.get("T")
            result *= temp
        elif((symptoms[0].upper() == "F") & (symptoms[1].upper() == "F")):
            temp = 1 - cold.get("F")
            result *= temp
    
    ## FATIGUE
    if(symptoms[2].upper() == "X"):                    
        result *=  1
    else:
        if((symptoms[0].upper() == "T") & (symptoms[1].upper() == "T") & (symptoms[2].upper() == "T")):
            result *= fatigue.get("TT")
        elif((symptoms[0].upper() == "F") & (symptoms[1].upper() == "T") & (symptoms[2].upper() == "T")):
            result *= fatigue.get("FT")
        elif((symptoms[0].upper() == "T") & (symptoms[1].upper() == "F") & (symptoms[2].upper() == "T")):
            result *= fatigue.get("TF")
        elif((symptoms[0].upper() == "F") & (symptoms[1].upper() == "F") & (symptoms[2].upper() == "T")):
            result *= fatigue.get("FF")
        elif((symptoms[0].upper() == "T") & (symptoms[1].upper() == "T") & (symptoms[2].upper() == "F")):
            temp = 1 - fatigue.get("TT")
            result *= temp
        elif((symptoms[0].upper() == "F") & (symptoms[1].upper() == "T") & (symptoms[2].upper() == "F")):
            temp = 1 - fatigue.get("FT")
            result *= temp
        elif((symptoms[0].upper() == "T") & (symptoms[1].upper() == "F") & (symptoms[2].upper() == "F")):
            temp = 1 - fatigue.get("TF")
            result *= temp
        elif((symptoms[0].upper() == "F") & (symptoms[1].upper() == "F") & (symptoms[2].upper() == "F")):
            temp = 1 - fatigue.get("FF")
            result *= temp
            
    ## SHORT BREATH
    if(symptoms[3].upper() == "X"):                    
        result *= 1
    else:
        if((symptoms[2].upper() == "T" & (symptoms[3].upper() == "T")):
            result *= short_breath.get("T")
        elif((symptomm[2].upper() == "F" & (symptoms[3].upper() == "T")):
            result *= short_breath.get("F")
        elif((symptomm[2].upper() == "T" & (symptoms[3].upper() == "F")):
            temp = 1 - short_breath.get("T")
            result *= temp
        elif((symptoms[2].upper() == "F") & (symptoms[3].upper() == "F")):
            temp = 1 - short_breath.get("F")
            result *= temp
    
    ## COUGH
    if(symptoms[4].upper() == "X"):                    
        result *= 1
    else:
        if((symptoms[3].upper()) == "T") & (symptoms[4].upper()) == "T")):
            result *= cough.get("T")
        elif((symptoms[3].upper() == "F") & (symptoms[4].upper() == "T")):
            result *= cough.get("F")
        elif((symptoms[3].upper() == "T") & (symptoms[4].upper() == "F")):
            temp = 1 - cough.get("T")
            result *= temp
        elif((symptoms[3].upper() == "F") & (symptoms[4].upper() == "F")):
            temp = 1 - cough.get("F")
            result *= temp
    
    ## MET
    result *= met_diagnosed_person.get(symptoms[5].upper())                

    ## VISIT
    result *= visited.get(symptoms[6].upper())                             
    
    return result