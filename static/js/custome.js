$(document).ready(function () {
  $('form select').each(function () {
    if(this.id != 'id_status'){
      $(this).select2();
    }
  });
});