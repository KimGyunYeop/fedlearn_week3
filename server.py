from symbol import parameters
from typing import List, Tuple
import wandb

import flwr.server.strategy
from flwr.server.client_manager import SimpleClientManager
# from fedavg_local import FedAvg
import flwr as fl
from flwr.common import Metrics, Parameters
from client import femnist_network 

import argparse

STRATEGY_LIST = {
    "fedavg": flwr.server.strategy.FedAvg,
    "fedavgm": flwr.server.strategy.FedAvgM,
    "qfedavg": flwr.server.strategy.QFedAvg,
    "faulttolearnfedavg": flwr.server.strategy.FaultTolerantFedAvg,
    "fedopt": flwr.server.strategy.FedOpt,
    "fedadagrad": flwr.server.strategy.FedAdagrad,
    "fedadam": flwr.server.strategy.FedAdam,
    "fedyogi": flwr.server.strategy.FedYogi
}

if __name__ == "__main__":

    def weighted_average(metrics: List[Tuple[int, Metrics]]) -> Metrics:
        # Multiply accuracy of each client by number of examples used
        accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
        examples = [num_examples for num_examples, _ in metrics]

        # Aggregate and return custom metric (weighted average)
        print("accuracy : {}".format(sum(accuracies) / sum(examples)))
        wandb.log({"accuracy": sum(accuracies) / sum(examples)})
        return {"accuracy": sum(accuracies) / sum(examples)}
    
    parser = argparse.ArgumentParser(description='federate learning')
    parser.add_argument('--method', type=str, required=True, choices=STRATEGY_LIST.keys())
    parser.add_argument('--port', default=8080)

    args = parser.parse_args()
    
    wandb.login()
    wandb.init(project="fedLearn_test", entity="gyunyeop", name=args.method)
    
    # Define strategy
    # client_manager = SimpleClientManager()
    strategy = STRATEGY_LIST[args.method](min_fit_clients=9, min_available_clients=9, evaluate_metrics_aggregation_fn=weighted_average)
    # server = Server(client_manager=client_manager, strategy=strategy)

    # Start Flower server
    fl.server.start_server(
        server_address="0.0.0.0:"+str(args.port),
        config=fl.server.ServerConfig(num_rounds=1000),
        strategy=strategy,
    )
