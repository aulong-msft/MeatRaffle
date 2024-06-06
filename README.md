# Points System Application  
  
This is a simple Flask application that keeps track of points for a list of users. Users can gain points, which are represented by bacon strip images, and a user can be randomly selected as a winner, with a higher chance of winning if they have more points.  
  
## Setup  
  
1. Clone the repository to your local machine.  
2. Navigate to the project directory in your terminal.  
3. Install the required packages with `pip install -r requirements.txt`.  
4. Run the application with `python app.py`.  
  
## Usage  
- Activate the env: `.\env\Scripts\activate`
- Run the application with `python app.py`
- Add points to a user by clicking their name.  
- Reset all points with the "Reset" button.  
- Randomly select a winner with the "Draw a random winner" button.  
  
## File Structure  
  
- `app.py`: The main application file.  
- `templates/`: This directory contains the HTML templates.  
    - `index.html`: The main HTML template for the application.  
- `static/`: This directory contains static files.  
    - `bacon.jpg`: The image file for the bacon strips.  
  
## Note  
  
The image of the bacon strip is displayed in the application with a width of 20% of its original size. If you want to use a different image or size, you can replace the image file and adjust the size in the `index.html` file.  
