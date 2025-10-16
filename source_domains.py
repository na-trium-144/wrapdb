import configparser
from pathlib import Path
from urllib.parse import urlparse
from typing import Dict


def main() -> None:
    domain_counts: Dict[str, int] = {}

    for file in Path("subprojects").iterdir():
        if file.is_file() and file.suffix == ".wrap":
            config = configparser.ConfigParser(interpolation=None)
            config.read(file)
            source_url = config["wrap-file"]["source_url"]
            parsed_url = urlparse(source_url)

            # maybe custom logic here depending on url or file name
            domain = parsed_url.netloc

            domain_counts[domain] = domain_counts.get(domain, 0) + 1

    for domain, count in sorted(
        domain_counts.items(), key=lambda item: item[1], reverse=True
    ):
        print(f"- [ ] {domain} ({count})")


if __name__ == "__main__":
    main()
