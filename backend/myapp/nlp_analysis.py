import spacy
from fuzzywuzzy import fuzz
# Load the English language model
nlp = spacy.load("en_core_web_sm")

def perform_nlp_analysis(user_objective):
    # Tokenize the user's input
    doc = nlp(user_objective)

    # Define contextually relevant keywords for different types of analysis
    analysis_keywords = {
        "Regression": ["predict", "relationship", "forecast", "trend", "correlation"],
        "linear regression": ["linear regression"],
        "regression trees": ["regression trees"],
        "non-linear regression": ["non-linear regression"],
        "polynomial regression": ["polynomial regression"],
        "classification": ["classify", "categorize", "identify", "group"],
        "decision tree": ["decision tree"],
        "random forest": ["random forest"],
        "exponential smoothing": ["exponential smoothing"],
        "hypothesis testing": ["test", "compare", "evaluate", "verify"],
        "t-test": ["t-test", "t test"],
        "z-test": ["z-test", "z test"],
        "descriptive statistics": ["summary", "overview", "statistics", "describe"],
    }

     # Initialize analysis type as "Not found"
    analysis_type = "Not found"

  # Initialize analysis type and similarity score
    analysis_type = "Not found"
    max_similarity = 0

    # Check for keywords in the user's input
    for keyword, keyword_list in analysis_keywords.items():
        for token in doc:
            for keyword_word in keyword_list:
                similarity = fuzz.ratio(token.text.lower(), keyword_word)
                if similarity > max_similarity:
                    max_similarity = similarity
                    analysis_type = keyword


    return analysis_type

