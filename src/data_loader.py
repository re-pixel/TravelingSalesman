import json


class DataLoader:
    @staticmethod
    def load_data(loc):
        with open(loc, 'r') as f:
            data = f.read()
            return data

    @staticmethod
    def parse_tsm_data(data):
        data = data.split('\n')
        data = [line.split()[1:] for line in data if line.strip()]
        data = [[float(num) for num in line] for line in data]
        return data

    @staticmethod
    def get_tsm_data(loc):
        data = DataLoader.load_data(loc)
        return DataLoader.parse_tsm_data(data)

    @staticmethod
    def load_json(loc):
        with open(loc, 'r') as f:
            data = json.load(f)
            return data
