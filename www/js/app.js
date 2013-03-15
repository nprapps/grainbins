$(function() {
    var $cards = $('.card');
    var $state_hdr = $('.state-filters').find('h4');
    var $state_btns = $('#filter-state-buttons');
    var $state_drop = $('#filter-state-dropdown');
    var $state_drop_sel = $state_drop.find('select');
    var $states = $('.filter-state');

    // state filters
    $states.click(function() {
        filter_state($(this).data('state'));
    });
    $state_drop_sel.on('change', function(e) {
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
    	$state_drop.removeClass('active');
    }
    
    // css classes to show/hide only defined for mobile view
    $state_hdr.click(function() {
    	$state_hdr.toggleClass('active');
    	$state_btns.toggleClass('active');
    	$state_drop.toggleClass('active');
    });
});
