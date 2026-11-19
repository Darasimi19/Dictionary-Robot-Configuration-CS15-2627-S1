robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

print(robot["name"])

print(robot["model"])

robot["battery"] = 100

robot["color"] = "wine"

robot.pop("mode")

print(len(robot))

for key, value in robot.items():
    print(key, "-", value)
