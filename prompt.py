import requests
import numpy as np

#request for  hugging face
def query(API_URL, headers, payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

#generate the sentence based on inputs by bloom model
def generate_text(text, name):
	text = "Follow the describe \""+text+"\" to generate the investor profile, including investing experience, risk tolerance, expected return, age, capital, goal between inflation rate and return. And just return the profile description."
	API_URL = f"https://api-inference.huggingface.co/models/google/{name}"
	headers = {"Authorization": f"Bearer {API_KEY}"}
	output = query(API_URL, headers,
	{"inputs": text,
	"parameters": {"return_full_text":False,
					}
	})
	return [item['generated_text'].replace("\n",'') for item in output][0]

#fill the [MASK] for how much capital can invest
def money_text(text,name):
	text = text + "I have $[MASK] thousand to invest."
	API_URL = f"https://api-inference.huggingface.co/models/{name}"
	headers = {"Authorization": f"Bearer {API_KEY}"}
	output = query(API_URL, headers, {
		"inputs": text
	})
	sequence = [item['sequence'].split(". ")[-1] for item in output]
	score = [item['score'] for item in output]
	flag = np.argmax(score)
	return sequence[flag][0].upper() + sequence[flag][1:]

#fill the [MASK] for what kind of investor
def investor_text(text, name):
	text = text + "I am a [MASK] investor."
	API_URL = f"https://api-inference.huggingface.co/models/{name}"
	headers = {"Authorization": f"Bearer {API_KEY}"}
	output = query(API_URL, headers, {
		"inputs": text
	})
	sequence = [item['sequence'].split(". ")[-1] for item in output]
	score = [item['score'] for item in output]
	flag = np.argmax(score)
	return sequence[flag][0].upper() + sequence[flag][1:]

#zero shot for risk lavel
def risk_text(text, name):
	text = text + "I am an investor who likes [MASK] risk."
	API_URL = f"https://api-inference.huggingface.co/models/{name}"
	headers = {"Authorization": f"Bearer {API_KEY}"}
	output = query(API_URL, headers, {
		"inputs": text
	})
	sequence = [item['sequence'].split(". ")[-1] for item in output]
	score = [item['score'] for item in output]
	flag = np.argmax(score)
	return sequence[flag][0].upper() + sequence[flag][1:]
	
#zero shot for reward(return) lavel
def reward_text(text, name):
	text = text + "I am an investor who likes [MASK] returns."
	API_URL = f"https://api-inference.huggingface.co/models/{name}"
	headers = {"Authorization": f"Bearer {API_KEY}"}
	output = query(API_URL, headers, {
		"inputs": text
	})
	sequence = [item['sequence'].split(". ")[-1] for item in output]
	score = [item['score'] for item in output]
	flag = np.argmax(score)
	return sequence[flag][0].upper() + sequence[flag][1:]

#fill the [MASK] for the investor age.
def age_text(text, name):
	text =  text + "My age is [MASK] years old."
	API_URL = f"https://api-inference.huggingface.co/models/{name}"
	headers = {"Authorization": f"Bearer {API_KEY}"}
	output = query(API_URL, headers, {
		"inputs": text
	})
	sequence = [item['sequence'].split(". ")[-1] for item in output]
	score = [item['score'] for item in output]
	flag = np.argmax(score)
	return sequence[flag][0].upper() + sequence[flag][1:]


#fill the [MASK] for how many year investoring experiencement. 
def experience_text(text, name):
	text =  text + "I have [MASK] years of investment experience."
	API_URL = f"https://api-inference.huggingface.co/models/{name}"
	headers = {"Authorization": f"Bearer {API_KEY}"}
	output = query(API_URL, headers, {
		"inputs": text
	})
	sequence = [item['sequence'].split(". ")[-1] for item in output]
	score = [item['score'] for item in output]
	flag = np.argmax(score)
	return sequence[flag][0].upper() + sequence[flag][1:]

#fill the [MASK] for know what investoring goal
def goal_text(text, name):
	text = text + "Expected returns can significantly [MASK] the inflation rate and are suitable for volatile investments."
	API_URL = f"https://api-inference.huggingface.co/models/{name}"
	headers = {"Authorization": f"Bearer {API_KEY}"}
	output = query(API_URL, headers, {
		"inputs": text
	})
	sequence = [item['sequence'].split(". ")[-1] for item in output]
	score = [item['score'] for item in output]
	flag = np.argmax(score)
	return sequence[flag][0].upper() + sequence[flag][1:]

# Using prompt with MASK
def single_mask(inputs, text_mask_model_name):
	inputs_money = money_text(inputs, text_mask_model_name)
	inputs_risk = risk_text(inputs, text_mask_model_name)
	inputs_reward = reward_text(inputs, text_mask_model_name)
	inputs_age = age_text(inputs, text_mask_model_name)
	inputs_experience = experience_text(inputs, text_mask_model_name)
	inputs_goal = goal_text(inputs, text_mask_model_name)
	inputs_investor = investor_text(inputs, text_mask_model_name)
	return begin_text + ' ' + inputs + ' ' + inputs_money + ' '  + inputs_risk + ' '  + inputs_reward + ' '  + inputs_age + ' '  + inputs_experience + ' '  + inputs_goal + ' '  + inputs_investor + ' '  + end_text

# Using prompt with GENERATE
def single_generate(inputs, text_generate_model_name):
	inputs_generate = generate_text(inputs, text_generate_model_name)
	return begin_text + ' '  + inputs + ' '  + inputs_generate + ' '  + end_text

#init parameters
API_KEY = "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" # using hugging face api 
begin_text = "Based on the provided investor profile, create a well-structured portfolio recommendation from the New York Stock Exchange." #begin prompt text
end_text = "Additionally, provide potential values for Sharpe ratio, maximum drawdown, return, and associated risks with the recommended portfolio. Your analysis should be detailed and aligned with the investor's circumstances and goals, considering their risk tolerance, investment experience, and returns. Please ensure that the portfolio recommendations are tailored to meet the investor's specific requirements and provide a clear rationale for each recommendation." #final prompt text
text_generate_model_name = "flan-t5-xxl" #["flan-t5-xxl", "Chinese-Llama-2-7b"] # generate text model
text_mask_model_name = "bert-base-uncased" #["bert-base-uncased", "xlm-roberta-base", "bert-base-chinese"]) # mask fill model