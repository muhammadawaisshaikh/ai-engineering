from sklearn.preprocessing import LabelEncoder

class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        """Handle missing values and duplicates"""
        self.data.drop_duplicates(inplace=True)
        self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
        return self.data

    def encode_data(self):
        """Convert categorical columns into numeric using Label Encoding"""
        label_enc = LabelEncoder()
        for col in self.data.select_dtypes(include="object").columns:
            self.data[col] = label_enc.fit_transform(self.data[col])
        return self.data