# language_detector

Language detector trained with 12 languages 

The languages:
- English: en,
- Danish: da,
- French: fr,
- German: ge,
- Hindi: hi,
- Italian: it,
- Portugeese: po,
- Russian: ru,
- Spanish: sp,
- Sweedish: sw,
- Turkish: tu,
- Arabic: ar

## Building the docker
docker build -t language_detector:latest .

## Run docker
docker run -p 5005:5005 language_detector:latest

## API Post
requests.post("http://localhost:5005/predict", 
		json={"sender": "amr", "message': "text"})

## API Response
{
	"sender": sender,
	"lang": language
}
