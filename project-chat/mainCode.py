import json
import random
import time
import datetime
import textwrap

# File Names List
schemaFile = "chatSchema.json"
logFile = "chatLogFile.txt"

# Agent Names List
agent = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George",
         "Hannah", "Ivan", "Julia", "Kevin", "Linda", "Michael", "Nancy",
         "Oscar", "Pamela", "Quincy", "Rachel", "Sam", "Tina", "Ursula",
         "Victor", "Wendy", "Xavier", "Yvonne", "Zach"]

# Function to load JSON file with utf-8 encoding
def load_json_file():
    with open(schemaFile, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Load JSON file
jsonData = load_json_file()

def print_in_box(text):
    # Determine the width of the box
    lines = textwrap.wrap(text, width=90)
    max_length = max(len(line) for line in lines)
    border = '─' * (max_length + 2)
    print(f"┌{border}┐")
    for line in lines:
        print(f"│ {line.ljust(max_length)} │")
    print(f"└{border}┘")

def print_list_in_box(items):
    # Determine the width of the box
    lines = []
    for idx, item in enumerate(items, 1):
        wrapped_text = textwrap.fill(f"{idx}. {item}", width=90)
        lines.extend(wrapped_text.split('\n'))
    max_length = max(len(line) for line in lines)
    border = '─' * (max_length + 2)
    print(f"┌{border}┐")
    for line in lines:
        print(f"│ {line.ljust(max_length)} │")
    print(f"└{border}┘")

def print_response_word_by_word(text, currentAgent, delay=0.2):
    words = text.split()
    response = f"{currentAgent}:"
    current_line = response
    lines = []
    
    for word in words:
        if len(current_line) + len(word) + 1 > 90:
            lines.append(current_line)
            current_line = word
        else:
            current_line += ' ' + word
    if current_line.strip():
        lines.append(current_line)
    
    # Determine the width of the box
    max_length = max(len(line) for line in lines)
    border = '─' * (max_length + 2)
    
    print(f"┌{border}┐")
    for line in lines:
        print(f"│ {line.ljust(max_length)} │", end='', flush=True)
        time.sleep(delay)
        print(f"\r│ {line.ljust(max_length)} │", flush=True)
    print(f"└{border}┘")

# Create log file
def createLogFile(datas):
    try:
        with open(logFile, "a") as file:
            file.write(str(datetime.datetime.now()))
            file.write("\n")
            if isinstance(datas, list):
                for data in datas:
                    file.write(data)
                    file.write("\n")
            else:
                file.write(datas)
            file.write("\n\n")
    except Exception as e:
        print('File Not Found Error:', e)

# Function to find responses for a given keyword
def find_responses(keyword, currentUser):
    keyword_lower = keyword.lower()
    
    # Check for an exact match
    for intent in jsonData["intents"]:
        for pattern in intent["patterns"]:
            if keyword_lower == pattern.lower():
                return [response.replace("{user}", currentUser) for response in intent["responses"]]
    
    # If no exact match is found, split the keyword into words
    keyword_words = keyword_lower.split()
    filtered_patterns = []
    
    for intent in jsonData["intents"]:
        for pattern in intent["patterns"]:
            pattern_lower = pattern.lower()
            # Check if all words in the keyword are present in the pattern
            if all(word in pattern_lower for word in keyword_words):
                filtered_patterns.append(pattern)
    
    if len(filtered_patterns) == 0:
        # If no patterns match all words, find the pattern that matches the maximum number of words
        max_match_count = 0
        best_patterns = []
        
        for intent in jsonData["intents"]:
            for pattern in intent["patterns"]:
                pattern_lower = pattern.lower()
                match_count = sum(word in pattern_lower for word in keyword_words)
                
                if match_count > max_match_count:
                    max_match_count = match_count
                    best_patterns = [pattern]
                elif match_count == max_match_count:
                    best_patterns.append(pattern)
        
        if max_match_count == 0:
            # If no words match, return a default response
            return ["Sorry, I do not understand that."]
        else:
            if len(keyword) > 15 and len(best_patterns) == 1:
                for intent in jsonData["intents"]:
                    for pattern in intent["patterns"]:
                        if best_patterns[0].lower() == pattern.lower():
                            return [response.replace("{user}", currentUser) for response in intent["responses"]]
            else:
                return [random.choice(jsonData["intents"][0]["responses"]).replace("{user}", currentUser)]
    elif len(filtered_patterns) == 1:
        # Find the corresponding responses for the single matched pattern
        for intent in jsonData["intents"]:
            if filtered_patterns[0] in intent["patterns"]:
                return [response.replace("{user}", currentUser) for response in intent["responses"]]
    else:
        return filtered_patterns

# Simulate thinking
def simulate_thinking():
    print("Chatbot is thinking...", flush=True)
    time.sleep(random.uniform(1, 2))

def print_boxed_message(message, width=60):
    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    border = '─' * (max_length + 2)
    print(f"┌{border}┐")
    for line in lines:
        print(f"│ {line.center(max_length)} │")
    print(f"└{border}┘")

# ASCII Art for University Name
header_art = """

██████╗  ██████╗ ██████╗ ██████╗ ██╗     ███████╗████████╗ ██████╗ ███╗   ██╗     ██████╗██╗  ██╗ █████╗ ████████╗██████╗  ██████╗ ████████╗
██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝╚══██╔══╝██╔═══██╗████╗  ██║    ██╔════╝██║  ██║██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝██║   ██║██████╔╝██████╔╝██║     █████╗     ██║   ██║   ██║██╔██╗ ██║    ██║     ███████║███████║   ██║   ██████╔╝██║   ██║   ██║   
██╔═══╝ ██║   ██║██╔═══╝ ██╔═══╝ ██║     ██╔══╝     ██║   ██║   ██║██║╚██╗██║    ██║     ██╔══██║██╔══██║   ██║   ██╔══██╗██║   ██║   ██║   
██║     ╚██████╔╝██║     ██║     ███████╗███████╗   ██║   ╚██████╔╝██║ ╚████║    ╚██████╗██║  ██║██║  ██║   ██║   ██████╔╝╚██████╔╝   ██║   
╚═╝      ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝  ╚═════╝    ╚═╝   
                                                                                                                                            
"""

# Assign a random agent to the user
currentAgent = random.choice(agent)

# Get the user's name
currentUser = input("Enter your name: ")

# Prepare the welcome message
welcome_message = f"""
Welcome to our University Chatbot Service!
Hi {currentUser}!
I am Agent {currentAgent}
How can I help you today?
"""

# Print the university name and welcome message in a boxed format
print(header_art)
print_boxed_message(welcome_message.strip())

# Main loop
while True:
    keyword = input(f"\n{currentUser}: ").strip()

    # Print the user's input in a box
    user_input = f"{currentUser}: {keyword}"
    print_in_box(user_input)

    # Simulate thinking
    simulate_thinking()
    
    # Find responses for the keyword
    responses = find_responses(keyword, currentUser)
    if isinstance(responses, list):
        if "Sad to see you go :(" in responses or "Goodbye!" in responses or "Come back soon!" in responses or "exit" in keyword.lower() or "quit" in keyword.lower() or "bye" in keyword.lower():
            byebyeResponse = random.choice(responses)
            # Log the conversation
            createLogFile([f"{currentUser}: {keyword}", f"Agent {currentAgent}: {byebyeResponse}"])
            print_response_word_by_word(byebyeResponse, currentAgent)
            break
        elif "?" in responses[0] and len(responses) >= 1:
            # Prompt the user with a similar question
            print("Did you Mean?\n")
            print_list_in_box(responses)
        else:
            # Respond with one of the possible responses
            multipleListResponses = random.choice(responses)
            createLogFile([f"{currentUser}: {keyword}", f"Agent {currentAgent}: {multipleListResponses}"])
            print_response_word_by_word(multipleListResponses, currentAgent)
    else:
        # Respond with the single response
        notListResponses = responses
        createLogFile([f"{currentUser}: {keyword}", f"Agent {currentAgent}: {notListResponses}"])
        print_response_word_by_word(notListResponses, currentAgent)