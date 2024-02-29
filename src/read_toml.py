import tomllib

from log import log

TOML_PATH = "src/data/data.toml"


def read_toml():
    """
    Reads a TOML file that has all the information for yt-dlp configurations.
    Returns: toml data if no errors were found, None otherwise
    """
    try:
        with open(TOML_PATH, 'rb') as toml_file:
            toml = tomllib.load(toml_file)
            log("debug", f"TOML data: {toml}")
        return toml
    except FileNotFoundError:
        log("error", f"Could not find TOML File at: {TOML_PATH}")
        return None
    except tomllib.TOMLDecodeError as e:
        log("error", f"Could not decode TOML file: {e}")
        return None
