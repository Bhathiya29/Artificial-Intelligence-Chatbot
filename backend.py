# THE BACK-END OF THE CHATBOT
import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "ENTER YOUR OPEN AI API KEY HERE "

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine='text-davinci-003',  # Algorithm
            prompt=user_input,  # The users input
            max_tokens=3000,  # Max no of words
            temperature=0.5  # Accuracy and diversity of answers

        ).choices[0].text

        return response


if __name__ == '__main__':
    chatbot =Chatbot()
    response = chatbot.get_response('Write a joke')
    print(response)
