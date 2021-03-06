#!/usr/bin/env python3
#
# aberdeen
#
"""
A static file CMS generator
"""

import sys

from .__meta__ import (
    author as __author__,
    author_email as __contact__,
    date as __date__,
    version as __version__,
    license as __license__,
    url as __homepage__,
)

from . import cli, utils

def read_config(repo_path='.'):
    from configparser import ConfigParser
    config = ConfigParser()
    config['database'] = {
        'type': 'mongodb',
        'host': 'localhost',
        'port': '27017',
        'database': 'aberdeen_blog',
        'collection': 'blog_posts'
    }

    config.read(['aberdeen.cfg'])
    return config

def call_git(args, verbose=False):
    """
    Helper function for calling a 'git' command.
    @param args: list of arguments to the git shell script.
    @return string stdout of git
    """
    from subprocess import check_output
    if isinstance(args,str):
        args = args.split()
    if verbose:
        print ("[call_git] << git ", ' '.join(args))
    res = check_output(['git'] + args)
    if verbose:
        print ("[call_git] >> {}".format(res))
    return res.decode()

def generate_from_markdown(src):
    """
    Generates a blogpost from a markdown script, src.
    @param src str: The plaintext markdown string.
    @return dict: Dictionary with header objects and 'html_content'
    """
    from termcolor2 import c
    from dateutil.parser import parse as parse_datetime
    REDERR = c('ERROR: ').red

    from markdown import Markdown
    md = Markdown(extensions=['markdown.extensions.meta'])
    html = md.convert(src)
    # copy the metadata
    res = {}
    for key, val in md.Meta.items():
        if len(val) == 1:
            # prefix lists with '@'
            if key[0] == '@':
                res[key[1:]] = val
            # special case for 'tag'
            elif key in ['tags', 'tag']:
                res[key] = val
            else:
                res[key] = val[0]
        else:
            res[key] = val

    res['raw_content'] = src
    res['html_content'] = html

    try:
        res['date'] = parse_datetime(res['date']).isoformat()
    except KeyError:
        raise Exception("    "+REDERR+"No 'date' component found in post.")
    except ValueError:
        err = "    "+REDERR+"Could not interprete 'date' value into a date."
        raise Exception(err)

    return res

def upload_posts_to_mongo(posts, cfg):
    """
    Uploads the list of items to the database as specified by the configuration
    file.
    @param posts: list of dicts containing post objects
    """
    from pymongo import MongoClient
    # from pprint import pprint
    if 'username' in cfg and 'password' in cfg:
        host = '%s:%s@%s' % map(cfg.get, ['username', 'password', 'host'])
    else:
        host = cfg.get('host', '127.0.0.1')
    mongo = MongoClient(host, int(cfg['port']), tz_aware=True)
    db_name = cfg['name']
    coll_name = cfg['post_collection']
    db = mongo[db_name]
    db[coll_name].find()
    # pprint([i for i in post_ids])
    db.drop_collection(coll_name)
    collection = db[coll_name]
    collection.insert(posts)
    # pprint(post_ids)

def upload_posts_to_database(posts, cfg):
    """
    Sends the posts to a database - determined by the configuration
    """
    if 'type' not in cfg:
        sys.stderr.write("ERROR - database type not specified in config")
        sys.exit(1)

    if cfg['type'] == 'mongodb':
        upload_posts_to_mongo(posts, cfg)
    else:
        sys.stderr.write("ERROR - unkown database type: '%s'" % (cfg['type']))
        sys.exit(1)
