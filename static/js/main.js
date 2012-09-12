/* Author: Michael Mulich with the Connexions Project */

require.config({
    paths:{
        // Core plugins:
        domReady:'libs/require-plugins/domReady',
        text:'libs/require-plugins/text',
        // Third-party libraries:
        bootstrap:'libs/bootstrap.min',
        mustache:'libs/libs/mustache',
        // Custom application code:
        templates:'templates',
        datasource:'datasource'
    },
    shim:{
        'bootstrap':['jquery'],
    }
});

require(['jquery', 'datasource', 'templates', 'bootstrap',
         'domReady!'],
        function ($, datasource, templates) {
            $('.dropdown-toggle').dropdown();
        });
