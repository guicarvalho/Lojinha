$(document).ready(function() {
    alert('teste');
});

$("#myModal").on('hidden.bs.modal', function(){});

/*
    Busca os dados do produto no servidor via Ajax
    e monta a modal com as informações do mesmo.
*/
function montarModalProduto(slug) {
    $.ajax({
        url: 'products/json/' + slug + '/',
        type: 'GET',

        success:
            function(data) {  
                $('#modal-mini-img').empty();

                $('#modal-main-image').attr('src', data.main_image);
                $('#product-modal-title').text(data.short_description);
                $('#product-modal-description').text(data.long_description);
                $('#product-modal-price').text(parseFloat(data.sale_value) + 5);
                $('#product-modal-promotion-price').text(parseFloat(data.sale_value));
                
                $('#product-modal-link-detail').attr('href', 'products/-1/'.replace(-1, data.slug));

                for (img in data.list_images) {
                    $('#modal-mini-img').append('<img src="'+ data.list_images[img] +'" alt="" width="60" height="50" style="padding-bottom: 5px;">');
                }

                $('#myModal').modal('show');
            },
    });
}
