# Detecção de Pessoas por IA

[Vídeo de Apresentação do Trabalho](https://youtu.be/OqSZh1aJNVk)

Parte do trabalho da disciplina de Sistemas Distribuídos do curso de Engenharia de Computação da Universidade Federal de Itajubá

Um script python que através da webcam do computador, detecta se há pessoas presentes. É feita uma requisição POST na URL do broker MQTT utilizado no projeto e o tópico "light" é alterado conforme a quantidade de pessoas detectadas: caso não tenha nenhuma pessoa, o estado do tópico é mudado para 0 (luz desligada) e caso tenha mais de uma pessoa, é mudado para 1 (luz ligada).

É necessário baixar o arquivo yolo.h5 disponível em: https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5

No arquivo "request.py", atribua à variável "url" a URL do broker.
