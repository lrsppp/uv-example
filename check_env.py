# check if PYTHONPATH was correctly set during (docker) build
import os

if __name__ == "__main__":
    print(os.environ["PYTHONPATH"])
    try:
        from core.config import settings  # noqa
    except ModuleNotFoundError as error:
        print(f"PYTHONPATH not correctly set. Adjust '.env'.")
