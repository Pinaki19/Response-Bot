# Response-Bot

This project aims to automate the response filling in google forms.

First Read the dependencies then check out the Setup.txt file If you want to continue.
---------------------------------------------------------------------------------------------------------------------------------------------------------------
This project has certain dependencies:
  You can only use G-form with this.
  The form must allow more than one response from one user.
  The form must not require sign in to submit response.
  The form should not have any other text field except a Email and a Name Field.(Not having any or both is OK!!).
  The email field should be of type="email" and not a text question, else response will be "Others".
  If the form has more text fields. all of them will be filled with the text "Others".
  The form should not contain any other type of question except of type 1. Multiple choice or 2. Check-box type.
  Filling of other types of questions are currently not supported.
  You can ask it to fill any number of responses but if the form requires a name field then you must provide that many names
  You can ask chatgpt to provide you the names, in the required format.
  If the form has  a Email field and you want to provide the mails you can. Else the emails will be auto generated by the Name that you provide.
  Further you can provide less number of mails than the number of names, the rest of the mails will be auto generated by their name.
  The matching of Names and Mails are index based. I.e. the 1st name will be used with the 1st mail and so on.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  If you see selenium content not interactable Error, increase the driver.implicitly_wait(x) time which is 'x' here.

  Now read the Setup file.
  
