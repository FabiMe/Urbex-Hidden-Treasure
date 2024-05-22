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
     - [Commenting System](#commenting-system)
     - [Like Feature](#like-feature)
     - [Profile Management](#profile-management)
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
8. [Source Credits](#source-credits)
   - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
   - [Media and Styling Credits](#media-and-styling-credits)

## Introduction
### Site Overview
Urbex Hidden Treasure is a comprehensive digital platform designed specifically for urban exploration enthusiasts. It serves as a central hub where adventurers can post detailed accounts of their explorations, share photos, and engage with a community of like-minded individuals. This platform not only catalogs urban explorations but also integrates interactive maps to enhance user experience by visually representing exploration sites.

### Purpose and Scope
This project aims to create a vibrant, interactive community around urban exploration, providing tools and features that allow users to document their adventures, share insights, and discover new locations through the experiences of others. It targets urban explorers, historians, photographers, and anyone intrigued by the hidden facets of urban environments.

## UI/UX Design
### Agile Development Approach
The development of Urbex Hidden Treasure adopted an Agile approach, prioritizing user feedback and iterative updates to ensure the platform evolves in alignment with user needs and expectations. Regular sprint reviews and planning sessions were integral to this process, helping to refine features and functionality continuously.

### Wireframes
Initial design concepts were visualized through wireframes, which provided a schematic representation of the user interface and experience. These wireframes served as a foundational blueprint for the development team and were refined over multiple iterations based on stakeholder feedback. During the development process, some elements were adjusted for practicality and completeness, resulting in a final product that may look different from the initial wireframes.

![landingpage_wireframe](https://github.com/FabiMe/Urbex-Hidden-Treasure/assets/136444209/5c45244a-6980-43d2-a671-09657456d5ce)

![sign_up_wireframe](https://github.com/FabiMe/Urbex-Hidden-Treasure/assets/136444209/9c664ff2-bf96-4b6d-84d5-c69297015d82)

![blog_detail_wireframe ](https://github.com/FabiMe/Urbex-Hidden-Treasure/assets/136444209/ec2cffb4-9707-48f3-8b48-af4eb87f5b23)

![blog_overview_wireframe](https://github.com/FabiMe/Urbex-Hidden-Treasure/assets/136444209/84b21cad-874d-4e38-bc14-b110a4e9f87d)


### Site Goals
The primary objectives of Urbex Hidden Treasure are to:
- Facilitate the sharing of urban exploration content in a structured and engaging manner.
- Foster a community of enthusiasts who can interact, collaborate, and share their passion for urban exploration.
- Provide educational content about the history and context of various urban locations.

### Five Planes of UX
The design and functionality of Urbex Hidden Treasure are structured around Jesse James Garrett's five planes of user experience:
- **Strategy Plane:** Focused on understanding user needs and business objectives.
- **Scope Plane:** Defined the functional and content requirements.
- **Structure Plane:** Detailed the interaction design and information architecture.
- **Skeleton Plane:** Developed the interface, navigation, and information design.
- **Surface Plane:** Crafted the visual design elements to create a pleasing aesthetic that enhances usability and user engagement.

### Visual Design Choices
The platform utilizes a sleek, modern design with a minimalist color palette to reduce visual clutter and focus on content readability. Typography choices such as Bebas Neue for headings and Roboto for body text combine readability with character, supporting the overall urban and modern theme. The interface is designed to be intuitive, with responsive design considerations ensuring usability across various devices and screen sizes.

## Features
### Existing Features
#### Blog Post Listing
Provides a dynamically updated list of blog posts, prominently displayed on the homepage. Each post includes a teaser excerpt, a visually striking featured image, and a link to the full article. Posts are sorted by their publication date, with the most recent posts appearing first.

#### Detailed Blog View
Each blog post can be accessed in full detail, displaying all content, including multimedia elements like images. Users can interact with posts through comments. Posts with geographical tags show an embedded map view that pinpoints the location discussed.

#### User Authentication
The site supports comprehensive user authentication mechanisms. Users can sign up, log in, and log out. Authentication is managed through Django Allauth, ensuring security and data integrity.

#### Commenting System
A fully integrated commenting system allows registered users to post comments on articles. Comments can be moderated by administrators to maintain quality and relevance. Comments must be approved by an admin before they are displayed on the page.

#### Profile Management
Users have the ability to view and edit their profiles, enhancing the personalization of the user experience. Profile management also includes the option to delete accounts, ensuring users have control over their data.

#### Map View Integration
Interactive maps are integrated into the platform using Leaflet.js, which allows users to visually explore the locations related to each post. This feature enriches the storytelling aspect by providing geographical context.

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

### Custom Model Features
Custom model methods include:
- Auto-generated slugs for posts: Ensures URLs are readable and SEO-friendly.

### CRUD Operations
The application supports full CRUD (Create, Read, Update, Delete) capabilities for blog posts, user profiles, and comments, providing a dynamic and interactive user experience.

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
### Test Guide
Instructions on running automated tests to ensure application stability and performance. Tests cover model validation, view functionality, and user interaction flows.

### Validator Testing

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
| Commenting System      | Post a comment on a blog post                           | Comment appears below the post                                 |
|                        | Edit an existing comment                                | Edited comment updated below the post                          |
|                        | Delete a comment                                        | Comment removed from the post                                  |
| Profile Management     | Update profile information                              | Profile information updated and displayed correctly            |
| Map View Integration   | View the map on the blog post detail page               | Map displays with a marker at the post's location              |
|                        | Click on a marker on the map                            | Popup with post title and link to detailed view                |
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