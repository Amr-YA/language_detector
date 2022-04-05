# language_detector

Language detector trained with 12 languages (English, Arabic, Danish, French, German, Hindi, Italian, Portugeese, Russian, Spanish, Sweedish, Turkish)

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
