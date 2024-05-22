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
Initial design concepts were visualized through wireframes, which provided a schematic representation of the user interface and experience. These wireframes served as a foundational blueprint for the development team and were refined over multiple iterations based on stakeholder feedback. [Link to wireframes]

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
Each blog post can be accessed in full detail, displaying all content, including multimedia elements like images and videos. Users can interact with posts through likes and comments. Posts with geographical tags show an embedded map view that pinpoints the location discussed.

#### User Authentication
The site supports comprehensive user authentication mechanisms. Users can sign up, log in, and log out. Authentication is managed through Django's built-in user management system, ensuring security and data integrity.

#### Commenting System
A fully integrated commenting system allows registered users to post comments on articles. Comments can be moderated by administrators to maintain quality and relevance.

#### Like Feature
Users can express appreciation for content through a like system, which is tallied and displayed on each post. This system enhances user engagement and provides feedback to content creators.

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
- `number_of_likes()`: Returns the count of likes for each post, allowing for dynamic display in templates.
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
PostgreSQL is used as the primary database, offering advanced features and reliability for storing complex relational data.

## Testing
### Test Guide
Instructions on running automated tests to ensure application stability and performance. Tests cover model validation, view functionality, and user interaction flows.

### Validator Testing
HTML and CSS code passes W3C validation without errors, ensuring standards compliance and browser compatibility.

### Browser Compatibility Testing
The site is tested across modern browsers including Google Chrome, Mozilla Firefox, and Safari, with adjustments made to ensure consistent behavior and appearance.

### List of Fixed Bugs
- **Map Loading Issue:** Fixed a bug where the map would not load correctly on initial page visits by ensuring asynchronous loading and proper initialization in JavaScript.

### List of Unfixed Bugs
- **Delayed Comment Display:** Occasionally, comments may not appear immediately due to caching issues. Work is ongoing to address this in future updates.

## Deployment
### Development Environment Setup
Detailed steps to set up a local development environment, including cloning the GitHub repository, setting up a virtual environment, installing dependencies, and running the Django development server.

### Deployment to Production
Comprehensive instructions for deploying the application to Heroku, including setting environment variables, configuring Django settings for production, and using Heroku's Git-based deployment workflow.

## Source Credits
### References/Documentation/Tutorials
A list of key resources, documentation, and tutorials that provided guidance and code snippets during the development process.

### Media and Styling Credits
Credits for images, icons, and other media used in the project, sourced from various free and paid resources.
