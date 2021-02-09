# rd-dl
A quick and dirty CLI downloader for Real-Debrid  

**NOTE**: I don't use this anymore, it's super broken and buggy.  
My current solution is clicking "View generated links" on the RD site and running those links through aria2, it's an extra step but much easier and cleaner.

## Usage

Input your API Key from https://real-debrid.com/apitoken in the "API_KEY" variable inside the script  
Install requirements with `pip3 install -r requirements.txt`

Run `python3 rd-dl.py <url>` or `python3 rd-dl.py <.txt file containing urls>`
