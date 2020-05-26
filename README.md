<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://https://github.com/lhandal/tinder-bot/images/logo.jpg">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">TINDER AUTO-SWIPE BOT</h3>

  <p align="center">
    Tinder web automation and scraper to swipe based on user training. Built with Selenium and Keras in Python.
    <br />
    <a href="https://https://github.com/lhandal/tinder-bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://https://github.com/lhandal/tinder-bot">View Demo</a>
    ·
    <a href="https://https://github.com/lhandal/tinder-bot/issues">Report Bug</a>
    ·
    <a href="https://https://github.com/lhandal/tinder-bot/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This project started with the motivation of learning web automation and scraping with Python. After succesfully creating a bot that could:

* Open a browser
* Login to Tinder.com
* Accept all notifications and dismiss pop-ups
* Swipe right or left 100% of the times

We decided to add a deep learning model to predict the probability of likelyhood of a given user. The model we used is a Convolutional Neural Network trained from scratch with more than 10,000 images scraped from Tinder. The model consists of 5 convolutional layers and 3 dense layers. 

This yielded a total of around 1,000,000 trainable parameters for 300x300 grayscale images and took about 6 hours to train 20 epochs with a batches of 50.


### Built With

* [Python](https://www.python.org/)
* [Keras](https://keras.io/)
* [Selenium](https://selenium.dev)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Environment running python 3.6
- Tinder account with Facebook login enabled

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/lhandal/tinder-bot.git
```
2. Install required packages
```sh
pip install -r requirements.txt
```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/github_username/repo/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@lhandal](https://instagram.com/lhandal) - lhandalb@gmail.com

Project Link: [https://https://github.com/lhandal/tinder-bot](https://https://github.com/lhandal/tinder-bot)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://https://github.com/lhandal/tinder-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://https://github.com/lhandal/tinder-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://https://github.com/lhandal/tinder-bot/stargazers
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://https://github.com/lhandal/tinder-bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/lhandal
[product-screenshot]: images/screenshot.png
