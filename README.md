# Estonian Text to Estonian Sign Language Prototype

This project provides a tool to translate Estonian text into Estonian Sign Language (ESL) using a virtual avatar. The avatar demonstrates sign language by analyzing and visualizing landmarks of the human body, face, and hands. The virtual avatar provides a visual and intuitive way to understand and learn Estonian Sign Language. By translating text into a series of animated gestures, this tool can be used for educational purposes, communication aids, and enhancing accessibility for the deaf and hard-of-hearing community.

Due to the limited availability of Estonian Sign Language videos, this project also focuses on utilizing existing videos to extract and calculate landmarks using MediaPipe. We can only make avatars for a limited number of sentences and words. This approach helps in generating accurate sign language animations based on the input text.

Original dataset utilized in this application is available at : https://arhiiv.eki.ee/dict/viibex/

## Features

- **Text Preprocessing**: Tokenization and spell-checking of input Estonian text.
- **Landmark Detection**: Using MediaPipe to detect and draw pose, face, and hand landmarks.
- **Avatar Animation**: Visual representation of sign language through a virtual avatar.


### Functionality

1. **Preprocessing Phase**:
   - Converts the input text to lowercase.
   - Removes punctuation.
   - Performs tokenization and spell-checking using `estnltk`.

2. **Creating Avatar**:
   - Processes the phrase into words.
   - For each normalized word, the corresponding sign language video is identified
   - Uses MediaPipe Holistic model to detect landmarks.
   - Draws pose, face, and hand landmarks on a virtual avatar.
   - Creates a video output showing the avatar performing sign language.

### Detailed Functionality

#### Preprocessing Phrase

The function preprocess phase is responsible for preparing the Estonian text for translation into sign language. It performs several key tasks:
1. **Lowercase Conversion**: Converts all characters in the input text to lowercase to ensure uniformity.
2. **Punctuation Removal**: Strips out punctuation marks to avoid processing errors.
3. **Whitespace Trimming**: Removes leading and trailing whitespace.
4. **Tokenization**: Breaks down the text into individual tokens (words) using `estnltk`.
5. **Spell Correction**: Corrects spelling errors in the tokens using `SpellCheckRetagger` from `estnltk`.
6. **Lemmatization**: Extracts the root form of each corrected word.

This preprocessing ensures that the input text is clean and correctly formatted, which is crucial for accurate sign language translation.

#### Creating Avatar

The function generate avatar phase handles the core functionality of translating text to sign language and animating the virtual avatar. It includes the following steps:

1. **Phrase Processing**: Calls `preprocess_phrase(phrase)` to clean and tokenize the input text.
2. **MediaPipe Initialization**: Sets up the MediaPipe Holistic model, which combines pose, face, and hand landmark detection.
3. **Landmark Detection**: For each word in the processed phrase, it retrieves the corresponding landmark data (pose, face, and hand landmarks).
4. **Drawing Landmarks**: Uses `MediaPipe` drawing utilities to visualize the detected landmarks on an avatar. This involves:
   - Drawing pose landmarks (e.g., body joints).
   - Drawing face landmarks (e.g., facial features).
   - Drawing hand landmarks (e.g., finger joints).
5. **Video Creation**: Creates a video output where the avatar demonstrates the sign language translation of the input text.



## Running the Application

### Prerequisites

Before you begin, ensure you have the following installed on your system:
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) or [Miniconda](https://docs.anaconda.com/miniconda/miniconda-install/)
- [Node.js](https://nodejs.org/en/download/)

### Getting Started

#### 1. Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/BamunugeDR99/Estonian-Sign-Language-Prototype.git
```
```sh
cd esl-prototype
```
#### 2. Set up the Backend
Navigate to the Backend Directory

```sh
cd backend
```
Create and Activate a Virtual Environment
```sh
conda create --name esl-prototype python=3.10
```
```sh
conda activate esl-prototype
```
Install Backend Dependencies
```sh
pip install -r requirements.txt
```
Run the Backend Server
```sh
uvicorn main:app --reload
```
The backend server should now be running on **http://localhost:8000**.

#### 3. Set up the Frontend
Open a new terminal window and navigate to the frontend directory
```sh
cd frontend
```

Install Frontend Dependencies
```sh
npm install
```
Start the Frontend
```sh
npm start
```
The frontend should now be running on **http://localhost:3000**.

### 4. Accessing the Application
Open your web browser and navigate to **http://localhost:3000** to view and interact with the ESL Prototype application



## Example Output

### Input Text

"Ma armastan sind"

### Output

Below is the video representation of the input text in Estonian Sign Language:

Please [Click Here](https://drive.google.com/file/d/1-kYinMYfFcin_L9UraoWI140Wx1ogOfQ/view?usp=sharing) to view the input text in Estonian Sign Language.

### Full flow demonstration


https://github.com/BamunugeDR99/Estonian-Sign-Language-Prototype/assets/88665574/b1359b2d-32d8-468e-911a-5e45a930720e


