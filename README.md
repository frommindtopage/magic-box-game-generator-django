# Magic-Box-Game-Generator-Django
This is a Django project by which you can Generate magic box Game of any Dimension  
ℹ️ If you randomly generate n * m magic box game it is not necessarily solvable  
>  ## But `Magic-Box-Game-Generator` always produces solvable games
![demo](https://user-images.githubusercontent.com/84379558/124361676-d9d2de80-dc4d-11eb-8a66-d2c9788d851f.png)

## Requirement

First you need to install python  
than open command prompt  
__run the given code__
```bash
pip install django
```

## How to use
* inside main directory  
* click Shift + Right mouse button   
* select "Open PowerShell window here"
than run the code
```bash
python manage.py runserver
```  
![Screenshot (954)](https://user-images.githubusercontent.com/84379558/123890376-bb7e9180-d974-11eb-96d5-ef4cccb9938d.png)
* Open the main link given by "Open PowerShell window" (see image above)
* you will see a default 4*4 Magic puzzle
* You can move the block by clicking on the block or arrow keys.
#### ℹ️ `mainLink` is the link given by "Open PowerShell window" (see image above)
* if you want square magic box game of side 5
    * open the link
        *    `mainLink/?d=5`
        *    e.g. http://127.0.0.1:8000/?d=5
* if you want magic box game of dimension 5*8
    * Open given link
        *    `mainLink/?d=5*8`
        *    e.g. http://127.0.0.1:8000/?d=5*8
* d = dimension and you can't able to take number of columns and rows less than 3 and more than 10
