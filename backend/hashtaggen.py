import os
import openai
import json
import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    response = getHashtags(user_input)
    print(response)
        

#Invoke openAPI to get the list of hashtags from the userInput
def getHashtags(userInput):
    openai.apikey=os.getenv("OPENAI_API_KEY")
    enriched_prompts = "give me a list of hashtags for " + userInput
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=enriched_prompts,
        max_tokens=100)
    return response.choices[0].text

if __name__ == "__main__":
    main()