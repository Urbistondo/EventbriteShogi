# EventbriteShogi
Command-line Shogi game

[![MIT License][license-shield]][license-url]

## Table of Contents

* [About the project](#about-the-project)
  * [Built with](#built-with)
* [Getting started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)

## About the project

This project is an implementation of a Shogi (Japanese chess) game aimed at showcasing object-oriented design and object-oriented programming principles.

As it stands, it provides a client to play the game through a command-line interface, but it's easily adaptable to other interfaces in the future. The implemented features include:
- Piece movement, including capturing opposing pieces, but without piece promotion abilities
- Dropping of captured pieces

The code has been structured to follow a rough hexagonal architecture, separating Domain, Application (use cases) and Infrastructure (interface) concerns. It also includes unit tests for Domain classes.

### Built With
* [Python 3.8.2](https://www.python.org/)

## Getting Started

### Prerequisites

You must have [Python 3.*](https://www.python.org/downloads/) installed.

### Installation

1. Clone the repo
```sh
git clone https://github.com/Urbistondo/Shogi.git
```

## Usage

To run the game, navigate to src/ and run the Main.py file
```sh
cd src
python Main.py
```

To move a piece, you must provide the coordinates to choose a piece the same color as the color of the current player, and the coordinates of the square to which you wish to move the piece, with the following format:
```sh
From (row col):
20
To (row col):
30
```

This will move the piece at row 2 and column 0 to the square at row 3 and column 0.

Captured pieces appear above the board for the white player and below it for the black one, and is refered to as line 9. To drop a captured piece on the board, select it like so:
```sh
From (row col):
91
To (row col):
44
```

Assuming you have captured pieces, this command will drop the second captured piece in square at row 4 and column 4 as long as said square is empty.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Javier Urbistondo - [@JaviUrbistondo](https://twitter.com/JaviUrbistondo)

Project Link: [https://github.com/Urbistondo/Shogi](https://github.com/Urbistondo/Shogi)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
