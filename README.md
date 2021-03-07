<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="images/logo.png" alt="Logo">
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)


<!-- GETTING STARTED -->

### Prerequisites

- Python 3.x
- Music Bee 3

### Installation

- Clone the repo

```sh
git clone https://github.com/davidsongoap/MusicBee-CLI.git
cd MusicBee-CLI
```

- Install the requirements

```sh
pip install -r Requirements.txt
```

- Install the musicbeeipc library

```sh
bee-lib\setup.py install
```

- Copy the included MusicBeeIPC.dll file into your MusicBee Plugins folder. (Usually located at C:\Program Files (x86)\MusicBee\Plugins)

- Restart Music Bee

- Finally run the bee script

```py
python bee.py
```

<!-- FEATURES -->


## Features

- Play a Song - `ps <song name>`
- Choose a Playlist - `pl`
- Set Volume - `sv <value>`
- Show Current Song - `cs`
- Skip Forward (use negative number to go backwards) - `skip <seconds>`
- Show the Song Lyrics - `lrc`
- Clear the Screen - `cls`
- Play Your Library - `lib`

<!-- CONTRIBUTING -->

## Contributing

Contributions to MusicBeeCLI are greatly appreciated!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact

Davidson Gonçalves - davisongoap@gmail.com

Project Link: https://github.com/davidsongoap/MusicBee-CLI

