import json

def main():
    with open("params.json", "r") as f:
        params = json.load(f)

    print("Paramètres reçus :", params)

    print("Hello")
if __name__ == "__main__":
    main()
