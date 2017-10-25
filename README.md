# HouseProxy
Protect your parents from phishing, HTTP proxy focused on block phishing URL's

# Install
<pre>
git clone https://github.com/mthbernardes/HouseProxy.git
cd HouseProxy/
pip install -r requeriments.txt
</pre>

# Config
<pre>
Edit etc/HouseProxy.conf to change de default user and password
Create a entry in your DNS to house.proxy
</pre>

# Usage
<pre>
$ hug -f index.py
$ sudo echo "localhost  house.proxy" >> /etc/hosts
Set the house.proxy:3128 as your proxy
Open the browser and access http://house.proxy:8000
Click in update blacklists It my take a while, the tool is downloading
blacklists from phishitank and openphish.
Done, now just try to access a malicious URL.
</pre>

# Usage recomendation
<pre>
Install it on a raspberry pi, create a network,
force all http traffics to pass through the pi on 3128 port (transparent proxy),
and connect the clients to this network
</pre>

[![HouseProxy Usage](youtube.png)](https://youtu.be/19bZr2VNTdo)
