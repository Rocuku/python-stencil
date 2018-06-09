var time_slot = 1

window.onload = function() {
	setTimeout("timedCount()",time_slot * 1000);
}


function timedCount() {
	show();
    timer_device = setTimeout("timedCount()", time_slot * 1000);	
}


function show(){
	var request = $.ajax({
		url: "/show_table/" ,
		method: "GET" , 
		data: {}, 
		dataType: "html"
	});
	request.done(function(msg){
		$("#table").html(msg);
	});
}

$(document).ready(function(){
		$("#time_slot_click").click(function(){
			console.log($("#time_slot_text").val());
			time_slot = $("#time_slot_text").val();
		});

		$("#random_table_click").click(function(){
			var request = $.ajax({
				url: "/new_random_table/" ,
				method: "GET" , 
				data: {}, 
				dataType: "html"
			});
			request.done(function(msg){
				$('.alert').html('重置成功！').addClass('alert-success').show().delay(1500).fadeOut();
			});
		});
	
});