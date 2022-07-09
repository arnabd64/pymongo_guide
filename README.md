# PyMongo Guide

## `requests.py`

If every method in this module returns a Python `dict` in the following format:
1. If the method works correctly as expected then it should return the following message:
```json
response = {
    "error" : 0,
    "message" : "Data Requested or Any other message"
}
```
2. If the method encounters any errors/exceptions then it should return the following message:
```json
response = {
    "error" : 1,
    "message" : "Name of the Error"
}

```