[![CI](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml)

## Jiechen_Li_Mini_3_Polars

The purpose of this repo is to generate the descriptive statistics on datasets using Polars to read `` spotify_2023.csv ``. 

The ``spotify_2023.csv `` is from: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/code 


This dataset contains a comprehensive list of the most famous songs of 2023 as listed on Spotify. The dataset offers a wealth of features beyond what is typically available in similar datasets. It provides insights into each song's attributes, popularity, and presence on various music platforms. The dataset includes information such as track name, artist(s) name, release date, Spotify playlists and charts, streaming statistics, Apple Music presence, Deezer presence, Shazam charts, and various audio features.

<img decoding="async" src="https://i.insider.com/61aaa842983f360019c86a94?width=1000&format=jpeg&auto=webp-logo.png" width="50%">


### Files 

- ``.devcontainer`` configures the local development container environment
- ``github/workflows/ci.yml`` triggers CI/CD on git push and pull request
- ``.gitignore`` specifies which files or directories should be excluded from version control when using Git
- ``Makefile`` build commands and utilities
- ``README.md`` instruction file for the readers
- ``requirements.txt`` specifies the dependencies (libraries and packages) required to run the project


### CI/CD

On git push/pull request the CI/CD flow is triggered using Github Actions:

1. Install and validate Rust toolchain
2. Format and lint code
3. Run unit tests
4. Build binary release
5. Lint Dockerfile
6. Build distroless rusty-ds image
7. Push image to [Github Container Registry](https://github.com/athletedecoded?tab=packages)

### Preparation
1. Open codespaces 
2. Wait for the container to be built with requiremnts.txt installed

### Generate the Descriptive Statistics 

![img](./mean_std.png)

### Visualizations
Visualization of bar graph on Top 10 Songs can be run by using python `test_main.py` 

![img](./Top_10_Songs.png)

### Summary Report
Please check ``Summary_Report.ipynb`` for details
