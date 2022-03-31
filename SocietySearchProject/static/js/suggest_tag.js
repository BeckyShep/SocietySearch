$(document).ready(function() {

    $.fn.updatePreview = function() {
        var tagText = $('#exampleFormControlTextarea1').val();
        var tagCol = $('#cPicker').val();
        var steamAppId = $('#sAppID').val();

        $('#preview-tag').css('background-color', tagCol);
        $('#preview-tag').text(tagText);
        $('#preview-steam').attr('href', "" + steamAppId);
    }
    $('#suggest-form').on('keyup change paste', ':input', function() {
        $.fn.updatePreview();
    });

    $('.edit-tag').click(function() {

        var tagInfo = $(this).closest('tr').children('td') // get list of items in this row
        var tagColText = tagInfo.get(0).id;

        var tagCol = tagColText.substring(0, 7);
        var tagText = tagColText.substring(7, );

        var tagSteamAppId = tagInfo.get(1).id;

        var tagIsGame = tagInfo.get(3).id;

        console.log(tagCol);
        console.log(tagText);
        console.log(tagSteamAppId);
        console.log(tagIsGame);

        $('#exampleFormControlTextarea1').val(tagText);
        $('#cPicker').val(tagCol);
        $('#sAppID').val(tagSteamAppId);
        $('#gTag').prop('checked', tagIsGame === "True");

        $.fn.updatePreview();
    });


});