#!/usr/bin/python

from jinja2 import Template
result_tab = "teddy"


def generate_site(nanimos, parties):

    try:
        template = open("template-membre.sfdl.j2", "r").read()
    except IOError:
        print("File sfdl not found")
        exit(1)

    for nanimo in nanimos:
        for partie in parties:
            tplt = Template(template)
            result = tplt.render({"nanimo": nanimo, "partie": partie})
            result_file = open("{}-{}-{}.fsdl".format(result_tab, nanimo, partie), 'w')
            result_file.write(result)
            result_file.close()

if __name__ == '__main__':
    nanimos = ["lapin", "ours"]
    tete = ["casquette", "chapeau"]
    haut = ["chemine", "t-shirt"]
    bas = ["short", "pentalon"]
    generate_site(nanimos, tete)
    generate_site(nanimos, haut)
    generate_site(nanimos, bas)
