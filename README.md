# fedlearn_week3_homework

Federate learning practice using flower  

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
    
