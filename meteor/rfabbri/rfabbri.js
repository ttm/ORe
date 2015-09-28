InStuff = new Mongo.Collection("in-stuff");
Router.route('/stuff');
Router.route('/ccs');
Router.route('/slide/:_id/:_id2',function (){
	this.render('slide'+this.params._id+this.params._id2);
});

Router.route('/slide/:_id',function (){
	this.render('slide'+this.params._id);
});
Router.route('/', {
	    template: 'home'
});

if (Meteor.isClient) {
  // counter starts at 0
  Session.setDefault('counter', 0);
  Session.set("tstatus","Nothing input by you yet")

  Template.stuff.helpers({
	  stuffs: function () {
		  return InStuff.find({},{sort: {createdAt: -1}}); // ???
	  }

  });

  Template.hello.helpers({
    counter: function () {
      return Session.get('counter');
    },
	  tstatus: function (){
	      return Session.get('tstatus');
	  }
  });

  Template.hello.events({
    'click button': function () {
      // increment the counter when button is clicked
      Session.set('counter', Session.get('counter') + 1);
    }
  });
  Template.hello.events({
	  "submit .new-task": function (event) {
		  // Prevent default browser form submit
		  event.preventDefault();
		  var text = event.target.text.value;
		  console.log(text)
		  InStuff.insert({
			  text: text,
			  createdAt: new Date() // current time
		  });
  		  Session.set("tstatus",text);
		  // Clear form
		  event.target.text.value = "";
	  },
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
