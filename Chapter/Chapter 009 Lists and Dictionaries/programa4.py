import argparse

parser = argparse.ArgumentParser()
parser.add_argument("edad", type=int)

args = parser.parse_args()

print(f"Edad: {args.edad}")