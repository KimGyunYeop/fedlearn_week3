# fedlearn_week3_homework

Federate learning practice using flower  
flower에서 제공하는 여러 strategy들을 사용할 수 있도록 수정  
https://flower.dev/docs/apiref-flwr.html?highlight=fedavg#flwr.server.strategy.FedAvg  

### usage  
여러개의 실험을 동시에 진행하기 위해 gpu number와 port를 직접 지정할 수 있도록 수정  
사전에 제공된 Femnist 링크에서의 data.zip을 폴더 내부에 다운로드 후 unzip해주어야함

#### server.py  
federate learning을 위해 각 edge들의 학습 결과를 종합하여 server에서 학습하는 파일  

    python server.py --method <method_name> --port <port_num>  
    
method name list = ['fedavg', 'fedavgm', 'qfedavg', 'faulttolearnfedavg', 'fedopt', 'fedadagrad', 'fedadam', 'fedyogi']  

#### client.py
각 client(edge)에서 학습을 진행하고 server로 전송하는 파일 

    python client.py --gpu <gpu_num> --port <port_num>   
    
### experiment  
각 방법론에 대한 실험 결과
#### fedavg  
![fedavg](https://user-images.githubusercontent.com/44080708/191684448-3d213ed1-5478-446a-9e56-9ff1dd783a5b.png)
#### fedavgm  
![fedavgm](https://user-images.githubusercontent.com/44080708/191684469-f1e8d7ad-4184-46d1-8de6-e66bd6c6443e.png)   
#### faulttolearnfedavg  
![faulttolearnfedavg](https://user-images.githubusercontent.com/44080708/191684459-fe0bbb51-e5c7-4658-bb7b-19aa61b55708.png)
#### fedopt  
![fadopt](https://user-images.githubusercontent.com/44080708/192958418-8d19add8-924a-43b0-840a-9ffe33acd7ea.png)
#### fedadagrad  
![fedadagrad](https://user-images.githubusercontent.com/44080708/192958427-6a7295be-665d-4a08-ae85-28301cf664e3.png)
#### fedadam   
server와 client의 lr을 0.001로 사용해야 학습됨
![fedadam](https://user-images.githubusercontent.com/44080708/192958445-5cf4a6f7-3c25-43ba-aa00-247d6f97196b.png)   
defalut일때(1)
![fedadam_falut](https://user-images.githubusercontent.com/44080708/192958432-333b28f2-239d-455f-9981-0fb8e4685d9e.png)

#### fedyogi
![W B Chart 2022  9  22  오후 10_31_08](https://user-images.githubusercontent.com/44080708/191760731-f41f6841-d4aa-4cf9-96a8-1e39dbcdb97a.png)
#### whole  
![all (1)](https://user-images.githubusercontent.com/44080708/192958408-3ef3a4f1-ce19-47a1-8aca-e52c434228e8.png)


### 결론   
hyper parameter tuning을 하지않아 완벽한 성능은 아니지만 전체적으로 fedadagrad, fedadam, fedyogi가 전체적으로 기조가 비슷한 방법론을 사용하는데 해당 방법론들의 성능이 뛰어나다.
