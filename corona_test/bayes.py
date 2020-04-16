### Dictionary for all nodes
short_breath = {"T": 0.16, "F": 0.17, "X":1}
dry_cough = {"T": 0.39, "F": 0.08, "X":1}
met_diagnosed_person = {"T": 0, "F": 0, "X":1}
visited_country = {"T": 0, "F": 0, "X":1}
fatigue = {"T": 0.22, "F": 0.15, "X":1}
cold = {"T": 0.28, "F": 0.09, "X":1}
fever = {"TTT": 0, "TTF": 0, "TFT": 0,
        "TFF": 0, "FTT": 0, "FTF": 0,
        "FFT": 0, "FFF": 0, "X":1}

P(C) =  0.171875 (55k/320k)
P(F) = 0.3
P(~F) = 0.7
P(CF) = P(FC) = 0.065484375
P(C|F) = 0.065*0.3 = 0.0195
P(C|F) = P(F|C) P(C) / P(F) = 0.381 * 0.171875 / 0.3 = 0.22
P(C|~F) = P(~F|C) P(C) / P(~F) = 0.619 * 0.171875 / 0.7 = 0.15

P(Dry Cough) = 0.3
P(~D) = 0.7
P(C|D) = P(D|C) P(C) / P(D) = 0.677 * 0.171875 / 0.3 = 0.39
P(C|~D) = P(~D|C) P(C) / P(~D) = 0.323 * 0.171875 / 0.7 = 0.08

P(Short Breath) = 0.2
P(~S) = 0.8
P(C|S) = P(S|C) P(C) / P(S) = 0.186 * 0.171875 / 0.2 = 0.16
P(C|~S) = P(~S|C) P(C) / P(~S) = 0.814 * 0.171875 / 0.8 = 0.17

P(Met Diagnosed) = 0.4
P(~M) = 0.6
P(C|M) = P(M|C) P(C) / P(M) = 
P(C|~M) = P(~M|C) P(C) / P(~M) = 

P(cold) = 0.4
P(~cl) = 0.6
P(C|cl) = P(cl|C) P(C) / P(cl) = 0.657 * 0.171875 / 0.4 = 0.28
P(C|~cl) = P(~cl|C) P(C) / P(~cl) = 0.343 * 0.171875 / 0.6 = 0.09

P(Fever) = 0.5
P(~Fv) = 0.5
P(C|Fv) = P(fv|C) P(C) / P(fv) = 0.879 * 0.171875 / 0.5 = 0.30
P(C|~fv) = P(~fv|C) P(C) / P(~fv) = 0.121 * 0.171875 / 0.5 = 0.04

P(Visit country)
P(C|V) = P(V|C) P(C) / P(V) = 
P(C|~V) = P(~V|C) P(C) / P(~V) = 