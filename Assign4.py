#Task 1: Customer Email Classification
emails = [
    "I have not received my invoice for last month.",
    "My payment was deducted twice.",
    "The app crashes when I try to log in.",
    "Unable to reset my password.",
    "Great service, I really like the new update.",
    "The customer support was very helpful.",
    "What are your working hours?",
    "Do you provide discounts for students?",
    "The website is too slow.",
    "Thanks for the quick response!"
]
def zero_shot_prompt(email):
    prompt = f"""
    Classify the following email into one of the categories:
    Billing, Technical Support, Feedback, Others.

    Email: "{email}"
    """
    return prompt
def one_shot_prompt(email):
    prompt = f"""
    Example:
    Email: "My internet bill is incorrect."
    Category: Billing

    Now classify:
    Email: "{email}"
    """
    return prompt
def few_shot_prompt(email):
    prompt = f"""
    Email: "My bill amount is wrong."
    Category: Billing

    Email: "The app is not opening."
    Category: Technical Support

    Email: "I love the new features."
    Category: Feedback

    Now classify:
    Email: "{email}"
    """
    return prompt
def is_valid(s):
    if len(s) == 0:
        return False
    return s[0].isupper() and s.endswith(".")   

#Task 2: Travel Query Classification

travel_queries = [
    "Book a flight from Delhi to Mumbai",
    "Cancel my hotel reservation",
    "What is the baggage limit?",
    "I need a hotel in Bangalore",
    "How to cancel my flight ticket?"
]
def travel_few_shot(query):
    prompt = f"""
    Query: "Book a flight from Delhi to Chennai"
    Category: Flight Booking

    Query: "Cancel my hotel reservation"
    Category: Cancellation

    Query: "Find hotels in Goa"
    Category: Hotel Booking

    Now classify:
    Query: "{query}"
    """
    return prompt

#Task 3: Programming Question Type Identification

coding_queries = [
    "Why is my code showing syntax error?",
    "My loop runs but gives wrong output",
    "How can I reduce time complexity?",
    "What is a Python dictionary?"
]
def coding_few_shot(query):
    prompt = f"""
    Question: "Missing colon in if statement"
    Category: Syntax Error

    Question: "Program runs but output is incorrect"
    Category: Logic Error

    Question: "How to make this code faster?"
    Category: Optimization

    Now classify:
    Question: "{query}"
    """
    return prompt
#Task 4: Social Media Post Categorization
posts = [
    "Worst service ever!",
    "Loved the new update!",
    "When will the sale start?",
    "Check out our latest offers"
]
def social_few_shot(post):
    prompt = f"""
    Post: "Amazing customer support!"
    Category: Appreciation

    Post: "This product stopped working"
    Category: Complaint

    Post: "Buy now with 50% off"
    Category: Promotion

    Now classify:
    Post: "{post}"
    """
    return prompt
