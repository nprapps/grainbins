$(function() {
    var $cards = $('.card');
    var $state_hdr = $('.state-filters').find('h4');
    var $state_btns = $('#filter-state-buttons');
    var $state_drop = $('#filter-state-dropdown');
    var $state_drop_sel = $state_drop.find('select');
    var $states = $('.filter-state');

//    var max_bar_amt = 1624000;
    var max_bar_amt = 1650000;
    var max_bar_amt_display = '$1.65 million';
//    var reset_max_bar_amt = 555000;
    var reset_max_bar_amt = 600000;
    var reset_max_bar_amt_display = "$600,000";
    
    // state filters
    $states.click(function() {
        filter_state($(this).data('state'));
    });
    $state_drop.on('change', function(e) {
    	filter_state(e.target.value);
    });
    function filter_state(state) {
        if (state == 'ALL') {
            $cards.show();
        } else {
            $cards.hide();
            $cards.filter('.state-' + state).show();
        }

		$states.removeClass('active');
		$('#state-btn-' + state).addClass('active'); // highlight the button for desktop
		$state_drop_sel.val(state); // select the dropdown item for mobile
        
        $state_hdr.removeClass('active');
    	$state_btns.removeClass('active');
    }
    
    // css classes to show/hide only defined for mobile view
    $state_hdr.click(function() {
    	$state_hdr.toggleClass('active');
    	$state_drop.toggleClass('active');
    });

    // size the bars
    $bars = $('#cards').find('.bar');
    $($bars).each(function() {
    	var this_amt = parseInt($(this).attr('data-amt'));
    	if (!isNaN(this_amt)) {
			var $axis_label = $(this).parents('.fines').find('.axis-label').find('span');
    		var parent_id = $(this).parents('.card').attr('id');
    		var this_width;

    		if (parent_id == 'steven-lee-mc-laughlin-sd' || parent_id == 'cody-rigsby-wiley-co') {
				this_width = (this_amt/max_bar_amt) * 100;
				$axis_label.empty().append(max_bar_amt_display);
			} else {
				this_width = (this_amt/reset_max_bar_amt) * 100;
				$axis_label.empty().append(reset_max_bar_amt_display);
			}
    		$(this).width(this_width + '%');
    	}
    });
});
