
***This Repo is obsolete.***
***To send MercedesME information to Victron, utilize the HA integration "https://github.com/ReneNulschDE/mbapi2020", MQTT and NodeRed in Venus Large OS.***



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<h3 align="center">hame_victron-bridge</h3>

  <p align="center">
    Display your MercedesME data on VenusOS
    <br />
    <a href="https://github.com/CzarofAK/hame_victron-bridge"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/CzarofAK/hame_victron-bridge/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/CzarofAK/hame_victron-bridge/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

I own a campervan with a built in Victron Energy system, including a Touch Display for the Venus OS. In the future I plan to replace my Truma Combi 4 with a Truma Combi D 6 E. As I would like to stay remote for several days in a row, i would like to have the Diesel Level of my Mercedes Sprinter VS30 (W910 but this also applies to the W907) directly on my Venus OS Touch Display.

<!-- GETTING STARTED -->
## Getting Started

You can feed more data to your Victron than i do. But for Adblue and Diesel, just follow this guide.

* It works with Venus GUIv2!
* THIS REPLACES THE HOMEASSISTANT MQTT BROKER WITH THE VENUS OS!
  * If you have many MQTT devices, it could eventually cause performance issues on the VENUS OS

### Prerequisites

This setup requires the following things.

- **Car**
  - Mercedes ME compatible car
  - Mercedes ME account
- **Home Assistant**
  - HomeAssistant instance
  - HACS
  - https://github.com/ReneNulschDE/mbapi2020
  - FileEditor or VSC addon
  - Mosquitto broker addon (MQTT Broker)
- **Victron**
  - Cerbo or RPi with VenusOS
  - https://github.com/freakent/dbus-mqtt-devices
  - MQTT Enabled

### Installation

1. **Venus OS (v3.50+)**
   1. install https://github.com/freakent/dbus-mqtt-devices
   2. enable MQTT (Settings -> services -> MQTT Access)
2. **Home Assistant**
   1. install HACS
   2. install https://github.com/ReneNulschDE/mbapi2020
   3. install and setup Mosquitto broker addon (to be checked if even requried)
   4. setup MQTT integration
      1. Broker: venus.local or IP of VenusOS
      2. Port: 1883
      3. Username: *empty*
      4. Password: *empty*
   5. edit script.py
      1. check "mqtt_host" and "mqtt_port"
      2. replace all "tbd" with actual sensor
         1. change "sensor.tbd_fuel_level" to actual MercedesME sensor name
         2. change "sensor.tbd_adblue_level" to actual MercedesME sensor name

Success, that was all required to get your data transmitted from your Mercedes to any Victron Venus installation!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/CzarofAK/hame_victron-bridge/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=CzarofAK/hame_victron-bridge" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Project Link: [https://github.com/CzarofAK/hame_victron-bridge](https://github.com/CzarofAK/hame_victron-bridge)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Home Assistant - Mercedes ME integration](https://github.com/ReneNulschDE/mbapi2020)
* [MQTT VenusOS - bridge](https://github.com/freakent/dbus-mqtt-devices)
* [Readme Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/CzarofAK/hame_victron-bridge.svg?style=for-the-badge
[contributors-url]: https://github.com/CzarofAK/hame_victron-bridge/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CzarofAK/hame_victron-bridge.svg?style=for-the-badge
[forks-url]: https://github.com/CzarofAK/hame_victron-bridge/network/members
[stars-shield]: https://img.shields.io/github/stars/CzarofAK/hame_victron-bridge.svg?style=for-the-badge
[stars-url]: https://github.com/CzarofAK/hame_victron-bridge/stargazers
[issues-shield]: https://img.shields.io/github/issues/CzarofAK/hame_victron-bridge.svg?style=for-the-badge
[issues-url]: https://github.com/CzarofAK/hame_victron-bridge/issues
[license-shield]: https://img.shields.io/github/license/CzarofAK/hame_victron-bridge.svg?style=for-the-badge
[license-url]: https://github.com/CzarofAK/hame_victron-bridge/blob/master/LICENSE.txt
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
