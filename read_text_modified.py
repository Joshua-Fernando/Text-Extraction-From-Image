from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import uuid

def recognize_text_in_image(image_file, annotated_folder):
    """
    Recognizes text in an image and returns the results in a dictionary.
    """
    try:
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        cv_client = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )

        with open(image_file, "rb") as f:
            image_data = f.read()

        result = cv_client.analyze(
            image_data=image_data,
            visual_features=[VisualFeatures.READ]
        )

        analysis_results = {
            'text_lines': [],
            'lines_image': None,
            'words_image': None
        }

        if result.read:
            # Extract text lines
            for line in result.read.blocks[0].lines:
                analysis_results['text_lines'].append(line.text)
            
            # Create and save annotated images
            analysis_results['lines_image'] = annotate_lines(image_file, result.read, annotated_folder)
            analysis_results['words_image'] = annotate_words(image_file, result.read, annotated_folder)
            
        return analysis_results

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}


def annotate_lines(image_file, detected_text, annotated_folder):
    image = Image.open(image_file)
    fig = plt.figure(figsize=(image.width/100, image.height/100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'cyan'

    for line in detected_text.blocks[0].lines:
        r = line.bounding_polygon
        rectangle = ((r[0].x, r[0].y), (r[1].x, r[1].y), (r[2].x, r[2].y), (r[3].x, r[3].y))
        draw.polygon(rectangle, outline=color, width=3)

    plt.imshow(image)
    plt.tight_layout(pad=0)
    
    # Generate a unique filename
    textfile = f"lines_{uuid.uuid4()}.jpg"
    filepath = os.path.join(annotated_folder, textfile)
    fig.savefig(filepath)
    plt.close(fig)
    return textfile
    

def annotate_words(image_file, detected_text, annotated_folder):
    image = Image.open(image_file)
    fig = plt.figure(figsize=(image.width/100, image.height/100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'cyan'

    for line in detected_text.blocks[0].lines:
        for word in line.words:
            r = word.bounding_polygon
            rectangle = ((r[0].x, r[0].y), (r[1].x, r[1].y), (r[2].x, r[2].y), (r[3].x, r[3].y))
            draw.polygon(rectangle, outline=color, width=3)

    plt.imshow(image)
    plt.tight_layout(pad=0)
    
    # Generate a unique filename
    textfile = f"words_{uuid.uuid4()}.jpg"
    filepath = os.path.join(annotated_folder, textfile)
    fig.savefig(filepath)
    plt.close(fig)
    return textfile