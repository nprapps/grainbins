$(function() {
    var $window = $(window);
    var $card_section = $('#cards');
    var $cards = $('.card');
    var $top_spacer = $('#top-spacer');
    var $bottom_spacer = $('#bottom-spacer');

    var card_y_offset = $card_section.offset()[1];
    var card_count = $cards.length;
    var active_card = 0;
    var $active_card = $($cards[0]);
    var $next_card = $($cards[1]);

    $active_card.show();
    $next_card.show();

    var card_height = $active_card.height();
    $card_section.height(card_height);

    var cards_height = card_height * card_count;
    $bottom_spacer.height(cards_height);

    function card_section_scrolled(ev) {
        var y = $card_section.scrollTop();

        new_active_card = Math.floor(y / card_height);

        if (active_card != new_active_card) {
            $active_card.hide();
            $next_card.hide();
            active_card = new_active_card;
        
            $next_card.css({ 'margin-top': '0px' });

            $active_card = $($cards[active_card]);
            $next_card = $($cards[active_card + 1]);

            $active_card.show();
            $next_card.show();
        }

        var offset = y - (y % card_height);

        $top_spacer.height(offset);
        $next_card.css({ 'margin-top': (-card_height + (y % card_height)) + 'px' });
        $bottom_spacer.height(cards_height - offset);
    }

    $card_section.scroll(card_section_scrolled);
});
