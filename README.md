# VKS hub

This is the official repository of vkshub.ddns.net.
The website backend is entirely made using the Python framework Django.
The website front is made using html,css and js with bootstrap.

## Getting Started

To make this site up you need to install some libraries which are essential to the website ! 

### Prerequisites

You need to install Pip3 to install these libraries : 
```
pip install filetype
pip install sweetify
pip install psutil
pip install tracking
pip install ipinfo
pip install ffmpeg
pip install vacances_scolaires_france
pip install django_waitress
pip install django_user_agents
pip install Pillow
pip install thispersondoesnotexist
pip install opencv-python
```

## What pages/features are inside it

Pages : 
* [Home](http://vkshub.tretis.fr) - page that include a dynamic graph and a counter of days before holidays (using the library vacances_scolaires_france)
* [Projects](http://vkshub.tretis.fr/projects) - page that includes a foldable list of projects that I made or I am involved in...
* [Cloud](http://vkshub.tretis.fr/cloud) - a personal cloud with detection of the type of files (using the library file type and if statement). 
* [Cloud-Upload](http://vkshub.tretis.fr/upload) - A webpage to upload file to the cloud. Safe and easy to debug using the Django csrf token and form)
* [URL shortener](http://vkshub.tretis.fr/short) - A simple URL shortener using database and models in Django.
* [Vekflix](http://vkshub.tretis.fr/vekflix) - a netflix parody
* [Youtube Downloader](http://vkshub.tretis.fr/ytb) - (Fix soon?) a tool to download youtube videos using pytube library
* [Steganography](http://vkshub.tretis.fr/steganography) - a tool to hide text inside a photos using a cryptostegano and a personal script that I keep private
* [Face Recognition](http://vkshub.tretis.fr/face_recognition) - a tool to find faces in a png/jpg using cv2 and haarscade library
* [Face Generation](http://vkshub.tretis.fr/thispersondoesnotexist) - a tool to generate faces of person that doesn't exist (based on thispersondoesnotexist library)
* [Algorithm of math training optimisation](http://vkshub.tretis.fr/bac_maths) - a tool to help people train maths in a limited time or in some domains 
* [Robert Bus](http://vkshub.tretis.fr/bus) - a tool to get a bus schedule using an API
* [Robert 2.0](http://vkshub.tretis.fr/robert) - a random sentences generator using js




### Template

Most of the pages are created based on this template (free with personal use):
[Dashio](https://templatemag.com/dashio-bootstrap-admin-template/)

## Test it !

You can test the website in this URL : [VKSHUB](http://vkshub.tretis.fr/)

## Built mostly With

* [Django](https://www.djangoproject.com/) - Django makes it easier to build better Web apps more quickly and with less code.
* [Bootstrap](https://getbootstrap.com/) - Build responsive, mobile-first projects on the web with the world’s most popular front-end component library. 

## Authors

* **Emile Delmas** - *Students* - [emiledelmas](https://github.com/emiledelmas)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

