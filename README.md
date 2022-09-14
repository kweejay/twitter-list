# twitter-list
Python script to make Twitter list from a list of handles.

# How to use

## Set up API keys.
Make sure to have access to the Twitter API. If you don't, these are the steps to set it up:
1. Go to https://developer.twitter.com/en and head to the Developer Portal.
2. Go to Project & Apps located on the left-hand side of the screen.
3. Click on the button "+ Create App".
4. Name the app and click "Complete".
5. Once you have created the app, Twitter will give you an API key, an API secret key, and a Bearer token.
6. In the same directory as the make_list.py file, create a text file.
7. Format it like so:
![image](https://user-images.githubusercontent.com/109972744/190273683-9c2d86a5-4544-422c-9517-13de9dfd02de.png)
8. Copy the API key in the quotation marks for CONSUMER_KEY, API secret key for CONSUMER_SECRET_KEY, and Bearer token for BEARER_TOKEN.
9. Save it as a ".env" file and leave the file open because you will be filling the other quotes in.
10. In the App details page, under User authentication settings, click on the "Edit" button next to User authentication set up.
11. In this page, change App permissions to "Read and write", click on "Native App" on Type of App, and fill in "https://ngrok.com" for the Callback URI and Website URL under App info.
12. Save your changes, and this will generate a new API key and API secret key.
13. Enter these generated keys into ACCESS_TOKEN and ACCESS_TOKEN_SECRET, respectively. The CLIENT_ID and CLIENT_SECRET are given to you once this process is done, so fill those in as well.

## Use the script.
2 things are needed for the program to work. The list ID number for your Twitter list, and a .csv file that contains all the URLs for the users that you want to add into the list.

The list ID is located in the URL of the Twitter list.

![image](https://user-images.githubusercontent.com/109972744/190275425-2e12322a-19fc-4fc5-8512-7b0d34a58ac5.png)

The second is a .csv file for the users that you would like to add to the list. Either make a text file and separate each URL with commas and save it as a .csv like so:

![image](https://user-images.githubusercontent.com/109972744/190275770-c95152db-5b9f-48fb-8866-f31a6e035ee5.png)

Or create a .csv file on a spreadsheet.

![image](https://user-images.githubusercontent.com/109972744/190276255-a6c8e4d5-2614-47bf-bf68-beaabfb81e9e.png)

Then just run the script with python.

Usage: make_list.py [-h] list_id /path/to/csv

Example:

![image](https://user-images.githubusercontent.com/109972744/190276636-fb32c108-ebe3-42d8-834f-75556b47c9b0.png)

![image](https://user-images.githubusercontent.com/109972744/190277020-f80c4912-a5e0-40c5-8be3-0d4523cc8685.png)



