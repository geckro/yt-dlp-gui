import log
import tomllib

TOML_PATH = "data/data.toml"


def read_toml():
    """
    Reads a TOML file that has all the information for yt-dlp configurations.
    Returns: toml data if no errors were found, None otherwise
    """
    try:
        with open(TOML_PATH, 'rb') as toml_file:
            toml = tomllib.load(toml_file)
            logging.debug(f"TOML data: {toml}")
        return toml
    except FileNotFoundError:
        logging.error(f"Could not find TOML File at: {TOML_PATH}")
        return None
    except tomllib.TOMLDecodeError as e:
        logging.error(f"Could not decode TOML file: {e}")
        return None
