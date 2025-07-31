# Text-Extraction-From-Image

## Description

The Image Text Recognition Web App is a powerful application designed to extract and visualize text from images using Azure AI Vision services. Users can upload any image file, and the application will return the recognized text along with annotated images showing the exact location of the detected text lines and words.
Built with a Flask backend, this app provides a clear example of how to integrate Azure's cloud-based AI to perform Optical Character Recognition (OCR). It serves as a practical guide for developers looking to build applications for digitizing documents, extracting information from images, or making image content accessible.


---

## Features
- Image Upload: Simple interface to upload an image for text analysis.
- Text Recognition: Extracts all text found within the uploaded image.
- Line Annotation: Generates and displays an image with bounding boxes drawn around each detected line of text.
- Word Annotation: Generates and displays an image with bounding boxes drawn around each individual detected word.

---

##  Tech Stack
- **Python 3.X**
- **Flask** (for the web interface)
- **Azure AI Vision Service API**
- Pillow


--- 

##  Project Structure
```
├── app.py                     # Flask web application
├── read_text_modified.py      # CLI script to test Azure Custom Vision predictions
├── templates/
│   └── index.html             # Web interface for image upload
│   └── results.html           # Web page to display results
├── static/
│   ├── style.css              # Web style template
│   ├── uploads/               # Directory for user-uploaded images
│   └── annotated/             # Directory for annotated result images
├── requirements.txt 
├── README.md                    
└── LICENSE                    


```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Joshua-Fernando/Text-Extraction-From-Image
cd Text-Extraction-From-Image
```

### 2. Install Dependencies
Using **pip**:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Azure AI Vision Setup
1. Create a Computer Vision resource in the Azure portal.
2. Once created, navigate to the Keys and Endpoint section of your resource.
3. Get the following credentials:
   - **Service Endpoint**
   - **API Key**
 
4. Add these to your environment variables:
   ```bash
   
    AI_SERVICE_ENDPOINT="YOUR_AZURE_ENDPOINT"
    AI_SERVICE_KEY="YOUR_AZURE_API_KEY"

   ```

---

## Running the Web App
```bash
python app.py
```
Then open your browser and navigate to:
```
http://localhost:5000
```

---

## Deployment
You can deploy this project to:
- **Azure App Service**
- **Replit**
- **Heroku**
- **Any cloud hosting that supports Flask**

---

## License
This project is licensed under the **Apache-2.0 license**.

---

### 👨‍💻 Author
Developed by **Joshua Fernando**  
Feel free to contribute or open issues!

