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
});
