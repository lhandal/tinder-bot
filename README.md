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
  <a href="https://github.com/lhandal/tinder-bot/blob/master/images/logo.jpg">
    <img src="https://github.com/lhandal/tinder-bot/blob/master/images/logo.jpg" width="600">
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



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/lhandal/tinder-bot/blob/master/images/probs.png">
    <img src="https://github.com/lhandal/tinder-bot/blob/master/images/probs.png" width="800">
  </a>
  </p>
</p>
  
This project started with the motivation of learning web automation and scraping with Python. After succesfully creating a bot that could:

* Open a browser
* Login to Tinder.com
* Accept all notifications and dismiss pop-ups
* Swipe right or left 100% of the times

I decided to add a deep learning model to predict the probability of likelyhood of a given user. The model I used is a Convolutional Neural Network trained from scratch with more than 10,000 images scraped from Tinder. The model consists of 5 convolutional layers and 3 dense layers. 

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

### Option 1 - Training Your Own Model
1. First and foremost open the [secrets.py](https://github.com/lhandal/tinder-bot/blob/master/secrets.py) file and input your Facebook credentials to be able to login to Tinder. 

2. If you have your own images for training, skip to step 4. Else the [scraping script](https://github.com/lhandal/tinder-bot/blob/master/tinder_scraper.py) can be used. Just add the directory to save the pictures in the variable `pictures_folder` inside the script and run. If you want, you can also configure the scraper to swipe right or left as it gathers the pictures.

3. You will have to label all the images to be predicted as 1 by adding "yay_" before the file name and the ones to be predicted as 0 with "nay_".

4. Add the path where you have the images to the `path` variable inside the [train_script.py](https://github.com/lhandal/tinder-bot/blob/master/train_script.py) script and run it. This should take a while, depending on how many images you have scraped. The script will generate a `.h5` model file inside the same folder -- this is the trained model.

**Example**

I used a model consisting of 5 convolutional layers and 3 dense layers, with pooling and normalization between layers. I also added some dropouts to avoid overfitting:

``` py
model = Sequential()
model.add(Convolution2D(32, kernel_size = (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())

model.add(Convolution2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())

model.add(Convolution2D(96, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())

model.add(Convolution2D(96, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())

model.add(Convolution2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Flatten())

model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(1, activation = 'sigmoid'))
```
This model yielded very good results consideing I only trained 10,000 grayscale pictures (_grayscale to reduce the number of dimensions_), but feel free to modify it as you consider best.

The end results after training were:
```
Accuracy (test): 89% 
Precision 84%
Recall: 64%
```

### Option 2 - Use the Pre-trained Model
1. If you don't want to train your own model, I have included the model I trained for this project. It is under [model_03.h5](https://github.com/lhandal/tinder-bot/blob/master/model_03.h5). 

Disclaimer:
This model has been trained using the information I had available at the moment. It may *not* reflect in any way what I consider to be any standard for beauty. This is a sample project and is prone to mistakes.

### Running the Bot
1. If you haven't already done so, open the [secrets.py](https://github.com/lhandal/tinder-bot/blob/master/secrets.py) file and input your Facebook credentials to be able to login to Tinder. 

2. Open the [tinder_bot.py](https://github.com/lhandal/tinder-bot/blob/master/tinder_bot.py) script and change the `pictures_folder` variable to any path you like. This is a temporary folder for the model to store each image and analyze it. It will be deleted later. By default this is the `tmp/` folder.

3. Change the `model` variable to whatever model you want to use. The default is set to `model_03.h5` which I used to test the bot. \

4. (Optional) You can also later on change the `threshold` var to regulate the "pickyness" of the bot. Default is set to 70%.

5. Save the changes and run the script. You can run it from the terminal with

     ``` sh 
     python -i tinder_bot.py
     ```
   or open the `run_bot` executable file. 



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/github_username/repo/issues) for a list of proposed features (and known issues).

<!-- TODOS -->
## TODOs

* Add face recognition and body recognition to improve accuracy.
* Implement the posibility to use the Tinder API to avoid automation errors.
* Add Google and Phone login options for Tinder
* Train using color images to improve accuracy.



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
