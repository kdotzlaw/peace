# [Peace Lutheran Church](https://peacelc.com): A Custom Wordpress Website   

## Documentation
Documentation can be found [here](https://docs.google.com/document/d/15RkCXNSL9OtPKiphF9jgUPiGUlcWiMuyPx_aq3dzQ9E/edit?usp=sharing)

## Website Development   
The goal of this website redesign was to create an elevated user experience for both Church regulars and newcomers, and integrate Church events into the website. The original website had outdated and nested pages information which was hard for many users to navigate and also caused the website to be inefficient on mobile devices. The redesigned website is dynamic and works equally efficiently on any device. 

#### Website Issues & Solutions  

- Wordpress doesn't allow video upload when 128MB limit is exceeded so all Message uploads failed.
  - Solved by uploading Messages to Youtube and embedding links, and using the Wordpress video archive feature to make Messages accessible through the website.
- Embedded media and Youtube videos ignored all Wordpress positioning.
  - Solved by adding custom CSS for embeds. 
- Plugins from different origins had inconsistent CSS (fonts, colors, padding) and have no manual options to change this for all instances.
  - Solved by adding custom CSS for forms, volunteer jobs, events, and posts.
- Headers from Wordpress theme covered page information.
  - Solved by adding custom CSS for headers that is dynamic across all devices.
- Inconsistent padding for columns, sidebars, and blog view.
  - Solved by adding custom CSS that is dynamic across all devices.
- Wordpress doesn't allow connections to and from outside the Wordpress server, so connections to the hosted database were always refused.
  - Solved by exporting database interactions to an independent, custom application.
 
## Database Application
### Frontend Development
- ReactJS
### Backend Development   
- Flask API and Python
#### API Endpoints
  

