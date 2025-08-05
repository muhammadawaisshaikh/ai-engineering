# Expert System (Simulated Logic) - diagnose fever and heache symptoms 
def diagnose(symptoms):
    if "fever" in symptoms and "cough" in symptoms:
        return "You may have the flu."
    elif "headache" in symptoms and "sensitivity to light" in symptoms:
        return "You may have a migraine."
    else:
        return "Further evaluation needed."

print(diagnose(["fever", "cough"]))
