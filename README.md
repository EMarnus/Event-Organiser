# Create an event

### [Live Website](https://bar-match-bookings-site-929e26b7b02a.herokuapp.com/)

A community wesite to organise gaming events/times.  
The objective of this is to provide a simple site to try to organise gaming events among friends. These days it's difficult to get my gaming group together to play something as we all have resposibilities this is an attempt to make getting together easier.    

[Features/Planning Board](https://github.com/users/EMarnus/projects/4/views/1)  
[Initial Mockup](./assets/images/initial%20wireframe.PNG)  
[Responsive Mockup](./assets/images/Am%20I%20responsive.PNG)

## Features 

### Existing Features

- __The Header bar__

  - Featured at the top of the page, the title introduces the subject content, reinforced by the header image.
  - The users name, set by the user and stored using local API.
  - The score system is a simple increment for a correct answer, on clicking check answer.

- __The Game Area__

  - This section is the main focus of the page and where the action happens.
  - The area starts with a haiku and once the game is started the text is replaced with a question and 4 answers.
  - Also contains a counter for the question you are on out of total questions.

- __Adding Factions__
<ol>
  <li>Create a json file in the format of the others, need all key pairs in order.</li>
  <li>Search in script.js for *Add New Faction* and add/update</li>
  <li>Add a label and input for it in HTML under id="checkboxes"</li>
  <li>Test and despair</li>
</ol>

### Features Left to Implement

- More question sets, based on faction and expand question selection.
- •	Multiple hero images based on the question.
- A weighted scoring system.
- A hint system.
- Redesign, not enough Gothic horror.
- New question validation for json files.

## Testing 

Ongoing testing on Chrome as features were added. Additional Testing was done desktop Edge, Firefox & Mobile Chrome. Manual testing was done for edge cases, that is how infinite score, no checkbox selected and reset game bugs were found.

[Incognito Lighthouse](./assets/images/Incognito%20Lighthouse.PNG)

### Validator Testing 

- HTML
    - Needed to fix some p elements and a legend element to pass [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Femarnus.github.io%2FWarhammer40kQuiz%2F)
- CSS
    - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Femarnus.github.io%2FWarhammer40kQuiz%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JavaScript
    - No errors were found when passing through the official [Jshint validator](https://jshint.com/)
      - The following metrics were returned: 
      - There are 24 functions in this file.
      - Function with the largest signature take 1 arguments, while the median is 0.
      - Largest function has 22 statements in it, while the median is 2.5.
      - The most complex function has a cyclomatic complexity value of 11 while the median is 1.

### Unfixed Bugs
- Updating Events broke after adding previously submitted dates as default. 
- Pagination doesn't work, just keeps flowing down.
- The desctiption on booking-submit is not dynamic depending on type selected.


### Fixed Bugs
- 
- 


## Deployment

- The site was deployed using Heroku: 
  - In heroku Create a new App
  - In your new App go to settings and reveal Config Vars, add your variables from env.py as well as PORT: 8000
  - Make sure your repo contains a Procfile
  - Go to Deply, select GitHub as the Deployment method, Deploy Branch from Main.


## Credits 
- Can Sucullu - Mentor at Code Institute
- Codemy.com - [Django Wednesdays Playlist](https://bit.ly/35Xo9jD)
- CI's I think Therefore I Blog - Used project as a base template for my site

### Content 


### Media

- 
- 