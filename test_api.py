from google import genai

client = genai.Client(api_key="AIzaSyDheZVPtUP3m9TYh_YOM3XIWSrT0kAAFPY")

models = client.models.list()

for m in models:
    print(m.name)