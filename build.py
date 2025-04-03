#! ./.venv/bin/python

# https://github.com/devidw/obsidian-to-hugo
import os
from obsidian_to_hugo import ObsidianToHugo

def filter_regex(file_contents: str, file_path: str) -> bool:
    return not 'Regex' in file_path

def filter_readmes(file_contents: str, file_path: str) -> bool:
    return not 'README.md' in file_path

if not os.path.exists('./content/wiki'):
    os.makedirs('./content/wiki')

obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir=os.path.expanduser("~/dev/html/stem"),
    hugo_content_dir=os.path.normpath("./content/wiki"),
    filters=[filter_regex, filter_readmes],
)

obsidian_to_hugo.run()