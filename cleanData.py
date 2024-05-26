import pandas as pd
import numpy as np


class Pokemon:

    def __init__(self, df):
        data = pd.read_csv(df)
        data["total"] = (
            data["hp"]
            + data["attack"]
            + data["defense"]
            + data["sp_attack"]
            + data["sp_defense"]
            + data["speed"]
        )
        data["total"] = data["total"] - data["total"].mean()
        data["capture_rate"] = data["capture_rate"] - data["capture_rate"].mean()
        self.df = data[["name", "total", "capture_rate", "is_legendary"]].copy()

    def returnData(self, nameList):
        names = self.df[self.df["name"].isin(nameList)].to_numpy()
        return names[:, 0], names[:, 1:3], names[:, 3]

    def getTests(self, testNames):
        tests = self.df[self.df["name"].isin(testNames)].to_numpy()
        return tests[:, [0, 3]], tests[:, 1:3]


def main():
    df = "pokemon.csv"
    pkmn = Pokemon(df)
    names = ["Weedle", "Charmander", "Starly", "Mewtwo", "Dialga"]
    tests = ["Wurmple", "Palkia"]
    test_names, test_data = pkmn.getTests(tests)
    names, x_data, y_data = pkmn.returnData(names)
    print("--------------------- Names --------------------")
    print(names)
    print("--------------------- X_data --------------------")
    print(x_data)
    print("--------------------- Y_data --------------------")
    print(y_data)
    print("--------------------- Test_data --------------------")
    print(test_data)


if __name__ == "__main__":
    main()
