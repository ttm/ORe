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
#L=r.Literal
def L(data, datatype=None,lang=None):
    if datatype and lang:
        return r.Literal(data, datatype=datatype,lang=lang)
    elif datatype:
        return r.Literal(data, datatype=datatype)
    elif lang:
        return r.Literal(data, lang=lang)
    else:
        return r.Literal(data)

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
def ID_GEN(namespace,tid):
    ind=namespace+"#"+tid
    G(ind,ns["rdf"].type,namespace)
    return ind



pe.namespaces=namespaces


ns=namespaces=pe.namespaces(["rdf","rdfs","owl","xsd", # basic namespaces
                          "aa","ot","opa","ops","ore", "obs","vbs","ocd", # participatory namespaces
                          "dcterms","dc", # useful Dublincore Metadata
                            ("wsg","http://www.w3.org/2003/01/geo/wgs84_pos#"), # georeferencing
                            ("sioc","http://rdfs.org/sioc/ns#"), # online communities
                            ("tsioc","http://rdfs.org/sioc/types#"), # sioc types 
                            ("schema","http://schema.org/") # umbrella
                          ])

# Info about ORe
#g.add((ouri,dct.description,r.Literal(u"Ontologia do Participa.br, levantada com base nos dados e para conectar com outras instâncias")))
G(      ns["ore"].data0+".rdf",
        ns["dcterms"].description,
        L("ORe (Ontology of the Research) initial triplestore (0)",lang="en")
        #L("Ontology of the Research (ORe), with focus on media, learning, agenda, and processes description",lang="pt")
    )

# Add Individuals, Literals, etc.
G(    ID_GEN(ns["ore"].Doubt,"meteor1"),
      ns["ore"].description,
      L("What are the differences between meteor packages, platform, sdk and project? What are the available options?",lang="en")
    )

G(    ID_GEN(ns["ore"].Doubt,"meteor2"),
      ns["ore"].description,
      L("What are the right tools for navigating RDF in meteor/javascript such as in pubby? Should whis be done by hand by loading RDF, starting from a class or overview and loading appropriate predicates and objects for a selected class?",lang="en")
)
G(    ID_GEN(ns["ore"].Idea,"suck_data"),
      ns["ore"].description,
      L("Put a suck my data button on the skin, by which a person can login via FB, TW, email, etc to have its data sucked",lang="en")
)
G(    ns["ore"].ProgResource,
      ns["rdfs"].subClassOf,
      ns["ore"].Resource,
)
# creates a uri using the resource path and adds it as an individual of that path:
turi=ID_GEN(ns["ore"].ProgResource,"semantic_web_tools")
G(turi,ns["ore"].qualification,L("para programação",lang="pt"))
G(turi,ns["ore"].qualification,L("javascript",lang="pt"))

G(    ID_GEN(ns["ore"].Id,"name"),
      ns["ore"].description,
      L("Renato Fabbri",datatype=ns["xsd"].string)
  )

G(    ID_GEN(ns["ore"].Id,"usualID"),
      ns["ore"].description,
      L("rfabbri",datatype=ns["xsd"].string)
  )

G(ns["ore"].Nick,
        ns["rdfs"].subClassOf,
        ns["ore"].Id)

G(    ID_GEN(ns["ore"].Nick,"rfabbri"),
      ns["ore"].description,
      L("rfabbri",datatype=ns["xsd"].string)
  )

G(    ID_GEN(ns["ore"].Nick,"hybrid"),
      ns["ore"].description,
      L("hybrid",datatype=ns["xsd"].string)
  )
nicks=("blober","hercules","tatoman","greenkobold","ttm")
for nick in nicks:
    G(    ID_GEN(ns["ore"].Nick,nick),
          ns["ore"].description,
          L(nick,datatype=ns["xsd"].string)
      )

G(ns["ore"].Birthdate,
        ns["rdfs"].subClassOf,
        ns["ore"].Id)

G(    ID_GEN(ns["ore"].Birthdate,"birth"),
      ns["ore"].description,
      L("19/Out/1982",datatype=ns["xsd"].dateTime)
  )

G(ns["ore"].Pick,
        ns["rdfs"].subClassOf,
        ns["ore"].Id)

turi=ID_GEN(ns["ore"].Pick,"1")
G(    turi,
      ns["ore"].url,
    L("https://dl.dropboxusercontent.com/u/22209842/fotosImagens/Webcam-1384027461.png",datatype=ns["xsd"].anyURI),
  )

G(    turi,
      ns["ore"].qualification,
    L("no neck",lang="en")
  )

G(    turi,
      ns["ore"].qualification,
    L("strange",lang="en")
  )
turi=ID_GEN(ns["ore"].Pick,"2")
G(    turi,
      ns["ore"].url,
    L("https://dl.dropboxusercontent.com/u/22209842/fotosImagens/Webcam-1390391951.png",datatype=ns["xsd"].anyURI),
  )
G(    turi,
      ns["ore"].qualification,
    L("funny, strange eye, show off",lang="en")
  )
turi=ID_GEN(ns["ore"].Pick,"3")
G(    turi,
      ns["ore"].url,
    L("https://dl.dropboxusercontent.com/u/22209842/fotosImagens/28042014.png",datatype=ns["xsd"].anyURI),
  )
G(    turi,
      ns["ore"].qualification,
    L("ok",lang="en")
  )
