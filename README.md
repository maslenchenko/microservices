# Microservices-Basics
### Project Installation
To clone the project, run:
```shell
$ mkdir ~/workdir
$ cd ~/workdir
$ git clone https://github.com/maslenchenko/microservices.git
$ cd microservices
```
To start the project, execute the following commands:
```shell
$ python .\src\logging-service.py
$ python .\src\messages-service.py
$ python .\src\facade-service.py
```
### Project Testing
Then, to test the microservice, run `test.py` script, it will consecutively make two POST and two GET requests:
```shell
$ python .\test.py
```
And here how it looks when all services are running:
![image](https://github.com/maslenchenko/microservices/assets/91615687/ddf09bb4-a32e-4dd7-bebf-11c955698725)
Here is a closer look:
![image](https://github.com/maslenchenko/microservices/assets/91615687/115a246e-14d1-4860-8776-f6ff37ddc95f)

