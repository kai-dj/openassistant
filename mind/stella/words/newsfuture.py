#!/usr/bin/env python

import subprocess
import feedparser
import string

rss = feedparser.parse('https://www.reddit.com/r/Futurology/.rss')

print(rss['feed']['title'])

subprocess.call("echo reading futurology news... | $VOICE", shell=True)

for post in rss.entries:
  headline = post.title
  exclude = set(string.punctuation)
  headline = ''.join(ch for ch in headline if ch not in exclude)
  subprocess.call("echo \"" + headline + "\n\" | tee /dev/tty | $VOICE", shell=True)

