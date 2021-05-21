$( "#bar_png" )
    .filter( ":odd" )
    .hide()
    .end()
    .filter( ":even" )
    .hover(function() {
        $( this )
            .toggleClass( "active" )
            .next()
            .stop( true, true )
            .slideToggle();
    });

