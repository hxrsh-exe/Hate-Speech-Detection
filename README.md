
# Hate Speech Detection Software

## Project Description
This project aims to detect hate speech and offensive language in text data using machine learning techniques. The software provides a graphical user interface for users to input text or upload a text file to be scanned for hate speech. The application includes exception handling to manage errors related to file operations, text processing, and model predictions, ensuring that the software can handle unexpected situations gracefully and provide informative error messages.

## Files in the Project
1. **bg.jpg**: Background image used in the user interface.
2. **icon.ico**: Icon image for the user interface window.
3. **main.py**: Contains the main logic for data preprocessing, model training, and prediction.
4. **text_file.txt**: Example text file used for testing the file input functionality.
5. **twitterdata.csv**: Dataset containing tweets labeled for hate speech detection.
6. **UserInterface.py**: Contains the code for the graphical user interface built using Tkinter.

## Installation Instructions
1. Clone the repository to your local machine.
2. Install the necessary dependencies using the command: 
   ```sh
   pip install -r requirements.txt
3. Ensure you have the necessary NLTK data files by running the following Python code: 
`import nltk`  
`nltk.download('stopwords')`

## Usage Instructions

1.  Run the user interface by executing :
    `python UserInterface.py` 
    
2.  Input text directly into the provided text box or use the "Open File" button to scan a text file for hate speech.
3.  The results will be displayed in a message box.

## Contributing

If you wish to contribute to this project, please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.