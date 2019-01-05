# Freki - Persistent XSS Detector

![Freki Pic](https://raw.githubusercontent.com/chuayupeng/freki/master/img/freki.jpg)

Cross-site Scripting is one of the many vulnerabilities that can be found on a website, even been listed under as OWASP top 10. As a penetration tester, one can establish the fact that this vulnerability exist by attempting to submit malicious code into the website. But in a large scale system, how does a penetration tester verify which web pages are affected?  

Freki is a tool that scans all of the web pages, attempting to detect the presence of the malicious payload. This is achieved by leveraging on the capabilities of web crawlers written in Python. This allows the developer to scan through the website without manually sourcing through the webpage, thus achieving results much faster by automating such a tedious process.  

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* [Python 3.6.6 or above](https://www.python.org/)
* [pip 18.1 or above](https://pypi.org/project/pip/)

If your OS does not have pip installed, use the following command:

```
sudo easy-install pip
```

### Installing

1. Clone the directory
2. Enter the directory by typing in this command

```
cd freki
```

3. Install prerequisite libraries with pip:

```
pip install -r requirements.txt
```

4. If you are on Linux OS, you can run setup.sh instead:

```
./setup.sh
```

This allows Linux OS users to access the program from anywhere on the system using:

```
freki
```

## Usage

1. Run the program with this command:
```
python freki.py
```

If you ran setup.sh, you may run the program using this command:
```
freki
```

2. You will first be prompted to enter the site URL to test for Persistent XSS. An example is:
```
http://192.168.18.133/dvwa
```

3. Enter the payload to be used. An example is:
```
<script>alert('freki')</script>
```

4. If the site requires cookie authentication, provide them in the form:
```
'keyOne=valueOne;keyTwo=valueTwo'
```

5. Finally, indicate if you would like to auto-inject the payload before searching for its presence.

Example Usage:

![Freki Pic](https://raw.githubusercontent.com/chuayupeng/freki/master/img/frekiEg1.jpg)

Test Payload found:

![Freki Pic](https://raw.githubusercontent.com/chuayupeng/freki/master/img/frekiEg2.jpg)

## Built With

* Languages
    * [Python 3.6](https://www.python.org/) - For its standard libraries argparse, contextlib and urllib.

* Frameworks and Libraries
    * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - For dealing with HTML data.
    * [Requests](http://docs.python-requests.org/en/master/) - To send HTTP requests.


## Contributing

Please read our [CONTRIBUTING.md](https://github.com/chuayupeng/freki/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

For the versions available, see the [tags on this repository](https://github.com/chuayupeng/freki/tags). 

## Authors

* **Chua Yu Peng** - [chuayupeng](https://github.com/chuayupeng)
* **Clyde** - [weizhang05](https://github.com/weizhang05)
* **Tan Yong He** - [x3tsunayh](https://github.com/x3tsunayh)

See also the list of [contributors](https://github.com/chuayupeng/freki/contributors) who participated in this project.

## License

This project is licensed under the GNU GPL v3 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* Logo created by Freepik
