$('#formLogin').submit(function(e) {
    login();
    e.preventDefault();
});

function login() {
    $.ajax({
        url: 'login/',
        type: 'POST',
        data: $("#formLogin").serialize(),

        success:
            function(data) {
                $('#btnCloseModal').trigger('click');
                $('#AjaxMessages').empty();
                $('#AjaxMessages').append('<p class="alert alert-'+ data.level +'">'+ data.message +'</p>');

                if (data.level == 'success') {
                    window.location = '/';
                }
            },
        error:
            function(textStatus, errorThrow) {
                var object = $.parseJSON(textStatus.responseText);

                if (object.username != undefined) {
                    $('#textUsernameError').text(object.username[0]);
                }

                if (object.password != undefined) {
                    $('#textPasswordError').text(object.password[0]);
                }
            }
    });
}
