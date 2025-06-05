/* =============================== */
/* ========== All Pages ========== */
/* =============================== */

/* ===== Header Dropdowns ===== */
$('.header-dropdown-link > a').click(function(e) {
    e.preventDefault();
    var link = $(this).parent();
    var dropdown = link.find('.header-dropdown');
    link.toggleClass('expand');
    if (link.hasClass('expand')){
        dropdown.css("display","block");
        $(this).attr("aria-expanded", "true");
    }
    else {
        dropdown.css("display","none");
        $(this).attr("aria-expanded", "false");
    }
    link.siblings('.header-dropdown-link').removeClass('expand').find('.header-dropdown').css("display","none");
});
