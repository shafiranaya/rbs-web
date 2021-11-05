from clips import Environment

env = Environment()

if __name__ == "__main__":
    env.clear()
    env.load("lip-products-recommendation.clp")
    for rule in env.rules():
        print(rule)
