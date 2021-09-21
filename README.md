```
  __                 _       _
 / _| ___   ___   __| |   __| | ___   ___  _ __
| |_ / _ \ / _ \ / _` |  / _` |/ _ \ / _ \| '__|
|  _| (_) | (_) | (_| | | (_| | (_) | (_) | |
|_|  \___/ \___/ \__,_|  \__,_|\___/ \___/|_|

```

## Food Door :wave:

_**Food Door**_ is a Web application where you can order food online, you can sign up as a user to order the food you like or you can sign up as a restaurant to publish your different types of food so clients can order them.

## Technically speaking :wrench:

_**Food Door**_ build in two separate environment:

- Backend environment build by `Python/Django` framework. we decide to move on with `django` because it's flexible
  and easy to use.
  abstraction and pre-pared library. We build our backend based on Models which was our link between the controller (or the api provider)
  each API request protected by the JWT encoding.
- Frontend environment build by `VueJS` and it was a great opportunity to learn Vue and to use it to build something usefull.

## You like to test it :nut_and_bolt:

If you want to test our web application you need to make few steps before you get it run and if you encounter any problem don't be shy
you find us here all the time for help. just ask.
First you need to get this repository on your local machine, sorry the only way to get a look on it is by run it locally.

```bach
git clone https://github.com/IhebChatti/food_door.git ~/
```

Then let's handle the backend dependencies by installing python3.

```bash
sudo apt-get install python3-dev
```

now let's install Django and the needed dependencies

````bash
sudo python -m pip install Django
sudo pip install django-cors-headers
sudo pip install djangorestframework
sudo pip install djangorestframework-simplejwt
```

For the front-end packages:

```bash
yarn install
````

Now we hope that everything goes ok with you, and all is ready to run the web application, in two separate terminal run

```
yarn dev
```

which run the frontend environment on port 3000.
In the second window run

```bash
python3 manage.py runserver
```

Which run the backend environment on port 8000
To get the same landing on page in this repository put `localhost:3000` on your browser
