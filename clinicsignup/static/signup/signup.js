// $('#appointmentDate').pickadate()


// $('#appointmentTime').pickatime({
// //    format: 'h:i',
//     formatlabel: '<b>h</b>:i',
//     formatSubmit:'HH:i',
//     hiddenPrefix: 'prefix__',
//     hiddenSuffix: '__suffix',
//     disable: [
// 	new Date(2016,3,20,4,30),
// 	new Date(2016,3,20,9)
//     ],
// })


// $(document).load(function() {


// $(document).ready(function() {
//     $.get("/disabled/", function(data, status) {
// 	console.log("GET performed");
// 	alert("data:" + data + "\nstatus:" + status);
// 	console.log("after alert");
//     });
// });
 




//$('#datepicker').datepicker();

// $('#timepicker').timepicker({
//     minTime: new Date(0,0,0,9,0,0),
//     maxTime: new Date(0,0,0,18,0,0)
// });


var array = ["2016-03-14","2015-03-15","2015-03-16"]
$('#datepicker').datepicker({
    beforeShowDay: function(shmate){
	var string = jQuery.datepicker.formatDate('yy-mm-dd', shmate);
	return [ array.indexOf(string) == -1 ];
    }
});


window.show = true;

disabled = [
    ['9am', '10am'],
]    

$('#timepicker').timepicker({
    'timeFormat':'H:i',
    'minTime':'9:00am',
    'maxTime':'6:00pm',
    'disableTimeRanges': disabled,
});
