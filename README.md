
# Automated Storyboard Generator for Advertisement Campaigns

This project aims to automate the creation of visually compelling storyboards for advertisement campaigns by leveraging natural language processing (NLP) and computer vision. It uses TensorFlow, PyTorch, and Keras for machine learning, OpenCV and Yolo for computer vision, and Tesseract, OpenCV, and TensorFlow for NLP. The generated storyboards are saved in the `output` directory.

## Introduction

In the realm of digital advertising, advancements in machine learning, natural language processing (NLP), and computer vision have revolutionized the creation of captivating and impactful campaigns. These technologies enable the interpretation of complex data, allowing for the seamless integration of textual concepts and visual storytelling in advertisements.

This transformative era of advertising recognizes the power of technology to streamline and enhance the ad creation process. As part of this initiative, the goal is to develop a machine learning solution that automates the conversion of textual advertisement concepts and asset descriptions into visually compelling storyboards. This solution will interpret provided concepts and assets, generate relevant visual and textual assets, and compose these assets into individual ad frames. Ultimately, it will synthesize a cohesive storyboard that encapsulates the essence of the proposed ad campaign.

## Technology Overview

### Data Preparation and Evaluation

#### Data Processing Libraries

-   **Pandas**, **NumPy**, and **Scikit-learn**: These libraries equip us with efficient data structures and algorithms to handle large datasets, performing essential preprocessing and feature engineering for optimal model performance.

#### Model Evaluation Libraries

-   **TensorFlow Model Analysis (TFMA)** and **Scikit-learn**: These libraries provide critical metrics and visualization tools to assess the accuracy and generalizability of our models, ensuring they deliver on their potential.

#### Visualization Libraries

-   **Matplotlib** and **Seaborn**: These libraries bring your generated images and storyboards to life, offering a wide range of customization options for creating clear and impactful visualizations that effectively communicate your creative ideas.

### Image and Text Processing and Understanding

#### Natural Language Processing (NLP) Libraries

-   **Tesseract**, **OpenCV**, and **TensorFlow**: These workhorses analyze textual descriptions, enabling tasks like named entity recognition, extraction and storing. These insights fuel effective visual and textual ad components.

#### Computer Vision Libraries

-   **OpenCV** and **Yolo**: These libraries empower image processing and analysis of ad visuals. Tasks like image segmentation, object detection, and classification pave the way for generating tailored visual assets.

### Image and Text Generation Models

These models have been developed to generate realistic and contextually relevant content, aligning with the objectives of creating engaging ad campaigns.
-   **Fooocus**: An open-source image generation tool that uses a combination of deep learning models, including GANs and VAEs, to generate images from textual prompts.

### Machine Learning Frameworks and Deployment

#### Frameworks

-   **TensorFlow**, **PyTorch**, and **Keras**: These industry-standard frameworks simplify development and training of machine learning models for image generation and text-to-image synthesis.

## Getting Started

1.  Clone the repository:
    
    `git clone https://github.com/week-10-g5/Automated-Storyboard-Synthesis-for-Digital-Advertising` 
    
2.  Navigate to the project directory:
     
    `cd Automated-Storyboard-Synthesis-for-Digital-Advertising` 
    
3.  Install the required Python packages:
    
    `pip install -r requirements.txt`
    
4. Run the `main.py` script:
 
	`python main.py`

## Contributing

Pull requests are welcome. Please update as appropriate.

## License

MIT