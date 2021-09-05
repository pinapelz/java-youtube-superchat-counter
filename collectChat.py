import argparse
from chat_downloader import ChatDownloader
parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()
downloader = ChatDownloader()
url = args.url
groups_example = downloader.get_chat(url, message_groups=['superchat'])
for message in groups_example:
    groups_example.print_formatted(message)

