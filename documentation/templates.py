import subprocess

# result from bash script that collected all templates and their dependencies
all_templates = subprocess.getoutput("./html_templates.sh")


# inhttps://www.ups.com/track?loc=en_US&rplates
# manipulate this string to get data needed
class AllTemplates:
    def __init__(self, temple_str):
        self.template_str = temple_str
        self.template_dic = self.get_dic_templates(temple_str)

    def get_templare_str(self):
        return self.template_str

    def get_template_dic(self):
        return self.template_dic

    # create dictionary from input string
    # separators between parent child is = and between templates ;
    # need to index of -2 bc split() gives empty string as last item int the list
    def get_dic_templates(self, words):
        templates = {}
        print(words)
        words = words.split(";")[:-2]
        for template in words:
            template = template.split("=")
            template_name = template[0]
            if len(template) == 1:
                template_dependency = " "
            template_dependency = template[1]
            templates.update({template_name: template_dependency})
        return templates

    # get only

    # get dict of parent templates files
    def get_parent(self):
        all_parents = []
        for template in self.template_dic:
            all_parents.append(template)
        return all_parents


template_maker = AllTemplates(all_templates)
y = template_maker.get_template_dic()
print(y)
