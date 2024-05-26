# Urbex Hidden Treasure Documentation

## Table of Contents
1. [Introduction](#introduction)
   - [Site Overview](#site-overview)
   - [Purpose and Scope](#purpose-and-scope)
2. [UI/UX Design](#uiux-design)
   - [Agile Development Approach](#agile-development-approach)
   - [Wireframes](#wireframes)
   - [Site Goals](#site-goals)
   - [Five Planes of UX](#five-planes-of-ux)
   - [Visual Design Choices](#visual-design-choices)
3. [Features](#features)
   - [Existing Features](#existing-features)
     - [Blog Post Listing](#blog-post-listing)
     - [Detailed Blog View](#detailed-blog-view)
     - [User Authentication](#user-authentication)
     - [User-Generated Content](#user-generated-content)
     - [Commenting System](#commenting-system)
     - [Map View Integration](#map-view-integration)
   - [Future Features](#future-features)
4. [Database Design](#database-design)
   - [Database Model Description](#database-model-description)
   - [Custom Model Features](#custom-model-features)
   - [CRUD Operations](#crud-operations)
5. [Technologies Used](#technologies-used)
   - [Work Environments and Hosting](#work-environments-and-hosting)
   - [Python Libraries](#python-libraries)
   - [Django Libraries](#django-libraries)
   - [External Libraries](#external-libraries)
   - [Database Technologies](#database-technologies)
6. [Testing](#testing)
   - [Test Guide](#test-guide)
   - [Validator Testing](#validator-testing)
   - [Browser Compatibility Testing](#browser-compatibility-testing)
   - [List of Fixed Bugs](#list-of-fixed-bugs)
   - [List of Unfixed Bugs](#list-of-unfixed-bugs)
   - [Manual Testing](#manual-testing)
7. [Deployment](#deployment)
   - [Development Environment Setup](#development-environment-setup)
   - [Deployment to Production](#deployment-to-production)
8. [Getting Started](#getting-started)
   - [Create a Django Project](#create-a-django-project)
   - [Create a Blog Application](#create-a-blog-application)
   - [Create a Virtual Environment and Install Django](#create-a-virtual-environment-and-install-django)
   - [Create Database Models](#create-database-models)
   - [Register the Blog Application](#register-the-blog-application)
   - [Run the Project and Migrate the Models](#run-the-project-and-migrate-the-models)
   - [Install Django Extensions](#install-django-extensions)
   - [Setup the Package](#setup-the-package)
   - [Generate the ERD](#generate-the-erd)
9. [Source Credits](#source-credits)
   - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
   - [Media and Styling Credits](#media-and-styling-credits)

## Introduction
### Site Overview
Urbex Hidden Treasure is a comprehensive digital platform designed specifically for urban exploration enthusiasts. It serves as a central hub where adventurers can post detailed accounts of their explorations, share photos, and engage with a community of like-minded individuals. This platform not only catalogs urban explorations but also integrates interactive maps to enhance user experience by visually representing exploration sites.

### Purpose and Scope
This project aims to create a vibrant, interactive community around urban exploration, providing tools and features that allow users to document their adventures, share insights, and discover new locations through the experiences of others. It targets urban explorers, historians, photographers, and anyone intrigued by the hidden facets of urban environments.

## UI/UX Design
### Agile Development Approach
The development of Urbex Hidden Treasure adopted an Agile approach, prioritizing user feedback and iterative updates to ensure the platform evolves in alignment with user needs and expectations. Regular reviews and planning sessions were integral to this process, helping to refine features and functionality continuously.

### Wireframes
Initial design concepts were visualized through wireframes, which provided a schematic representation of the user interface and experience. These wireframes served as a foundational blueprint for the development process and were refined over multiple iterations based on stakeholder feedback. During the development process, some elements were adjusted for practicality and completeness, resulting in a final product that may look different from the initial wireframes.

#### The Landing Page
![landingpage_wireframe](https://github.com/FabiMe/Urbex-The-Hidden-Gem/assets/136444209/862309c6-311a-4961-8510-f710fbde1720)

#### Blog Detail 
![blog_detail_wireframe ](https://github.com/FabiMe/Urbex-The-Hidden-Gem/assets/136444209/c2f8d3bf-808e-4525-9c0c-7937049bbfc5)

#### Blog Overview
![blog_overview_wireframe](https://github.com/FabiMe/Urbex-The-Hidden-Gem/assets/136444209/68ced510-742c-4f82-863a-59271e954c9b)

#### Sign Up Page
![sign_up_wireframe](https://github.com/FabiMe/Urbex-The-Hidden-Gem/assets/136444209/442f3ed7-7753-4369-8173-46f99487b0be)


### Site Goals
The primary objectives of Urbex Hidden Treasure are to:
- Facilitate the sharing of urban exploration content in a structured and engaging manner.
- Foster a community of enthusiasts who can interact, collaborate, and share their passion for urban exploration.
- Provide educational content about the history and context of various urban locations.

### Five Planes of UX
The design and functionality of Urbex Hidden Treasure are structured around Jesse James Garrett's five planes of user experience. Each plane represents a different aspect of the user experience, from the abstract strategy to the concrete surface.

- **Strategy Plane:** 
  - **User Needs:** Identifying the primary users as urban exploration enthusiasts who need a platform to share their discoveries, interact with other explorers, and find new places to explore.
  - **Business Objectives:** Objectives include creating a vibrant community, increasing user engagement through interactive features, and providing a comprehensive resource for urban exploration.

- **Scope Plane:**
  - **Functional Requirements:** Includes technical functionalities such as user authentication, blog post creation, commenting system, profile management, and map view integration.
  - **Content Requirements:** Involves the types of content the site will host, such as blog posts, comments, user profiles, and interactive maps.

- **Structure Plane:**
  - **Interaction Design:** Defines how users interact with the site, such as the flow of creating a new blog post, commenting on posts, navigating through the site, and viewing maps.
  - **Information Architecture:** Involves organizing and structuring the content logically, such as categorizing blog posts, managing user profiles, and structuring the homepage to highlight recent posts.

- **Skeleton Plane:**
  - **Interface Design:** Focused on the layout and arrangement of elements on each page, ensuring that the interface is intuitive and user-friendly. This includes placement of buttons, forms, and navigation menus.
  - **Navigation Design:** Creating a seamless navigation system that allows users to move through the site effortlessly. This includes the main navigation bar, sidebar menus, and internal linking within posts.
  - **Information Design:** Ensuring that information is presented clearly and effectively, with a focus on readability and accessibility.

- **Surface Plane:**
  - **Visual Design:** Deals with the final visual elements of the site, including the color scheme, typography, imagery, and overall aesthetic. The goal is to create a visually appealing design that supports the user experience.
  - **Brand Identity:** Consistency in visual elements to reinforce the brand identity of Urbex Hidden Treasure. This includes the use of specific fonts (like Bebas Neue for headings and Roboto for body text), a dark theme with high contrast for readability, and imagery that resonates with urban exploration.

### Visual Design Choices
The platform utilizes a sleek, modern design with a minimalist color palette to reduce visual clutter and focus on content readability. Typography choices such as Bebas Neue for headings and Roboto for body text combine readability with character, supporting the overall urban and modern theme. The interface is designed to be intuitive, with responsive design considerations ensuring usability across various devices and screen sizes.

## Features
### Existing Features
#### Blog Post Listing
Provides a dynamically updated list of blog posts, prominently displayed on the homepage. Each post includes a teaser excerpt, a visually striking featured image, and a link to the full article. Posts are sorted by their publication date, with the most recent posts appearing first.
![blog_detail](https://github.com/FabiMe/Urbex-Hidden-Treasure/assets/136444209/d5752bcc-da4e-4396-b580-9558d46f26f2)

#### Detailed Blog View
Each blog post can be accessed in full detail, displaying all content, including multimedia elements like images and videos. Users can interact with posts through comments. Posts with geographical tags show an embedded map view that pinpoints the location discussed.

![blog_detail_1](https://github.com/FabiMe/Urbex-The-Hidden-Gem/assets/136444209/a224f396-8b83-45a9-acf2-2057d9ef4831)

![blog_detail_2](https://github.com/FabiMe/Urbex-The-Hidden-Gem/assets/136444209/9e0f9916-1794-42b5-b38f-aa41f6fe1a7d)

#### User Authentication
The site supports comprehensive user authentication mechanisms. Users can sign up, log in, and log out. Authentication is managed through Django Allauth, ensuring security and data integrity.
##### Sign In
![sign_in](https://github.com/FabiMe/Urbex-The-Hidden-Gem/assets/136444209/4bea6f73-218b-4c35-a050-1b0ca33e6b88)

##### Sign Up
![sign_up](https://github.com/FabiMe/Urbex-The-Hidden-Gem/assets/136444209/f44d40e7-4a6e-41df-8b05-77668586e12f)

#### User-Generated Content
All registered users have the ability to create new blog posts, sharing their own urban exploration stories and experiences with the community. This feature encourages active participation and content generation from users.

##### Create New Post Button
![create_new_post](https://github.com/FabiMe/Urbex-The-Hidden-Gem/assets/136444209/0a6c7ddc-3578-47cc-a88b-ca65044169b1)

##### Create New Blog Post 
![create_new_post_2](https://github.com/FabiMe/Urbex-The-Hidden-Gem/assets/136444209/10f7ad5a-516c-4b9f-93f5-cb5ad39be92a)

#### Commenting System
A fully integrated commenting system allows registered users to post comments on articles. Comments can be moderated by administrators to maintain quality and relevance. Comments must be approved by an admin before they are displayed on the page.
![comments](https://github.com/FabiMe/boutique_ado_v1/assets/136444209/86357f98-640d-4b5e-9b97-724955b5fd4a)
![comments_signed_in](https://github.com/FabiMe/boutique_ado_v1/assets/136444209/9d3d543e-a525-4de9-b0e2-c85b81998468)

#### Map View Integration
Interactive maps are integrated into the platform using Leaflet.js, which allows users to visually explore the locations related to each post. Each blog post includes an embedded map view showing the location discussed. Additionally, there is a dedicated map navigation point that provides an overview of all locations mentioned in the blog posts. This feature enriches the storytelling aspect by providing geographical context and allowing users to explore multiple locations through a single interface.
##### Blog Post Map
![pripyat](https://github.com/FabiMe/Fit-Hub/assets/136444209/5ccec439-467a-4e8f-8692-97301873fc18)

##### Map Overview
![map overview](https://github.com/FabiMe/Fit-Hub/assets/136444209/c11d0d74-981e-4887-9d12-a35e27ed4089)

### Future Features
Planned enhancements include:
- Real-time social media integration to allow users to share posts directly to their social media accounts.
- Advanced search functionality with filters for location, date, and popularity to help users find specific content more easily.

## Database Design
### Database Model Description
The project uses several Django models to manage its data:
- **Post:** Stores all information about blog entries, including title, content, and meta-data like author and timestamps.
- **User:** Utilizes Django’s built-in User model for authentication and user management.
- **Comment:** Linked to blog posts for user interactions.
- **Category:** Allows posts to be categorized to help organize content and aid in navigation.
- **Article:** Used for longer form content that is separate from regular blog posts.

### Database Model
![urbex_models (1)](https://github.com/FabiMe/boutique_ado_v1/assets/136444209/65de82d8-d7ee-4d59-8ce2-8d29017b794f)

- To create an automatically generated ERD Model the following steps are crucial:

- Uses Django's ORM with PostgreSQL. Models include:

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/722508d2-8890-47cf-91c3-ca3d77275d05)

- This will create the bellow files and directories.

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/1f2af177-121c-45f0-93da-7ca0dacf2b32)

- Create a blog application

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/e4a67d91-5ef6-4cbd-b449-4a478b81a0bf)

- Install Django

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/6822922e-6758-40b7-a0c3-de2383178b84)

- In blog/models.py 

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/9eced74b-9261-4679-a4c5-6da9f4775541)

- In mysite/settings.py

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/1d81af87-8c66-4e4d-a954-0f7e83e071db)

- Run the project and migrate the models

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/b61c960f-f4e6-49dd-ad18-d445d32b06e4)

- Install django-extensions 

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/28514a57-5779-4805-85df-042cbdd95753)

- Setup the package

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/c575987d-5557-4187-ba43-c6a8c64a3920)

- Generate ERD Model

![image](https://github.com/FabiMe/Fitness-Forge/assets/136444209/fefc1cc8-80c8-4355-bb55-a4050780b991)

### Custom Model Features
Custom model methods include:
- Auto-generated slugs for posts: Ensures URLs are readable and SEO-friendly.

### CRUD Operations
The application supports full CRUD (Create, Read, Update, Delete) capabilities for blog posts and comments, providing a dynamic and interactive user experience.

## Technologies Used
### Work Environments and Hosting
The application is developed using Django and Python. The live application is hosted on Heroku, which provides a robust platform for app deployment and scaling.

### Python Libraries
Key Python libraries used include:
- **Django:** The core framework providing the structure and tools for web application development.
- **Pillow:** Used for image processing capabilities within Django.
- **Gunicorn:** Serves as the HTTP server for Django applications on Heroku.

### Django Libraries
Django’s rich ecosystem is leveraged to extend the functionality of Urbex Hidden Treasure, including:
- **Django Forms:** Simplifies the creation and handling of HTML forms.
- **Django Admin:** Provides a ready-to-use interface for site administration.

### External Libraries
External libraries enhance functionality and user experience:
- **Leaflet.js:** For interactive maps that do not require complex GIS capabilities.
- **Bootstrap:** Used for responsive design and modern UI components.

### Database Technologies
Cloudinary is used as the primary database, offering advanced features and reliability for storing complex relational data.

## Testing

Code is validated using tools like Flake8 and Pylint to ensure adherence to coding standards.

### Browser Compatibility Testing

The application is tested across multiple browsers, including Chrome, Firefox, and Safari, to ensure compatibility.

### List of Fixed Bugs

- Fixed issue with map markers not displaying correctly on certain browsers.
- Resolved a bug where users couldn't delete their comments.

### List of Unfixed Bugs

- Occasional slow loading times on the map view due to large datasets.

### Manual Testing

The following table lists the features that require manual testing, along with the test cases and expected outcomes:

| Feature                | Test Case                                               | Expected Outcome                                               |
|------------------------|---------------------------------------------------------|----------------------------------------------------------------|
| Blog Post Listing      | Navigate to the blog overview page                      | List of blog posts displayed with title, excerpt, author, date |
| Detailed Blog View     | Click on a blog post title                              | Detailed view of the blog post with full content and comments   |
| User Authentication    | Sign up with a new email                                | Account created and user logged in                             |
|                        | Log in with existing credentials                        | User logged in successfully                                    |
|                        | Log out                                                 | User logged out and redirected to home page                    |
| User-Generated Content | Create a new blog post                                  | New post is created and displayed in the blog overview         |
|                        | Edit an existing blog post                              | Updated post content displayed correctly                       |
|                        | Delete an existing blog post                            | Post is removed from the blog overview                         |
| Commenting System      | Post a comment on a blog post                           | Comment appears below the post                                 |
|                        | Edit an existing comment                                | Edited comment updated below the post                          |
|                        | Delete a comment                                        | Comment removed from the post                                  |
| Profile Management     | Update profile information                              | Profile information updated and displayed correctly            |
| Map View Integration   | View the map on the blog post detail page               | Map displays with a marker at the post's location              |
|                        | Click on a marker on the map                            | Popup with post title and link to detailed view                |
|                        | Navigate to the map overview                            | Map displays all post locations with markers                   |
| Responsive Design      | View the site on various screen sizes (mobile, tablet)  | Layout adjusts to fit screen size without breaking             |

### Deployment

#### Development Environment Setup

To set up the development environment, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/username/UrbexHiddenTreasure.git
    ```
2. **Navigate into the directory:**
    ```sh
    cd UrbexHiddenTreasure
    ```
3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
4. **Set up the database:**
    ```sh
    python manage.py migrate
    ```

#### Deployment to Production

The application is deployed to Heroku. Follow these steps to deploy:

1. **Login to Heroku:**
    ```sh
    heroku login
    ```
2. **Create a new Heroku app:**
    ```sh
    heroku create
    ```
3. **Set up environment variables:**
    ```sh
    heroku config:set SECRET_KEY='your_secret_key'
    heroku config:set DATABASE_URL='your_database_url'
    ```
4. **Deploy the application:**
    ```sh
    git push heroku main
    ```

### Source Credits

#### References/Documentation/Tutorials

- Django documentation: https://docs.djangoproject.com/
- Leaflet.js documentation: https://leafletjs.com/
- Bootstrap documentation: https://getbootstrap.com/

#### Media and Styling Credits

- Background images and icons from Cloudinary.
- Fonts from Google Fonts.