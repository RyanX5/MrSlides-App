from speech_to_text import audio_to_text as audioTT
import openai
import json

class chat:

	def __init__(self):

		self.API = 'insert-api-here'


	def request_text(self, filePath):

		speech = audioTT()
		openai.api_key = self.API

		text = speech.audio_text(filePath)

		print("We got: " + text)


		prompt = self.get_prompt(text)

		if prompt != "error":

			messages = [{"role": "user", "content": prompt}]

			response = openai.ChatCompletion.create(
	        model="gpt-3.5-turbo",
	        messages=messages
	    	)

			response_message = response['choices'][0]['message']['content']

			self.output_json(response_message)

			print(response_message)

			return response_message
		else:
			print("ERROR, COULDN'T DETECT WORDS.")
			return ""




	def get_prompt(self, prompt):

		boilerplate = """Create me a JSON file such that it contains information
						 that I can use to programmatically create Google Slides 
						 based on user's prompt which is as follows: \n"""

		footer = "\nGive me only the JSON file and no other text."

		format_ = """{
				  "title": "Presentation about (insert title)",
				  "slides": [
				    {
				      "title": "Topic 1",
				      "content": [
				        "insert content 1",
				        "insert content 2"
				      ]
				    },
				    {
				      "title": "Topic 2",
				      "content": [
				        "insert content 1",
				        "insert content 2"
				      ]
				    },
				    {
				      "title": "Topic 3",
				      "content": [
				        "insert content 1",
				        "insert content 2"
				      ]
				    },
				    {
				      "title": "Topic 4",
				      "content": [
				        "insert content 1",
				        "insert content 2"
				      ]
				    }
				  ]
				}\n Follow the above json template. Replace placeholder texts,
				and change the number of slides based on the prompt. Replace 'insert content'
				with relevant information, and NOT placeholders."""

		return boilerplate + prompt + footer + format_

	def output_json(self, response):
		response_data = json.loads(response)
		with open("output.json", "w") as json_file:
			json.dump(response_data, json_file, indent=4)






