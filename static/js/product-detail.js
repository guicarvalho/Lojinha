(function($) {
    'use strict';

    var _private = {
        queries: {
            fields: {
                bigImage: $('#big-image'),
                thumbnailImage: $('.img-thumbnail')
            },
            containers: {
                image: $('#gallery')
            }
        }
    };

    function ProductDetail() {
        var _this = this;
        _this.init();
    };

    ProductDetail.prototype.init = function() {
        var _this = this;
        _this.registerElevateZoom();
    };

    ProductDetail.prototype.registerElevateZoom = function() {
        var config = {
            gallery: 'gallery',
            galleryActiveClass: 'active',
            responsive: true
        };

        // Initiate the plugin and pass id of the div containing gallery images
        _private.queries.fields.bigImage.elevateZoom(config);
    };

    return new ProductDetail();
})(jQuery);
