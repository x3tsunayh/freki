import argparse
import crawler
import injector

def main(args):
    if args.inject:
        injector.inject(args.url, args.payload, args.keyword, args.cookie)
    else:
        crawler.crawl(args.url, args.payload, args.keyword, args.cookie)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL of website to fetch", type=str, required=True)
    parser.add_argument("-p", "--payload", help="Malicious script to submit as payload", type=str, required=True)
    parser.add_argument("-c", "--cookie", help="For user identifcation purposes", type=str, required=False)
    parser.add_argument("-k", "--keyword", help="Restrict search within the domain of a keyword", type=str, required=False)
    parser.add_argument("-i", "--inject", help="Toggle on Injection mode", action='store_true', required=False)
    args = parser.parse_args()
    main(args)
