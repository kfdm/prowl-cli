import optparse
import subprocess
import logging

import pushnotify


def main():
    parser = optparse.OptionParser(usage='usage: %prog [options] <command...>')
    parser.disable_interspersed_args()
    parser.add_option('-a', '--application', default='Prowl')
    parser.add_option('-k', '--api-key')
    parser.add_option('-e', '--event', default='Message')

    parser.add_option(
        '-c', '--client', type='choice', default='prowl',
        choices=['nma', 'prowl']
    )
    parser.add_option('-p', '--priority')
    parser.add_option('-u', '--url')

    parser.add_option(
        "-v", "--verbose",
        action='store_const',
        const=logging.INFO,
        default=logging.WARNING)

    (opts, args) = parser.parse_args()

    logging.basicConfig(level=opts.verbose)

    if opts.api_key is None:
        try:
            opts.api_key = subprocess.check_output([
                'defaults', 'read', 'net.weks.prowl', 'apikey'
            ]).strip()
        except:
            parser.parser_error('Error reading API key')

    if not len(args):
        parser.parse_error('Missing message')

    client = pushnotify.get_client(opts.client, application=opts.application)
    client.add_key(opts.api_key)
    kwargs = {}
    if opts.priority:
        kwargs['prority'] = opts.priority
    if opts.url:
        kwargs['url'] = opts.url
    client.notify(' '.join(args), opts.event, split=True, kwargs=kwargs)
