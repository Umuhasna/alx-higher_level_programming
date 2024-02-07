$(document).ready(function () {
  $('#btn_translate').click(getTranslate);
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      getTranslate();
    }
  });
});

function getTranslate () {
  const languageCode = $('#language_code').val();
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;
  $.get(url, function (data) {
    $('#hello').text(data.hello);
  });
}
