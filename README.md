This project was created to automate user actions and collect advertisements from armenian news website https://www.azdarar.am/. Here was used automation testing pattern such as PageObjects.

To sent search results to an email, you need to create ui/tests/secrets.json and put there an access token:
```
{
  "from_email": "your_email@gmail.com",
  "token": "access token",
  "to_email": "recipient_email"
}
```


## Run the project
How to build and run the project

Ensure you have Git and Python3 installed
 
Clone the project 
```bash
git clone https://github.com/XeniaBerkut/azdarar.git
```
Go to the directory
```bash
cd azdarar/
```
### Run the project via installing environment and requirements

Create virtual python environment
```bash
virtualenv venv
```
Activate virtual python environment
```bash
source venv/bin/activate
```
Install all the requirements
```bash
pip install -r requirements.txt
```
Export Python path
```bash
export PYTHONPATH=ui:$PYTHONPATH
```
Run test
```bash
pytest ui/tests/test_search_advertisements.py
```