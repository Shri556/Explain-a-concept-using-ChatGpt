import openai

openai.api_key = "<YOUR_API>"

class Generate():

    def __init__(self,text_to_send):
        self.text_to_send = text_to_send

    def send_response(self):
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages =[
                {
                    "role":"system",
                    "content":"Explain Concept"
                },

                {
                    "role":"user",
                    "content":f"{self.text_to_send}"
                }
            ],
            temperature = 1,
            max_tokens = 256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        result = {
            "id":response.id,
            "output":response.choices
        }

        return result["output"][0]["message"]["content"]