$(function() {
    var $states = $('.filter-state'); 
    var $cards = $('.card');
    
    $states.click(function() {
        var state = $(this).data('state');

        if (state == 'ALL') {
            $cards.show();
        } else {
            $cards.hide();
            $cards.filter('.state-' + state).show();
        }

        $states.removeClass('active');
        $(this).addClass('active');
    });

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
