## Pickling Data & Exception Handling


### INTRODUCTION

There were two different topics covered this week – Pickling Data and Exception Handling. Let's start with pickling data. It can best be thought of as a way to store more complex data in a more efficient format/file for recall at a later time. Exeption handling is a way for the programmer to provide more user-centric feedback to the user when they make an error – typically in the form of data entry.


### THE PROCESS – PICKLING DATA

1. Open a new PyCharm file and enter your program’s header comments. An example of this assignment's comments can be seen below.

![image](https://user-images.githubusercontent.com/99459802/156287039-c15130d9-9b46-4297-b852-03a05ee7ff18.png)

2. We'll be working with the 'pickling' module, so let's be sure to import it into our program. Enter the code shown below.

![image](https://user-images.githubusercontent.com/99459802/156287069-d94a5ea2-c617-4500-91fb-f7a044e9ac9b.png)

3. Now let's create a couple lists of data to be pickled. For the sake of something a little different, I've used a couple bike related lists. Enter the code shown below.

![image](https://user-images.githubusercontent.com/99459802/156287102-a9aef9da-76ac-4cae-b78f-a32b9adb948d.png)

4. With our lists created, we can now pickle our data. By using the “wb” file access mode, we can let the program create our text file for us. In this case, the text file “pickledbikes” will be created in the same directory folder as our program. Each list is then 'dumped' into our text file and the file then closed. Enter the code shown below.

![image](https://user-images.githubusercontent.com/99459802/156287113-9421a7dc-3eff-48ea-99df-2ab18682b301.png)

5. Here's an example of the type of information you should see when viewing your “pickledbikes” text file. Note that much of the data is jumbled do to its binary storage.

![image](https://user-images.githubusercontent.com/99459802/156287137-ae4a15fc-1333-4d12-8256-164a1f58c24c.png)

6. It is now time to unpickle our data. We do this by against opening our text file, but we'll use the “rb” file access mode to simply read from the file. Each list is then loaded back into our program from the text file. Enter the code shown below.

![image](https://user-images.githubusercontent.com/99459802/156287162-d978d897-4e9b-4d46-a6bf-6154f94f735e.png)

7. We will now display our unpickled list data loaded in the previous step. Once printed, we close the file as it no longer required to be open. Enter the code shown below.

![image](https://user-images.githubusercontent.com/99459802/156287186-531d4440-f185-424c-ac17-738f8c6b2ec4.png)

#### Add'l resources:
- [Real Python Pickle Module Information](https://realpython.com/python-pickle-module/) – User friendly breakdown of the pickle module and its usage. Gives plenty of examples and does a good job of describing its intent and limitations.
- [Python.org Pickle Information](https://docs.python.org/3/library/pickle.html) – More in-depth technical description of the pickle module and its associated applications.


### THE PROCESS – EXCEPTION HANDLING

1. Next, we'll look at an example of exception handling. In the example below, we query the user for a number between 1 and 10. If a number outside of the range is received, the user will receive the message stating the entry is invalid. However, if they enter something other than a number, such as text, they'll be met with a statement that their entry was not a number, rather than the standard error exception message for 'ValueError'. Enter the code shown below.

![image](https://user-images.githubusercontent.com/99459802/156287203-4a31c01d-eb15-4307-ba51-4f8dee0bebbe.png)

#### Add'l resources:
- [Real Python Exeptions Information](https://realpython.com/python-exceptions/) – User friendly breakdown of exceptions and exception handling. Gives plenty of examples and does a good job of describing its intent and limitations. There's also a related course!
- [W3Schools Try/Except Information](https://www.w3schools.com/python/python_try_except.asp) – Provides clear definitions of each function and incremental examples. You can also step into the example code and make tweaks to the code to see how it affects the program.
- [Python.org Error Tutorial](https://docs.python.org/3/tutorial/errors.html) – More in-depth technical description of exception handling and errors. Also goes into more advanced exception handling technics.


### SUMMARY

The pickle module sounds like it's pretty useful for storing larger amounts of data for recall at a later time. I did manage to find some pretty useful links providing additional guidance with its applications and usage. The exception handling is a very handle tool. While general exceptions can be figured out with a bit of familiarity, having the ability to convey more user-centric feedback is handy for making sure the user if providing the data necessary to utilize the program. I need to do a bit more exploring with this particular topic.
