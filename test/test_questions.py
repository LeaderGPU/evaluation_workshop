import pandas as pd

def import_csv_data():
    df = pd.read_csv("../data/spells.csv", sep=";", encoding="cp1252")
    filtered = df[df["book"] == "Player's Handbook"]
    return filtered

def generate_test_cases(dataframe, batch_size=10):
    filtered = dataframe.sample(n=batch_size)

    test_case_dict = dict()

    for index, row in filtered.iterrows():
        question = f'What is the level of the spell {row["name"]}'
        answer = f'{row["level"]}'

        test_case_dict[question] = answer

    return test_case_dict



if __name__ == '__main__':
    data = import_csv_data()
    tests = generate_test_cases(data)
    print(tests)
