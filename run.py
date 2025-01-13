import json
import time

def main():
    params = {}
    try:
        with open("params.json", "r") as f:
            params = json.load(f)
    except:
        pass

    print("Paramètres reçus :", params)
    print("Wait for 10 seconds")
    time.sleep(10)
    print("Hello")
if __name__ == "__main__":
    main()
