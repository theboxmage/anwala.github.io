import os
import http
import urllib
import requests
import sys
from boilerpipe.extract import Extractor
import glob
import socket
count = 0;
with open("links.txt", "r") as f:
    for line in f:
        count = count + 1
        try:
            extractor = Extractor(extractor='ArticleExtractor', url=line)
            s = "ParsedHTML/" + str(count) + ".txt"
            print(s + ": " + str(len(extractor.getText())))
            if len(extractor.getText()) > 0:
                with open(s, "w+") as htm:
                    print("???")
                    htm.write(extractor.getText())
        except urllib.error.HTTPError:
            pass
        except LookupError:
            pass
        except urllib.error.URLError:
            pass
        except http.client.HTTPException:
            pass
        except UnicodeDecodeError:
            pass
        except socket.timeout:
            pass
