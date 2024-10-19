$(document).ready(function(){
    var listOfElements = $('select[id^="id_product_features-"][id$="-feature"]');
    $(listOfElements).on('change', function() {
        var f_id = $(this).val();
        var dd1 = $(this).attr('id');
        var dd2 = dd1.replace("-feature", "-filter_value");

        $.ajax({
            type: 'GET',
            url: "/products/ajax_admin/?feature_id=" + f_id,
            success: function(res){
                cols = document.getElementById(dd2);
                cols.options.length = 0;
                for (var k in res) {
                    cols.options.add(new Option(k, res[k]));
                }
            }
        });
    });
});