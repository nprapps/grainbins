$(function() {
    var $cards = $('.card');
    var $state_hdr = $('.state-filters').find('h4');
    var $state_btns = $('#filter-state-buttons');
    var $states = $('.filter-state');

    var max_bar_amt = 1600000; // per @stiles
    
    // state filters
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
        
        $state_hdr.removeClass('active');
    	$state_btns.removeClass('active');
    });
    
    // css classes to show/hide only defined for mobile view
    $state_hdr.click(function() {
    	$state_hdr.toggleClass('active');
    	$state_btns.toggleClass('active');
    });

    // size the bars
    $bars = $('#cards').find('.bar');
    $($bars).each(function() {
    	var this_amt = parseInt($(this).attr('data-amt'));
    	if (!isNaN(this_amt)) {
    		var this_width = (this_amt/max_bar_amt) * 100;
    		$(this).width(this_width + '%');
    	}
    });
});
