#!/usr/bin/env python

from optparse import OptionParser
import bugzilla

def initialize_bugzilla(url, bug):
    """check url here """
    bz = bugzilla.Bugzilla(url=url)
    bug = bz.getbug(bug)
    return bug, bz
def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-u", "--url",
            default="https://bugzilla.suse.com",
            type="string",
            help="specify bugzilla url")
    parser.add_option("-n", "--bugnumber",
                      default=False,
                      type='string',
                      help="bugzilla number",)
    (options, args) = parser.parse_args()

    if len(args) != 0:
        parser.error("wrong number of arguments")

    bug, bz = initialize_bugzilla(options.url, options.bugnumber)
    print bug


if __name__ == '__main__':
    main()
