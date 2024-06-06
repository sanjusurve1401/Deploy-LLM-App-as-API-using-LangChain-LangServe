import requests

# Function to generate prompt based on user's choice
def generate_prompt(choice):
    if choice == "essay":
        return "provide me an essay about {topic}"
    elif choice == "poem":
        return "provide me a poem about {topic}"
    elif choice == "story":
        return "write a short story about {topic}"
    elif choice == "dialogue":
        return "write a conversation between {character1} and {character2} discussing {topic}"
    elif choice == "article":
        return "write an article about {topic}"
    
    else:
        return None

# Function to get the topic from the user
def get_topic():
    return input("Enter the topic: ")

# User's choice
user_choice = input("Enter your choice (essay/poem/story/dialogue/article): ")

# Getting the topic from the user
topic = get_topic()

# Generating prompt based on user's choice
prompt_template = generate_prompt(user_choice)

if prompt_template:
    response = requests.post(
        f"http://localhost:8000/{user_choice}/invoke",
        json={'input': {'topic': topic}}
    )

    # Extracting the story content from the response JSON
    story_content = response.json()['output']['content']

    # Printing only the story content
    print("\n", story_content)
else:
    print("\nInvalid choice! Please choose from essay, poem, story, dialogue, or article.")
