import argparse
import crawler
import injector
import sys

def mainVerbose(args):
    #payload = "<script>alert(1);</script>" TODO: Add more scripts to test with
    if args['payload'] != '':
        payload = args['payload']    
    if args['inject']:
        injector.inject(args['url'], payload, args['keyword'], args['cookie'])
    else:
        crawler.crawl(args['url'], payload, args['keyword'], args['cookie'])

def mainCLI(args):
    payload = "<script>alert(1);</script>" #TODO: Add more scripts to test with
    if args.payload != '':
        payload = args.payload    
    if args.inject:
        injector.inject(args.url, payload, args.keyword, args.cookie)
    else:
        crawler.crawl(args.url, payload, args.keyword, args.cookie)

def printASCII():
    wolf = '''
       @@                                            
      @@@#                                           
     @@@@@%                                          
      @@@@@@@                                        
      @@@@@@@&                                       
      @@@@@@@@,                                      
      @@@@@@@@@@#                                    
     .@@@@@@@@@@@                                    
     @@@@@@@@@@@@@.                                  
     @@@@@@@@@@@@@@@(                                
     #@@@@@@@@@@@@@@@@@@                             
      %@@@@@@@@@@@@@@@@@@@@                          
       @@@@@@@@@@@@@@@@@@@@@@@@@@                    
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
         #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
             @@@*& @@@      @@@@@@@@@@@@ @@@@@@@@@@@ 
              @@   @@@      @@@@@@@@@@@@*   @@@@,      _____                __   .__ 
              @@   @@@       @@@@@@@@@@@@            _/ ____\______   ____ |  | _|__|
             #@@   (@@        @@@@@  @@@@@&          \   _ _\\_  __ \_/ __ \|  |/ /  |
             @@/   @@@          @@@    @@@@           |  |   |  | \/\  ___/|    <|  |
           %@@@   @@@            @@@    #@@@          |__|   |__|    \___  >__|_ \__|
        @@@@@@/ @@@@@            @@@     .@@                             \/     \/   
       @@@@@@@@@@@@@@@@@@@@@&    @@,      #@@        XOR's Hammer 2018
      ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@       &@@        Created for HackSmith v2.0
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@        
     *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%    
    '''
    print(wolf)
    print('''
Welcome to freki, the Persistent XSS Detector.
P.S. Auto-injection is kind of buggy right now, so we would prefer if you manually injected your script into the targeted form beforehand :X
        
        ''')

if __name__ == "__main__":
    printASCII()
    if len(sys.argv) == 1:
        running = True
        while running:
            url = ''
            while url == '':
                url = input("Enter URL to test for presence of Persistent XSS: ")
            payload = ''
            while payload == '':
                payload = input("Enter the payload used: ")
            print("Does the site require cookie authentication? If so, paste your cookie here, otherwise, just hit enter.")
            cookie = input("Cookie: ")
            keyword = ''
            inject= input("Do you want to try the auto-inject function before searching for the payload? (y/N):")
            if inject.lower() != 'y':
                inject = False
            else:
                inject = True
            args = {}
            args['url'] = url
            args['payload'] = payload
            args['cookie'] = cookie
            args['keyword'] = keyword
            args['inject'] = inject
            mainVerbose(args)
            break
    else:
        parser = argparse.ArgumentParser(argument_default='')
        parser.add_argument("-u", "--url", help="URL of website to fetch", type=str, required=True)
        parser.add_argument("-p", "--payload", help="Malicious script to submit as payload, otherwise we default", type=str, required=False)
        parser.add_argument("-c", "--cookie", help="For user identifcation purposes", type=str, required=False)
        parser.add_argument("-k", "--keyword", help="Restrict search within the domain of a keyword", type=str, required=False)
        parser.add_argument("-i", "--inject", help="Toggle on Injection mode", action='store_true', required=False)
        args = parser.parse_args()
        mainCLI(args)
