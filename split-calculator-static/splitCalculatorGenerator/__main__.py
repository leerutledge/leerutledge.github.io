"""Build static HTML site from directory of HTML templates and plain files."""
from jinja2 import Template, Environment, FileSystemLoader, select_autoescape
import json
from pprint import pprint
import os
import sys
import shutil
import click

@click.command()
@click.argument('input_dir')
@click.option('--verbose/-v', is_flag=True, help='Print more output.')

def main(verbose, input_dir):
    """Top level command line interface."""
    if os.path.exists(os.path.join(input_dir, 'static')):
        if os.path.exists(os.path.join(input_dir, 'html')):
            shutil.rmtree(os.path.join(input_dir, 'html'))
        shutil.copytree(os.path.join(input_dir, 'static'),
                        os.path.join(input_dir, 'html'))
        if verbose:
            print('Copied '
                  + os.path.join(input_dir, 'static')
                  + ' -> '
                  + os.path.join(input_dir, 'html')
                  )

    try:
        with open(os.path.join(input_dir, 'config.json')) as f:
            data = json.load(f)
    except Exception:
        print('Error_JSON: failed to parse '
              + os.path.join(input_dir, 'config.json'))
        print('Current directory: ' + os.getcwd())
        return
    except IOError:
        print('Error_FileNotFound: could not find '
              + os.path.join(input_dir, 'config.json'))
        return

    template_dir = os.path.join(input_dir, 'templates')

    i = 0
    while i < len(data):
        try:
            template_env = Environment(
                loader=FileSystemLoader(template_dir),
                autoescape=select_autoescape(['html', 'xml']),
            )
            template = template_env.get_template(data[i]['template'])
            output = template.render(data[i]['context'])
        except Exception:
            print('Error_Jinja: jinja2 template ' + data[i]['template'])
            # Maybe this should be a separate exception
            print('TemplateNotFound: ' + data[i]['template'])
            sys.exit()

        if os.path.exists(os.path.join(input_dir, 'html')
                          + data[i]['url']
                          + 'index.html'):
            print('Error: output directory already contains files: %s' % os.path.join(input_dir, 'html')
                                                                         + data[i]['url']
                                                                         + 'index.html')
            sys.exit()

        if not os.path.exists(os.path.join(input_dir, 'html')
                              + data[i]['url']):
            os.makedirs(os.path.join(input_dir, 'html')
                        + data[i]['url'])

        try:
            rendered_file = open(os.path.join(input_dir, 'html')
                                 + data[i]['url']
                                 + 'index.html', 'w')
        except IOError:
            print('Error_FileNotFound: could not find '
                  + os.path.join(input_dir, 'html')
                  + data[i]['url']
                  + 'index.html')
        rendered_file.write(output)
        rendered_file.close()
        if verbose:
            print('Rendered '
                  + data[i]['template']
                  + ' -> '
                  + os.path.join(input_dir, 'html')
                  + data[i]['url']
                  + 'index.html'
                  )
        i += 1


if __name__ == "__main__":
    main()
