import rdflib as r, pygraphviz as gv, sys
import  importlib
from IPython.lib.deepreload import reload as dreload
import percolation as pe
#importlib.reload(g.loadMessages)
#importlib.reload(g.listDataStructures)
#importlib.reload(g.interactionNetwork)
#importlib.reload(pe.linkedData)
##dreload(pe,exclude="pytz")
#dreload(pe)

g = r.Graph()
def G(S,P,O):
    g.add((S,P,O))
L=r.Literal

def namespaces(ids=[]):
    """Declare namespace URIs in RDF graph and return a dictionary of them.
    
    input: list of ids. Use tuple for (idstring, URIString) of
    benefint from RDFLib and particpatory IDs 
    throughtput: declare RDF in graph g
    output: dictionary of {key=id, value=URI} as declared
    
    Deals automaticaly with namespaces from RDFlib and selected
    participatory libs"""
    idict={}
    for tid in ids:
        # findig URIRef 
        if type(tid)!=type("fooString"): # tuple (tid,iuri)
            idict[tid[0]]=r.Namespace(tid[1])
        elif tid in [fooString.lower() for fooString in dir(r.namespace)]: # rdflib shortcut
            if tid in dir(r.namespace):
                idict[tid]=eval("r.namespace."+tid)
            else:
                idict[tid]=eval("r.namespace."+tid.upper())
        else: # participatory shortcut
            idict[tid]=r.Namespace("http://purl.org/socialparticipation/{}/".format(tid))
        # adding to RDF Graph
        if type(tid)!=type("fooString"): # tuple (tid,iuri)
            g.namespace_manager.bind(tid[0], idict[tid[0]])    
        else:
            g.namespace_manager.bind(tid, idict[tid])    
    return idict


pe.namespaces=namespaces

namespaces=pe.namespaces(["rdf","rdfs","owl","xsd", # basic namespaces
                          "aa","ot","opa","ops","ore", "obs","vbs","ocd", # participatory namespaces
                          "dcterms","dc", # useful Dublincore Metadata
                            ("wsg","http://www.w3.org/2003/01/geo/wgs84_pos#"), # georeferencing
                            ("sioc","http://rdfs.org/sioc/ns#"), # online communities
                            ("tsioc","http://rdfs.org/sioc/types#"), # sioc types 
                            ("schema","http://schema.org/") # umbrella
                          ])



