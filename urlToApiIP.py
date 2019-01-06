def converter(url):
    #url is a string which is of the form "https://twitter.com/i/web/status/1062065617547812864"
    url = url[20 :]
    ID = url[-19 :]
    url = url[: -19]
    url = url[: -8]
    user = url
    return user, ID


if __name__ == "__main__":
    user, ID = converter("https://twitter.com/indiannavy/status/1063471004717117440")
    print("User in the link: " + user)
    print("ID in the link: " + ID)