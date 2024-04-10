def main():
    # Trivial example to see who is calling
    print(f"{get_name()=}")


def get_name():
    return __name__
