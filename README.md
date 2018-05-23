
## Pip Requirements

There are only a few requirements but you will have to create a python-env, virtualenv or conda env environment in order to do the installation of the required files.  I like virtualenv for something small.  So `$ virtualenv venv` and then do `$ source venv/bin/activate`.  Once you have activated your environment you can do the pip install `pip install -r requirements.txt`.

For both the worker computers and main computer you will need to activate the above environment.

## Redis Broker

You will need to have access to a Redis server for the task message passing.  On my Mac, I went to `https://redis.io/download`, downloaded it, untarred and compiled.  Then ran it using `redis-server` in the appropriate directory.

## Worker Computers

For test purposes this can be run on your local computer.  So, in this directory you can just run `sh runme_workers`.

Alternatively, you could copy this repo onto a remote machine and just run the same `sh runme_workers` (don't forget to setup and activate a virtual environment).

## Distribution computer

Then on your local computer you want to activate your environment and then type:

```
$ python runme.py
```

