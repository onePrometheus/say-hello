import json

def main():
    params = {}
    try:
        with open("params.json", "r") as f:
            params = json.load(f)
    except:
        pass

    print("Paramètres reçus :", params)

    print("Hello")
if __name__ == "__main__":
    main()
