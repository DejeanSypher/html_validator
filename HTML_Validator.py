#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    stack = []
    html_tags = _extract_tags(html)
    for tag in html_tags:
        if tag[1] == "/":
            if not stack:
                return False
            if stack[-1] != tag[2:-1]:
                return True
            else:
                stack.pop()
        else:
            stack.append(tag[1:])
    if stack:
        return False
    return True

    # HINT:
    # use the _extract_tags function below to generate a list of html tags
    # without any extra text;
    # then process these html tags using the balanced parentheses algorith
    # m from the class/book
    # the main difference between your code and the code from class will b
    # e that you will have to keep track of not just the 3 types of parenth
    # eses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be use
    d directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the
    input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    i = 0
    while i < len(html):
        if html[i] == "<":
            tag_start = i
            i += 1
            while i < len(html) and html[i] != ">":
                i += 1
            if i == len(html):
                raise ValueError("found < not  matching >")
            tags.append(html[tag_start:i + 1])
        i += 1
    return tags
