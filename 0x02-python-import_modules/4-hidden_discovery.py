#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    x = dir(hidden_4)

    for mod in x:
        if mod[:2] != "__":
            print(mod)
