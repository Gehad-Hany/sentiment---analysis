# Sentiment Analysis using BERT

This project is a web application that performs sentiment analysis on user-provided text using a BERT model. The application is built using Streamlit and the `transformers` library.

## Features

- Analyze the sentiment of multiple sentences.
- Display results with sentiment labels and confidence scores.
- Provide example sentences for quick testing.
- Clear input functionality.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/project1.git
    cd project1
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run project1_cv.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter one or more sentences (each sentence on a new line) in the text area provided.

4. Click the "Analyze Sentiment" button to see the sentiment analysis results.

## Example

You can try the example sentences provided by clicking the "Try an Example" button. The example sentences include:

- "I love this place, it's amazing!"
- "The service was very bad."
- "It's okay, nothing special."
- "I'm extremely disappointed!"
- "This is the best experience I've ever had!"

## Dependencies

- [streamlit](http://_vscodecontentref_/0)
- [transformers](http://_vscodecontentref_/1)
- [pandas](http://_vscodecontentref_/2)

## License

This project is licensed under the MIT License. See the LICENSE file for details.