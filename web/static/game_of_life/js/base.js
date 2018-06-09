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
		show_table_html = ""
		for(i = 0, len = now.length; i < len; i++) {
			show_table_html += "<div class=\"line\">"
			for(j = 0, len = now.length; j < len; j++) {
	   			cell = now[i][j];
	   			temp = ""
	   			if(JSON.stringify(last) != '[]' && now[i][j] != last[i][j]) temp += "changed ";
	   			if(now[i][j] == "*") temp += "alive ";
	   			if(now[i][j] == "o") temp += "dead ";
					show_table_html += "<div class = \"container\"><div class=\"cell " + temp + "\"></div></div>";
			}
			show_table_html += "</div>"
		}
		console.log(show_table_html);
		$("#table").html(show_table_html);
//		anime({targets: '.changed', scale: 1.2, easing: 'easeOutExpo'});
//		anime({targets: '.changed', scale: 1, easing: 'easeOutExpo'});
		last = now;
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


