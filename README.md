# 🌱 AI Crop Recommendation System

An AI-powered **Crop Recommendation System** that analyzes soil nutrients and environmental conditions to recommend the most suitable crops for cultivation.

The application uses a trained **Machine Learning Logistic Regression model** to predict suitable crops based on soil and climate parameters. It provides the **top 3 crop recommendations**, prediction confidence, scientific names, reasons for the recommendation, and useful growing tips.

---

## 🚀 Features

- 🌱 AI-powered crop recommendation
- 🧪 Soil nutrient analysis using **Nitrogen (N), Phosphorus (P), and Potassium (K)**
- 🌡️ Environmental analysis using temperature and humidity
- 🧬 Soil pH analysis
- 🌧️ Rainfall-based recommendations
- 🍂 Season-based crop prediction
- 🏆 Top 3 crop recommendations
- 📊 Prediction confidence scores
- 🔬 Scientific names of recommended crops
- 💡 Explanation for each recommendation
- 🌿 Crop-specific growing tips
- 🖥️ Interactive web interface
- 🔗 Flask API connecting the frontend with the Machine Learning model

---

## 🏗️ Project Structure

```text
AI-Crop-Recommendation/
│
├── app.py
├── crop_predict.py
├── crop_info.py
│
├── Rec_Models/
│   ├── crop_recommendation_model.pkl
│   ├── season_encoder.pkl
│   └── scaler.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

---

## 🤖 Machine Learning Model

The system uses a trained **Logistic Regression** model to predict suitable crops.

The prediction model analyzes the following features:

| Feature | Description |
|---|---|
| **N** | Nitrogen content in soil |
| **P** | Phosphorus content in soil |
| **K** | Potassium content in soil |
| **Temperature** | Environmental temperature in °C |
| **Humidity** | Relative humidity in % |
| **pH** | Soil pH value |
| **Rainfall** | Rainfall in mm |
| **Season** | Current agricultural season |

The model processes these features and calculates prediction probabilities for the available crop classes.

---

## 🌾 Supported Seasons

The application supports the following seasons:

- Autumn
- Rainy
- Spring
- Summer
- Winter
- Zaid

---

## 📊 Recommendation Output

The system provides:

### 🥇 Best Crop Recommendation

The highest-probability crop predicted by the Machine Learning model.

Example information displayed:

- Crop Name
- Scientific Name
- Prediction Confidence
- Reason for Recommendation
- Growing Tips

### 🥈🥉 Alternative Recommendations

The application also displays additional suitable crops ranked according to their prediction confidence.

---

## 💻 Technologies Used

### Backend

- Python
- Flask
- NumPy
- Scikit-learn

### Machine Learning

- Logistic Regression
- StandardScaler
- LabelEncoder

### Frontend

- HTML5
- CSS3
- JavaScript

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
```

### 2. Navigate to the Project Directory

```bash
cd YOUR-REPOSITORY-NAME
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install flask numpy scikit-learn
```

---

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

After starting the server, open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🖥️ How It Works

```text
User Input
    │
    ▼
Enter Soil & Environmental Data
    │
    ▼
Flask Backend
    │
    ▼
CropRecommender
    │
    ▼
Season Encoding
    │
    ▼
Feature Scaling
    │
    ▼
Machine Learning Model
    │
    ▼
Prediction Probabilities
    │
    ▼
Top 3 Crop Recommendations
    │
    ▼
Display Results on Frontend
```

---

## 🔄 Application Workflow

### Step 1 — Enter Agricultural Data

The user enters:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- Soil pH
- Rainfall
- Season

### Step 2 — Send Data to the Backend

The frontend sends the input data to the Flask `/predict` endpoint.

### Step 3 — Data Processing

The backend:

1. Validates the user input.
2. Encodes the selected season.
3. Arranges features in the required order.
4. Applies feature scaling.

### Step 4 — Model Prediction

The trained Logistic Regression model calculates probabilities for available crops.

### Step 5 — Recommendation

The application returns:

- 🥇 Best crop recommendation
- 🥈 Second-best recommendation
- 🥉 Third-best recommendation
- 📊 Confidence scores
- 🔬 Scientific names
- 💡 Recommendation reasons
- 🌿 Growing tips

---

## 📁 Important Files

### `app.py`

The main Flask application.

Responsible for:

- Serving the frontend
- Receiving user input
- Calling the crop recommendation model
- Returning prediction results as JSON

---

### `crop_predict.py`

Contains the core crop recommendation logic.

It:

- Loads the trained Machine Learning model
- Loads the season encoder
- Loads the feature scaler
- Processes input features
- Calculates prediction probabilities
- Returns the top crop recommendations

---

### `crop_info.py`

Contains additional information about supported crops.

The application uses it to provide:

- Scientific names
- Reasons for recommendations
- Growing tips

---

## 📦 Required Model Files

The following files must be available inside the `Rec_Models` directory:

```text
Rec_Models/
│
├── crop_recommendation_model.pkl
├── season_encoder.pkl
└── scaler.pkl
```

These files are required for the application to perform crop predictions.

---

## 📸 Screenshots

You can add screenshots of the application here.

Example:

```markdown
![Home Page](screenshots/home.png)

![Recommendation Result](screenshots/result.png)
```

---

## 🔮 Future Improvements

Possible improvements for the project include:

- 🌦️ Real-time weather API integration
- 📍 Location-based recommendations
- 🧪 Soil sensor integration using IoT
- 🌱 Fertilizer recommendation system
- 📊 Soil health dashboard
- 🦠 Plant disease detection
- 📱 Mobile-responsive application improvements
- 🌾 Region-specific crop recommendations
- 🗺️ Interactive farm location support
- ☁️ Cloud deployment
- 🤖 Integration into the larger **AgriSense Smart Agriculture Platform**

---

## ⚠️ Disclaimer

The recommendations generated by this application are based on the trained Machine Learning model and the provided input data.

Actual agricultural decisions should also consider factors such as:

- Local soil conditions
- Geographic location
- Crop variety
- Pest and disease conditions
- Water availability
- Local agricultural guidelines

For real-world farming decisions, consultation with agricultural experts or local agricultural extension services is recommended.

---

## 👨‍💻 Author

**Adithya Krishna T K**

AI & Machine Learning Enthusiast | Data Science | Computer Vision

🔗 LinkedIn: https://www.linkedin.com/in/adithya-krishna-t-k-ak0604

---

## ⭐ Contributing

Contributions, suggestions, and improvements are welcome!

If you find this project useful, consider giving the repository a **⭐ star**.

---

### 🌱 Built with Machine Learning for Smarter Agriculture
