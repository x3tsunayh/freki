import argparse
import crawler

def main(args):
    crawler.crawl(args.url, args.payload, args.keyword, args.cookie)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL of website to fetch", type=str, required=True)
    parser.add_argument("-p", "--payload", help="Malicious script to submit as payload", type=str, required=True)
    parser.add_argument("-c", "--cookie", help="For user identifcation purposes", type=str, required=False)
    parser.add_argument("-k", "--keyword", help="Restrict search within the domain of a keyword", type=str, required=False)
    args = parser.parse_args()
    main(args)
