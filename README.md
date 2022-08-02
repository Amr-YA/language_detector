# Language Detector

Language detector trained with 12 languages, takes in a text and return the language through API

The languages:
- English: en
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
- Arabic: ar

## Installation
### Building with docker
build the project using docker, and give it a tag "language_detector"
`docker build -t language_detector:latest .`

### Run with docker
tun the image built previously using the tage "language_detector"
`docker run -p 5005:5005 language_detector:latest`

## Usage
### API Post
send a text to the model using:
`requests.post("http://localhost:5005/predict", 
		json={"sender": "amr", "message': "text"})`

### API Response
the reply of the post request containing the detected language 
`{
	"sender": sender,
	"lang": language
}`
