import rdflib as r

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
        tpick=I(tclass="PICK",tid=mkid("PICK")
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

tmilestone=C(tclass="Milestone",tid=mkid("Milestone"))
G(tmilestone,"level",10)
G(tmilestone,"description","make first betas for ccs presentation")
G(tmilestone0,ore.nextTask,tmilestone)



