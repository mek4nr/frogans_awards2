#!/usr/bin/python

from jinja2 import Template
result_tab = "teddy"


def generate_site(nanimos, parts):

    try:
        template = open("template-membre.fsdl.j2", "r").read()
    except IOError:
        print("File sfdl not found")
        exit(1)

    for nanimo in nanimos:
        for p in parts:
            tplt = Template(template)
            index_part = parts.index(p)
            index_next = parts[(index_part + 1) % len(parts)]
            index_prev = parts[(index_part - 1)]
            # print("prev={} index={} next={}".format(index_prev, index_part, index_next))
            result = tplt.render({"nanimo": nanimo, "part": p,
                                  "previous": index_prev,
                                  "next": index_next})
            result_file = open("{}-{}-{}.fsdl".format(result_tab, nanimo, p), 'w')
            result_file.write(result)
            result_file.close()

if __name__ == '__main__':
    nanimos = ["rabbit"]
    head = ["blank", "glass1", "glass2", "hat1", "hat2"]
    body = ["blank", "dress1", "tshort1"]
    generate_site(nanimos, head)
    generate_site(nanimos, body)