##########################################
#### TTM
"""
sys.exit()
import rdflib as r, pygraphviz as gv, sys
import  importlib
from IPython.lib.deepreload import reload as dreload
import percolation as pe

URI="http://purl.org/socialparticipation/ore/"
# redirect to rfabbri.meteor.com/navigate/
# example:
# "http://purl.org/socialparticipation/ore/Pick/1" to:
# redirect to http://rfabbri.meteor.com/navigate/Pick/1
# and
# "http://purl.org/socialparticipation/ore/Pick" to:
# redirect to http://rfabbri.meteor.com/navigate/Pick
# showing all picks.

# study possibility of using something already working
# or pubby

# sequência de triplas:
T=[("Doubt","doubt","What are the differences between meteor packages, platform, sdk and project? What are the available options?"),
("Doubt","doubt","What are the right tools for navigating RDF in meteor/javascript such as in pubby? Should whis be done by hand by loading RDF, starting from a class or overview and loading appropriate predicates and objects for a selected class?"),
"ProgResource","url","http://www.w3.org/wiki/SemanticWebTools",
"ProgResource","a","Resource",
"ProgResource","qualification",L("para programação","pt"),
"ProgResource","qualification",L("javascript","pt"),
        "IDS","name","Renato Fabbri",
        "IDS","usualID","rfabbri",
        "IDS","nick","rfabbri",
        "IDS","nick","hybrid",
        "IDS","nick","blober",
        "IDS","nick","hercules",
        "IDS","nick","tatoman",
        "IDS","nick","greenkobold",
        "IDS","pseudonyms","Various manly for music, code and literature",
        "IDS","birthdate","19/Out/1982",
        tpick=I(tclass="PICK",tid=mkid("PICK"),
        "IDS","pick",tpick,
        tpick,P("url"),L("https://dl.dropboxusercontent.com/u/22209842/fotosImagens/Webcam-1384027461.png"),
        tpick,P("qualification"),L("no neck"),
        tpick,P("qualification"),L("strange"),

        tpick=I(tclass="PICK",tid=mkid("PICK")
        "IDS","pick",tpick,
        tpick,P("url"),L("https://dl.dropboxusercontent.com/u/22209842/fotosImagens/Webcam-1390391951.png"),
        tpick,P("qualification"),L("funny"),
        tpick,P("qualification"),L("strange eye"),
        tpick,P("qualification"),L("show off"),

        tpick=I(tclass="PICK",tid=mkid("PICK")
        "IDS","pick",tpick,
        tpick,P("url"),L("https://dl.dropboxusercontent.com/u/22209842/fotosImagens/28042014.png"),
        tpick,P("qualification"),L("ok"),

        tpick=I(tclass="PICK",tid=mkid("PICK")
        "IDS","pick",tpick,
        tpick,P("url"),L("https://dl.dropboxusercontent.com/u/22209842/fotosImagens/2011-09-02-023637__.png"),
        tpick,P("qualification"),L("freak"),
        ]
##
tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",100)
G(tmilestone,"description","deposit thesis")
G(tmilestone,"dueDate","15/Dec/2015")


tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",100)
G(tmilestone,"description","deliver final versions of articles")
G(tmilestone,"dueDate","27/Out/2015")


tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",100)
G(tmilestone,"description","deliver final versions of software")
G(tmilestone,"dueDate","15/Nov/2015")


tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",100)
G(tmilestone,"description","deliver final versions of audiovisualizations")
G(tmilestone,"dueDate","15/Nov/2015")

tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",100)
G(tmilestone,"description","thesis defense")
G(tmilestone,"dueDate","15/Fev/2015")


tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",100)
G(tmilestone,"description","final thesis review")
G(tmilestone,"dueDate","15/Abr/2015")

tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",100)
G(tmilestone,"description","deliver thesis for advisor review")
G(tmilestone,"dueDate","15/Nov/2015")

toverlay=C("MilestoneOverlay")
tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",200)
G(tmilestone,"description","Finish doctorate process")

C("Milestone",rdf.description,"a goal that consists of other minor milestones or tasks. A milestone should usually take at least one day."
P("level",rdf.description,"a milestone level: higher level milestones consist of lower level milestones and tasks.")
P("level",rdf.range,int)

C("Task",rdf.description,"a simple task without subdivisions a-priori.")

P("Milestone","task",("Milestone","Task"))

tmilestone0=tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",10)
G(tmilestone,"description","write first operating version of ORe to be confortable enough for next task")
G(tmilestone,"dueDate","26/Set/2015")

tmilestone0=tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",7)
G(tmilestone,"description","Integrate percolation python package to ORe in the making of the RDF")
G(tmilestone,"dueDate","26/Set/2015")

tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",10)
G(tmilestone,"description","make first betas for ccs presentation")
G(tmilestone0,ore.nextTask,tmilestone)

#############
## Resources

talg=C(tclass="Algorithm",tid=mkid("Algorithm"))
G(talg,"description","triplification facilities for rapid specificationi. Created in the RDF representation of the Brazilian Decree 8.243 (PNPS) conceptualization.")
G(talg,ore.project,ore.Resource.Percolation)
#G(talg,ore.derivedProject,"Percolation")
G(talg,ore.derivedResource,ore.Resource.Percolation)
G(talg,"url","https://github.com/ttm/vocabulario-participacao/blob/master/scripts/obsPNPS.py")

G(ore.ot,ore.prototypeOf,ore)


#############
## Hand-on tasks and milestones



"""


