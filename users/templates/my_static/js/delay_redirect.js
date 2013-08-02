
$(document).ready(function() {
    var timer = $.timer(function() {
        var url = $("#redirect-url").attr('rel');
        window.location = url;
        // django_js_utils.urls.resolve('my-accounts', { pk: 1})
    });
    timer.set({ time : 1500, autostart : true });
});

// $.post(dutils.urls.resolve('time_edit', { project_id: 1, time_id: 2 }), ...

