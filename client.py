import requests

def main():
    r = requests.get("http://vcm-3572.vm.duke.edu:5000/name")
    name = r.json()
    print(name)

    r2 = requests.get("http://vcm-3572.vm.duke.edu:5000/hello/zhiwei")
    message = r2.json()
    print(message)

    r3 = requests.post("http://vcm-3572.vm.duke.edu:5000/distance", json = {"a": [2,3], "b": [3,6]})
    distance_result = r3.json()
    print(distance_result)

if __name__ == "__main__":
    main()
