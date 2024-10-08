# Introduction to XPath

## What is XPath?
XPath stands for XML Path Language. 
<br>
### What is XML?
XML stands for(X)Extensible Markup Langauge. The "extensible" points towards the language having non-standard or extensible markup tags. 
It is used for storing, exchanging and reconstructing data. It is both machine and human-readable, unlike other langauges. It is platform-agnostic 
It is not designed to be particularly efficient. However, if there wasn't a common consensus on a language like XML, different systems would have to write parsing algorithms/interpreters to transfer data between one another. JSON is considered a more efficient successor. 
<br>
### XPaths
  Coming back to XPath, it can be thought of as an alternative to the CSS selectors that are used in tools like Selectolax. For example, we would now use a path such as: html/body/ul/li/span \[@class="title\]\text().
- Use downloaded cheatsheet as a resource
- Use [XPather](http://xpather.com/) to test out XPaths

## XPath Axes
XPath aces represent relations between nodes of a tree. 
1. <b>/ancestor::nodename[n]</b> picks up all the ancestor nodes of the current node up to the root.  
2. <b>/parent::nodename</b> matches only the immediate ancestor of the current node. No need for [1] here as it is redundant
3. <b>/child::nodename</b> matches only the immediate descendant of the current node.
4. <b>//</b> is simply an abbreviation of the descendant axis
5. <b>node/following::nodename</b> This will exclude the current node but match whatever follows (from its sibling onward)
6. <b>currnode/following-sibling::nodename</b> This will match ONLY if the matched nodes have the same parent as the current node
7. <b>/preceding</b> same as following; for any level match. Will start from the bottom-most if multiple copies. 
8. <b>/preceding-sibling</b> same as following-sibling; only for match with same parent.

- Use downloaded cheatsheet as a resource