turi=ID_GEN(ns["ore"].Pick,"4")
G(    turi,
      ns["ore"].url,
    L("https://dl.dropboxusercontent.com/u/22209842/fotosImagens/2011-09-02-023637__.png",datatype=ns["xsd"].anyURI),
  )
G(    turi,
      ns["ore"].qualification,
    L("freak",lang="en")
  )
ore=ns["ore"]; xsd=ns["xsd"]
turi=ID_GEN(ore.Milestone,"thesisDeposit")
G(turi,ore.level,L(100,xsd.integer))
G(turi,ore.description,L("deposit thesis",0,"en"))
G(turi,ore.dueDate,L("15/Dec/2015",xsd.dateTime))

turi=ID_GEN(ore.Milestone,"finishArticles")
G(turi,ore.level,L(100,xsd.integer))
G(turi,ore.description,L("deliver final versions of articles",0,"en"))
G(turi,ore.dueDate,L("27/Out/2015",xsd.dateTime))

turi=ID_GEN(ore.Milestone,"finishSoftware")
G(turi,ore.level,L(100,xsd.integer))
G(turi,ore.description,L("deliver final versions of software",0,"en"))
G(turi,ore.dueDate,L("15/Nov/2015",xsd.dateTime))

turi=ID_GEN(ore.Milestone,"finishAudiovisualizations")
G(turi,ore.level,L(100,xsd.integer))
G(turi,ore.description,L("deliver final versions of audiovisualizations",0,"en"))
G(turi,ore.dueDate,L("15/Nov/2015",xsd.dateTime))

turi=ID_GEN(ore.Milestone,"thesisDefense")
G(turi,ore.level,L(100,xsd.integer))
G(turi,ore.description,L("thesis defense",0,"en"))
G(turi,ore.dueDate,L("15/Fev/2016",xsd.dateTime))

turi=ID_GEN(ore.Milestone,"thesisReview")
G(turi,ore.level,L(100,xsd.integer))
G(turi,ore.description,L("deliver thesis review",0,"en"))
G(turi,ore.dueDate,L("15/Apr/2016",xsd.dateTime))

turi=ID_GEN(ore.Milestone,"thesisAdvisorReview")
G(turi,ore.level,L(100,xsd.integer))
G(turi,ore.description,L("deliver thesis for review by the advisor",0,"en"))
G(turi,ore.dueDate,L("15/Nov/2016",xsd.dateTime))

turi=ID_GEN(ore.Milestone,"FinishDoctorate")
G(turi,ore.level,L(200,xsd.integer))
G(turi,ore.description,L("finish doctare process",0,"en"))
G(turi,ore.dueDate,L("15/Mai/2016",xsd.dateTime))

rdfs=ns["rdfs"]
G(ore.Milestone,rdfs.comment,L("a goal that consists of other minor milestones or tasks. A milestone should usually take at least one day.",0,"en"))
# Deriving ontoloty naturally, this can be commented off as
# our data driven ORe will present this relations
#G(ore.level,rdfs.range,xsd.integer)
#G(ore.task,rdfs.range,ore.Milestone)
#G(ore.task,rdfs.range,ore.Task)

G(ore.Task,rdfs.comment,L("a simple task without subdivisions a priori.",0,"en"))

tmil=ID_GEN(ore.Milestone,"oreStart")
G(tmil,ore.description,L("write first operating version of ORe to be confortable enough for next task",xsd.string))
G(tmil,ore.dueDate,L("26/Set/2015",xsd.dateTime))
G(tmil,ore.level,L(10,xsd.integer))

tmil=ID_GEN(ore.Milestone,"orePercolate")
G(tmil,ore.description,L("write first operating version of ORe to be confortable enough for next task",xsd.string))
G(tmil,ore.dueDate,L("26/Set/2015",xsd.dateTime))
G(tmil,ore.level,L(7,xsd.integer))

tmil=ID_GEN(ore.Milestone,"cssBeta")
G(tmil,ore.description,L("make first betas for ccs presentation",xsd.string))
G(tmil,ore.dueDate,L("26/Set/2015",xsd.dateTime))
G(tmil,ore.level,L(10,xsd.integer))

talg=ID_GEN(ore.Algorithm,"obsSynth")
G(talg,ore.description,L("triplification facilities for rapid specificationi. Created in the RDF representation of the Brazilian Decree 8.243 (PNPS) conceptualization.",0,"en"))
G(talg,ore.url,L("https://github.com/ttm/vocabulario-participacao/blob/master/scripts/obsPNPS.py",xsd.anyURI))

G(talg,ore.derivedResource,ore.Resource+"#Percolation")
G(talg,ore.url,L("https://github.com/ttm/vocabulario-participacao/blob/master/scripts/obsPNPS.py",xsd.anyURI))
ot=ns["ot"]
G(ot.base+"#Ontology",ore.prototypeOf,ore.base+"#Ontology")
G(ot.base+"#Ontology",ore.prototypeOf,ore.base+"#Framework")

G(talg,ore.derivedResource,ore.Resource+"#Percolation")
G(talg,ore.url,L("https://github.com/ttm/vocabulario-participacao/blob/master/scripts/obsPNPS.py",xsd.anyURI))



f=open("rdf/oreFirstTriplestore.rdf","wb")
f.write(g.serialize())
f.close()
f=open("rdf/oreFirstTriplestore.ttl","wb")
f.write(g.serialize(format="turtle"))
f.close()
##########################################
#### TTM
"""
sys.exit()

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


