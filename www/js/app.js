$(function() {
    var context = $.extend(APP_CONFIG, {
        'template_path': 'jst/example.html',
        'config': JSON.stringify(APP_CONFIG, null, 4)
    });

    var html = JST.example(context);

    $('#template-example').html(html);
    
    
    // size the bars
    $bars = $('#cards').find('.bar');
    $($bars).each(function() {
    	var max_amt = 1600000;
    	var this_amt = parseInt($(this).attr('data-amt'));
    	if (!isNaN(this_amt)) {
    		var this_width = (this_amt/max_amt) * 100;
    		$(this).width(this_width + '%');
    	}
    });
});
