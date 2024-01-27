import json

def insuranceCover(
    age = 27,
    tier = "tier_1",
    pre_existing_diease='',
    genetic_history='',
    smoking_and_drinking ='',
): 
    

    INFLATION_RATE = 7
    base_amount = 0

    # Add more critical illnesses as desired
    CRITICAL_ILLNESS = [
        "Sarcoidosis",
        "Malignant Neoplasms",
        "Epilepsy",
        "Heart Ailments",
        "Cerebrovascular DiseaseS",
        "Inflammatory Bowel Diseases",
        "Chronic Liver Diseases",
        "Pancreatic Diseases",
        "Chronic Kidney Diseases",
        "Hepatitis B",
        "Alzheimer's Disease",
        "Parkinson's Disease",
        "Demyelinating Disease",
        "HIV/AIDS",
        "Loss of Hearing",
        "Papulosquamous Skin Disease",
        "Avascular Necrosis",
    ]


    with open('incidence_rate.json', 'r') as f:
        incidence_rate_data = json.load(f)
    with open('disease_cost.json', 'r') as f:
        disease_cost_data = json.load(f)
    with open('treatment_cost.json', 'r') as f:
        treatment_cost_data = json.load(f)
    

    # Code to calculate base amunt

    incidence = ''
    for key in incidence_rate_data.keys():
        age_range = key.split('-')
        if int(age_range[0]) <= age and age <= int(age_range[1]):
            incidence = incidence_rate_data[key]
            # AGE_CAP = int(age_range[1])
            break
    

    for key in incidence.keys():
        base_amount +=  disease_cost_data[key][tier] * incidence[key]/100
    
    inflation_time = 0
    if age <= 40:
        inflation_time = 10 - age % 5
    elif age > 40:
        inflation_time = 60 - age

    base_amount = base_amount * pow(1+INFLATION_RATE/100, inflation_time)




    # print(inflation_time)
    # print(base_amount)
    
    
    # code to calcualte amount for PED

    if pre_existing_diease in CRITICAL_ILLNESS:
        message = "Since you already have a prexisting disease, we recommend you to buy insurance with cover " + str(int(base_amount)) + ". This will be coving you for long duration. Plus we would also recommend you to add some additional amount in your cover."
        print(message)
        return message

    
    if pre_existing_diease in treatment_cost_data.keys():
        base_amount_ped = treatment_cost_data[pre_existing_diease][tier] * pow(1+INFLATION_RATE/100, 60 - age)
        message = "Since you already have a prexisting disease, we recommend you to buy insurance with cover " + str(int(base_amount_ped)) + ". This will be coving you for long duration."
        if base_amount_ped > 2000000:
            message  = "Since you already have a prexisting disease, we recommend you to buy insurance with cover 2000000. This will be coving you for long duration. We also recommend you to buy supertop in existing insurance."
        print(message)
        return message

    if pre_existing_diease == "Others":
        base_amount += 500000 
        message = "Since you already have a prexisting disease, we recommend you to buy insurance with cover " + str(int(base_amount)) + ". This will be coving you for long duration."
        print(message)
        return(message)

    message = "We recommend you to buy insurance with cover " + str(int(base_amount)) +"."

    if age < 40:
        message += " We also recommed you to re-evaluate you cover amount in next 10 years."
    print(message)
    return message
    
    
insuranceCover()