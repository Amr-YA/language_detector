# Language Detector

Language detector trained with 12 languages, takes in a text and return the language through API

The languages:
- English: en
- Arabic: ar
- Danish: da
- French: fr
- German: ge
- Hindi: hi
- Italian: it
- Portugeese: po
- Russian: ru
- Spanish: sp
- Sweedish: sw
- Turkish: tu

## Building the docker
docker build -t language_detector:latest .

## Run docker
docker run -p 3000:3000 language_detector:latest

## Prediction:
### API
requests.post("http://localhost:3000/predict", 
		json={"sender": "amr", "message': "text"})

### Response
{
	"sender": sender,
	"lang": language
}

## Healthcheack:
### API
requests.get("http://localhost:3000/healthcheck")

### Response
{
	"success": "true"
}

**Status codes for healthcheck**:
1. 200: Model running and prediction is successful
2. 426: Model running but prediction was not successful, code needs to be edited
3. 500: Model not responding
