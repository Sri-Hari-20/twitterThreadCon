# twitterThreadCon
To generate a thread of conversation for a given tweet (through its URL) recursively till the end node and generate the output in a file, by general web scraping.

## Intention
This code is intended to generate the replies recursively till the end nodes (tweets with no further replies).

## Required Input:
Input should be of the form: "https://www.twitter.com/<user>/status/<tweetId>"

## Objective Checklist:
1. Retrieve replies for the given tweet URL (Done)
2. Write the Replies along with metadata to an csv/ xlsx file (Progress)
3. Recursive call and create hierarchial conversational thread files (Under consideration)

## Dependencies
The requirements.txt file should cover the required python packages for the functionality of the program. Use the following command after cloning.
```sudo pip install -r requirements.txt```

### Side note:
This is a side project of mine, so feel free to issue any pull requests for any module you feel can be improved.
