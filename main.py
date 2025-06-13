if __name__ == "__main__":
    from TSM import TSM

    with open('data_tsp.txt', 'r') as f:
        data = f.read()

    data = data.split('\n')
    data = [line.split()[1:] for line in data if line.strip()] 
    data = [[float(num) for num in line] for line in data]

    travelling_salesman = TSM(data)
    best_path, cost = travelling_salesman.run()
    print("Best path:", best_path, "with cost:", cost)