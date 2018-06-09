var time_slot = 1
var last = []

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
		now = msg.split("\n");
		show_table_html = "";
		for(i = 0, height = now.length; i < height; i++) {
			show_table_html += "<div class=\"row\">"
			for(j = 0, weight = now[0].length; j < weight; j++) {
	   			temp = "";
	   			if(now[i][j] == "*") temp += "alive ";
	   			if(now[i][j] == "o") temp += "dead ";
					show_table_html += "<div class = \"col-md-1\"><div class=\"cell " + temp + "\"></div></div>";
			}
			show_table_html += "</div>"
		}
		$("#table").width(now[0].length * 50);
		$("#table").html(show_table_html);
		last = now;
	});
}

$(document).ready(function(){
		$("#time_slot_click").click(function(){
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
			});
		});

		$("#input_table_click").click(function(){
			var request = $.ajax({
				url: "/new_input_table/" ,
				method: "GET" , 
				data: {input_table: $("#input_table_text").val()}, 
				dataType: "html"
			});
			request.done(function(msg){
				last = [];
				$('#inputmodal').modal('toggle');  
			});
		});
});


