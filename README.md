<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/douglasjnr/sentiment-analysis">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Real-Time Twitter Sentiment Analysis</h3>

  <p align="center">
    A NLP project to perform Twitter Sentiment Analysis in real-time
    <br />
    <a href="https://github.com/douglasjnr/sentiment-analysis"><strong>Explore the docs »</strong></a>
    <br />
    <a href="#demo-preview">View Demo</a>
  </p>
</div>

<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#key-components">Key Components</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#demo-preview">Demo Preview</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This project analyzes sentiment from real-time Twitter (X) data using a deep learning approach. 
The goal is to classify tweets into four categories — **Positive**, **Neutral**, **Negative**, and **Irrelevant** — by training a Recurrent Neural Network (RNN) on labeled data, 
then integrating a live prediction interface using Streamlit.

It serves as a full-stack ML pipeline for natural language processing (NLP), suitable for applications in social listening, brand monitoring, or public opinion analysis.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### ⭐ Features:

* Live tweet fetching via Twitter API
* Sentiment classification: Positive, Neutral, Negative, Irrelevant
* Visual interface for predictions
* Modular codebase (`utils/` and `app/`)
* Jupyter Notebook EDA & training support

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 🧱 Key Components:

* **RNN Model** using Keras/TensorFlow
* **Tweepy API integration** for Twitter data
* **Text preprocessing pipeline**
* **Tokenization + Padding**
* **Model evaluation (accuracy & F1)**
* **Streamlit UI for real-time interaction**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With:

<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/jupyter/jupyter-original-wordmark.svg" title="Jupyter" alt="Jupyter" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/numpy/numpy-original.svg" title="NumPy" alt="NumPy" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/pandas/pandas-original.svg" title="Pandas" alt="Pandas" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/matplotlib/matplotlib-original.svg" title="matplotlib" alt="matplotlib" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/scikitlearn/scikitlearn-original.svg" title="Scikitlearn" alt="Scikitlearn" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/keras/keras-original.svg" title="Keras" alt="Kera" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/tensorflow/tensorflow-original-wordmark.svg" title="tensorflow" alt="tensorflow" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original.svg" title="Git" alt="Git" width="40" height="40"/>&nbsp;

<p align="right">(<a href="#readme-top">back to top</a>)</p>


---

<!-- GETTING STARTED -->
## Getting Started

This is a guide to setup the project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites:

### 🔁 Fork This Project

If you want to make changes or run this project under your own GitHub account:

1. **Fork the repository** to your GitHub profile using the `Fork` button at the top right of [this repo](https://github.com/douglasjnr/sentiment-analysis).
2. **Clone your forked repository**:

### Installation:

1. Clone the repository
   ```sh
   git clone https://github.com/your-username/Sentiment-Analysis.git
   cd Sentiment-Analysis
   ```
2. (Optional but recommended) Create a virtual environment

   For Mac:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
   For Windows:
   ```sh
   python3 -m venv venv
   source venv\Scripts\activate
   ```
4. Install the required packages 
   ```sh
   pip install -r requirements.txt
   ```
5. Set up your Twitter API credentials
   Create a .env file in the root directory
   ```sh
   TWITTER_BEARER_TOKEN=your_bearer_token_here
   ```
   You can get your bearer token from the Twitter Developer Portal
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>


---


<!-- USAGE EXAMPLES -->
## Usage

### :test_tube: Run the Streamlit App
```sh
streamlit run app/streamlit_app.py
```
### :notebook: 
From JupyterLab or VSCode/PyCharm:
```sh
jupyter lab
```
Make sure to switch the kernel to you environment if using `venv`
```sh
python -m ipykernel install --user --name=sentiment-env --display-name "Python (sentiment-env)"
```

## Demo Preview
<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- CONTACT -->
## Contact

Douglas Tanyanyiwa - [LinkedIn](https://linkedin.in/douglas-junior-tanyanyiwa) - [junior.dougyt@gmail.com](mailto:junior.dougyt@gmail.com)

Project Link: [https://github.com/douglasjnr/sentiment-analysis](https://github.com/douglasjn/sentiment-analysis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/douglasjnr/sentiment-analysis.svg?style=for-the-badge
[contributors-url]: https://github.com/douglasjnr/sentiment-analysis/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/douglasjnr/sentiment-analysis.svg?style=for-the-badge
[forks-url]: https://github.com/douglasjnr/sentiment-analysis/network/members
[stars-shield]: https://img.shields.io/github/stars/douglasjnr/sentiment-analysis.svg?style=for-the-badge
[stars-url]: https://github.com/douglasjnr/sentiment-analysis/stargazers
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/douglas-junior-tanyanyiwa
[Pandas-url]: https://pandas.pydata.org/
[Matplotlib]: https://github.com/devicons/devicon/blob/master/icons/matplotlib/matplotlib-original.svg
[Matplotlib-url]: https://matplotlib.org/
