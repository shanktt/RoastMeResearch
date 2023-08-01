import pandas as pd
import sys

BADLY_ENCODED_STRINGS = "\x19"
REGEX = r'\/comments\/([a-zA-Z0-9]+)'


def main():
    file_name = sys.argv[1]  # first argument is the name of the input file
    columnn = sys.argv[2]  # second argument is the name of the column containing the text of the comments

    df = pd.read_csv(file_name)

    # Fix apostrophes
    df[columnn] = df[columnn].str.replace(BADLY_ENCODED_STRINGS, '\'')

    # Create link_id column
    df['id'] = df['url'].str.extract(REGEX)

    df.to_csv(file_name, index=False)


if __name__ == "__main__":
    main()
