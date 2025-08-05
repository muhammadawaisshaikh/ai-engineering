import pandas as pd

def generate_sample_emails():
    data = [
        {"email": "Congratulations! You win a free ticket", "label": 1},
        {"email": "Meeting rescheduled to 3 PM", "label": 0},
        {"email": "Get free access to our exclusive offer", "label": 1},
        {"email": "Lunch tomorrow?", "label": 0},
        {"email": "You have won a prize, claim now", "label": 1},
        {"email": "Monthly report is attached", "label": 0}
    ]
    return pd.DataFrame(data)