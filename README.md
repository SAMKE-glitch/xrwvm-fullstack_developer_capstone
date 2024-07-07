# **Best Cars Dealership Application**
## Table of Contents
* [Introduction](#introduction)
* [Architectural Overview](#architectural-overview)
    * [Detailed Services](#detailed-services)
* [Technologies](#technologies)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


## **Introduction**
A national car dealership with local branches spread across the United States recently conducted a market survey. One of the suggestions that emerged from the survey was that customers would find it beneficial if they could access a central database of dealership reviews across the country.

You are a new hire at the company. You are assigned the task of building a website that allows new and existing customers to look up different branches by state and look at customer reviews of the various branches. Customers should be able to create an account and add their review for any of the branches. The management hopes this will bring transparency to the system and also increase the trust customers have in the dealership.

After thorough research and brainstorming, the team developed use cases for anonymous, authorized, and admin users.

### Use cases for authorized users:
In addition to the above, authorized users should be able to write a review for any dealership on the dealership's page. In order to enable authorized users to write their reviews:

- A Review button should be provided against each dealer listed in the dealership table.
- Clicking on the Review button should take the user to the review page.
- Filling the form on the review page and submitting it should add the review. The review details include:

    ```json
    {
        "user_id": 1,               // from Django
        "name": "Berkly Shepley",   // from Django
        "dealership": 15,           // from the form
        "review": "Total grid-enabled service-desk", // form textbox
        "time": "",                 // current time
        "purchase": true,           // form checkbox
        "purchase_date": "07/11/2020", // form calendar (bootstrap)
        "car_make": "Audi",         // from django dropdown
        "car_model": "A6",          // from django dropdown
        "car_year": 2010            // from django dropdown
    }
    ```

On submission, the user should be taken back to the dealership detail page with the submitted review featured at the top of the reviews list, sorted on time.

### Use cases for admin users:
- Log in to the admin site with a predefined username and password.
- Add new make, model, and other attributes.

Your organization has assigned you as the Lead Full-Stack Software Developer on this project. Your job is to develop this portal as part of your Capstone project by following best practices for Full-Stack software development.

## **Architectural Overview**

1. **Django Application:**
    - Add user management using the Django user authentication system.
    - Create Django models and views to manage car model and car make.
    - Create Django proxy services and views to integrate dealers and reviews together.

2. **React Frontend:**
    - Implement user management using the Django user authentication system.
    - Create a React frontend for the application.

3. **Backend Services:**
    - Create a Node.js server to manage dealers and reviews using MongoDB.
    - Dockerize the Node.js server.
    - Deploy the sentiment analyzer on Code Engine.

4. **Sentiment Analyzer:**
    - Deploy and integrate the sentiment analyzer as a backend service.

![Architecture Diagram](/images/architectDesign.png)
### **Detailed Services**

The user interacts with the "Dealerships Website", a Django website, through a web browser.

#### Django Application
The Django application provides the following microservices for the end user:

- `get_cars/` - To get the list of cars.
- `get_dealers/` - To get the list of dealers.
- `get_dealers/:state` - To get dealers by state.
- `dealer/:id` - To get dealer by id.
- `review/dealer/:id` - To get reviews specific to a dealer.
- `add_review/` - To post review about a dealer.

The Django application uses an SQLite database to store the Car Make and the Car Model data.

#### Dealerships and Reviews Service
The "Dealerships and Reviews Service" is an Express Mongo service running in a Docker container. It provides the following services:

- `/fetchDealers` - To fetch the dealers.
- `/fetchDealer/:id` - To fetch the dealer by id.
- `/fetchReviews` - To fetch all the reviews.
- `/fetchReview/dealer/:id` - To fetch reviews for a dealer by id.
- `/insertReview` - To insert a review.

"Dealerships Website" interacts with the "Dealership and Reviews Service" through the "Django Proxy Service" contained within the Django Application.

#### Sentiment Analyzer Service
The "Sentiment Analyzer Service" is deployed on IBM Cloud Code Engine and provides the following service:

- `/analyze/:text` - To analyze the sentiment of the text passed. It returns positive, negative, or neutral.

The "Dealerships Website" consumes the "Sentiment Analyzer Service" to analyze the sentiments of the reviews through the Django Proxy contained within the Django application.
## **Technologies**

- **Frontend:**
    - React
    - Bootstrap (for form and UI components)

- **Backend:**
    - Django
    - Node.js
    - MongoDB

- **Services:**
    - Docker (for containerization)
    - Code Engine (for deploying the sentiment analyzer)

- **Other:**
    - Python (for the Django application)
    - JavaScript (for the Node.js server and React frontend)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/SAMKE-glitch/xrwvm-fullstack_developer_capstone
cd xrwvm-fullstack_developer_capstone/server
```

### 2. Set up virtual environment for your Django application to run
```bash
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
```

### 3. Install necessary Python packages in your virtual environment
```bash
python3 -m pip install -U -r requirements.txt
```

### 4. Perform migrations to create necessary tables
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 5. Start the local development server
```bash
python3 manage.py runserver
```

![Homepage](/images/landingPAGE.png)

## Node.js Mongo DB Dockerized Server

### 1. Open a new terminal, Change to the directory with the data files.
```bash
cd /xrwvm-fullstack_developer_capstone/server/database
```

### 2. Run the following command to build the Docker app.
```bash
docker build . -t nodeapp
```

### 3. The docker-compose.yml has been created to run two containers, one for Mongo and the other for the Node app. Run the following command to run the server:
```bash
docker-compose up
```
