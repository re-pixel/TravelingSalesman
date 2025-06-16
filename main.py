if __name__ == "__main__":
    from TSM import TSM

    with open('data_tsp.txt', 'r') as f:
        data = f.read()

    data = data.split('\n')
    data = [line.split()[1:] for line in data if line.strip()]
    data = [[float(num) for num in line] for line in data]

    travelling_salesman = TSM(data)
    best_path, cost, optimality_gap = travelling_salesman.run()
    print(f"--- TSP Solution Details ---")
    print(f"Path Discovered: {best_path}")
    print(f"Calculated Tour Cost: {cost:.2f}")
    print(
        f"Relative to the lower bound, this solution is {optimality_gap * 100:.2f}% from optimal.")
    print(f"NOTE:: Our calculated 'optimal' serves as a measure against the 1-tree relaxation, not necessarily the exact optimal solution.")
    print(f"--------------------------")
