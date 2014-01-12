import logging
import sys
import locale
import mimetypes
import os
from hsaudiotag import auto
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.compat import xmlrpc_client

def main(argv):
    logfile = os.path.join(os.path.expanduser("~"),os.path.split(argv[0])[1] + ".log")
    logging.basicConfig(filename=logfile,level=logging.DEBUG)
    h2 = logging.StreamHandler(sys.stderr)
    logging.getLogger().addHandler(h2)
    try:
        filename = argv[1]
        mimetypes.init()
        logging.info("Audio Uploader")
        logging.info("--------------")
        logging.info("File selected for upload:")
        logging.info("%s" % (filename))
        logging.info("Destination:")
        logging.info("%s@%s" % (argv[3],argv[2]))
        logging.info("")
        logging.info("Retrieving metadata...")
        myfile = auto.File(argv[1])
        logging.info("---------------------------------------------------------------------")
        logging.info("Artist:\t\t%s" % myfile.artist)
        logging.info("Album:\t\t%s" % myfile.album)
        logging.info("Title:\t\t%s" % myfile.title)
        logging.info("Comment:\t%s" % myfile.comment.replace("\n","\n\t\t"))
        logging.info("---------------------------------------------------------------------")
        logging.info("Connecting to WordPress...")
        wp = Client(argv[2], argv[3], argv[4])
        logging.info("...done")

        logging.info("Encoding file for upload...")
        data = {
            'name': os.path.split(filename)[1],
            'type':mimetypes.guess_type(filename)
            }
        with open(filename, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())
        logging.info("...done")

        logging.info("Uploading media...")
        response = wp.call(media.UploadFile(data))
        logging.info("...done")
        
        logging.info("Creating post...")
        titleStyle = 'style="border: 2px solid #a1a1a1; padding: 5px 10px; background: #ddddff; border-radius: 10px;"'
        linkStyle = 'style="border: 2px solid #a1a1a1; color: #ffffff; padding: 5px 5px; background: #0000ff; border-radius: 10px;"'
        post = WordPressPost()
        post.title = "<div " + titleStyle + "> [Audio] " + myfile.title + "</div>"
        content = "<h2>" + myfile.artist + "</h2>"
        content = content + "<p>" + myfile.title + '</p>'
        if myfile.comment != "":
            content = content + '<p>' + myfile.comment + '</p>'
        content = content + '<a ' + linkStyle + ' href="' + response['url'] + '">Click to download</a>'
        post.content = content
        post.terms_names = {
            'category': ['Audio']
            }
        wp.call(NewPost(post))
        logging.info("...done")
    except Exception as e:
        logging.exception(e)
        return 99
    else:
        return 0

if __name__ == "__main__":
    exit(main(sys.argv))
