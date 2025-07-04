#  TechStax: GitHub Webhook Receiver 

This project listens to GitHub repository webhook events — specifically **Push**, **Pull Request**, and optionally **Merge** — and stores those in a MongoDB database. It includes a simple UI that polls for updates every 15 seconds.

---

#  Insatllation
```bash

git clone https://github.com/AdarshBelnekar/webhook-repo.git
```
## Create Virtual Environment
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate     # For Linux/Mac
# OR
venv\Scripts\activate        # For Windows
```
##  Install Dependencies
```bash
pip install -r requirements.txt
```
## Configure .env
```bash
MONGO_URI=mongodb://localhost:27017/webhook_db
```
## Start the Flask Server
```bash
python run.py
```
## GitHub Webhook Setup
**Go to your action-repo on GitHub.**

Navigate to Settings → Webhooks → Add Webhook.

Set:

Payload URL: http://your-ngrok-url/webhook/receiver

Content-Type: application/json

Events: Select:

Push

Pull requests

Click Add Webhook.

# Author
Build by Adarsh Belnekar



