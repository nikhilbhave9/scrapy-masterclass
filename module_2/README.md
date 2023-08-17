# Introduction to XPath

## What is XPath?
XPath stands for XML Path Language. 
<br>
### What is XML?
XML stands for(X)Extensible Markup Langauge. The "extensible" points towards the language having non-standard or extensible markup tags. 
It is used for storing, exchanging and reconstructing data. It is both machine and human-readable, unlike other langauges. It is platform-agnostic 
It is not designed to be particularly efficient. However, if there wasn't a common consensus on a language like XML, different systems would have to write parsing algorithms/interpreters to transfer data between one another. JSON is considered a more efficient successor. 
<br>

  Coming back to XPath, it can be thought of as an alternative to the CSS selectors that are used in tools like Selectolax. For example, we would have a path such as: html/body/ul/li/span \[@class="title\]\text().
- Use downloaded cheatsheet as a resource
- Use [XPather](http://xpather.com/) to test out XPaths

## XPath Axes
XPath aces represent relations between nodes of a tree. 
1. /ancestor::nodename picks up all the parent nodes of the current node up to the root
2. 
