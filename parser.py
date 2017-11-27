#!/usr/bin/env /usr/bin/python3

import yaml, sys
from jinja2 import Template
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--template", dest="templateFile",
                  type="string", action="store",
                  help="template file to parse")
parser.add_option("-p", "--params", dest="paramsFile",
                  type="string", action="store",
                  help="YAML parameters file")
parser.add_option("-s","--stage", dest="stage",
                  type="string", action="store",
                  help="parameters 'stage'")

(options, noise) = parser.parse_args()

if len(sys.argv) != 7 or len(noise) > 0:
    parser.print_help()
else:
    with open(options.paramsFile) as parameters:
        parameters = yaml.load(parameters)
    with open(options.templateFile) as template:
        template = Template(template.read())

    print(template.render(parameters[options.stage],ENV=options.stage))
