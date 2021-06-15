# mopc - My Own Private Cloud
## Are you concerned with who has rights over your personal data ? Well you should be.
All the personal data that one posts onto the web constitutes one's digital self. In the physical world, unless you are a public figure, personal data are deemed private and as belonging to you. In the digital world, not so much. For instance, it may depend on where they are actually stored (the bridge with the physical world is the storage and communication hardware that belong to corporations or other individuals). If others than yourself have right over your personal data, they might use them not in your best interests.
## Why this project ?
I want to help address this issue by creating a platform hosting your personal data that would totally be under your control, while keeping all the nice features that new technologies have brought to us (mainly the ability to share things), in a secured and userfriendly environment (that's the trickiest part).  
## What is cloud computing ?
According to NIST,
>Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources–e.g., networks, servers, storage, applications, and services–that can be rapidly provisioned and released with minimal management effort or service provider interaction.
>
If you find this definition intimidating, just retain that a cloud is a space that hosts data and applications (e.g. your photos and an application managing them into albums and allowing selected people to access these albums).
On top of this general definition, note that clouds may be owned by corporations or other individuals. But most interstingly, they can be privately-owned, meaning owned by yourself, even though they might actually be hosted on an equipment that is not yours (this is called a _virtual private cloud_).
## How is this project structured ? What does (or will) it really look like ?
1. The administration<br>
    * Main Home Page:
![Main Home Page](/mopc/main/static/img/Screenshot_main_homepage.png "Main Home Page")
1. The applications<br>
    * Contact List:
![Contact List](/mopc/main/static/img/Screenshot_contact_list.png "Contact List")
    * Photo Album:
![Photo Album](/mopc/main/static/img/Screenshot_gallery.png "Photo Album")   

## TASKS LIST
- [x] Fill README.md page (project brief) - Day51
- [x] Issue a prototype of the project home page - Day52
- [x] Lists functionalities and applications to add to project - Day51
- [ ] Priorize above list, define scope to fit a two weeks window, plan - Day51
- [ ] Select technical platform(s) - Day51
- [ ] Set up Django social authentication - Day52
- [ ] Set up Django multi-tenancy - Day55
- [x] Set up address book app - Day52
- [ ] Set up notes app - Day54
- [ ] Set up blog app - Day54
- [ ] Set up photo album app - Day 53
- [ ] Set up file storage and sharing service - Day55
- [ ] Set up genealogy app
- [ ] Set up news aggregator app
- [ ] Set up professional section (CV, portfolio) - Day56-57
- [ ] Set up game section (asteroids interactive game) - Day58-59
- [ ] Set up server (owned or virtual) - Day58-59

## Modules, packages and other resources used in this project
* Login with social network id: https://python-social-auth.readthedocs.io/en/latest/index.html
* Address Book: https://github.com/tomitokko/contacts-list
* iCalendar abd vCard files: https://eventable.github.io/vobject/
* bootstrap5
* https://fontawesome.com/
* Photo gallery: https://github.com/richardbarran/django-photologue

## Subjects to further explore
* Set up server to run interactive Python apps
* Django social networks authentication (-> https://github.com/pennersr/django-allauth)
    * (see also: https://djangopackages.org/grids/g/facebook-authentication/)
* Multi-tenancy in Django (-> https://github.com/django-tenants/django-tenants)
    * (see also: https://djangopackages.org/grids/g/multi-tenancy/)
