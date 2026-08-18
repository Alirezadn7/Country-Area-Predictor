import subprocess
import sys


def run(script, interactive=False):
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f"{script} failed.")
        sys.exit(1)


def main():
    print("1) Scraping data...")
    run("webscrape.py")

    print("2) Training model...")
    run("ml.py")

    print("3) Testing model...")
    run("predict.py", interactive=True)


if __name__ == "__main__":
    main()