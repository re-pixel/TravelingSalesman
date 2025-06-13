if __name__ == "__main__":
    from TSM import TSM
    travelling_salesman = TSM()
    best_route, cost = travelling_salesman.run()
    print("Best route:", best_route, "with cost:", cost)