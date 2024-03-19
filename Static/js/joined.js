// script.js

var globalExamId;

function isErdIdInFile(erdId, callback) {
    $.ajax({
        url: `/check_erd_id?erd_id=${erdId}`,
        method: 'GET',
        success: function(response) {
            callback(response.exists);
        },
        error: function(error) {
            console.error('Error:', error);
        },
    });
}

function fetchData() {
    if (!globalExamId) {
        console.log("Exam ID not found.");
        return;
    }

    $.ajax({
        url: `/room_management_data?exam_id=${globalExamId}`,
        method: 'GET',
        success: function(response) {
            var tableBody = $('#joined-exam-room tbody');
            tableBody.empty();
            response.data.forEach(function(item) {
                isErdIdInFile(item.erd_id, function(exists) {
                    var hideUnlock = exists ? 'style="display:none;"' : '';

                    tableBody.append(
                        `<tr>
                            <td>${item.his_id}</td>
                            <td>${item.htime}</td>
                            <td>${item.labels}</td>
                            <td>${item.erd_id}</td>
                            <td>${item.erd_id__username__username}</td>
                            <td>${item.erd_id__state}</td>
                            <td ${hideUnlock}><button onclick="writeToken('${item.erd_id}')">Unlock</button></td>
                        </tr>`
                    );
                });
            });

            if (response.data.length === 0) {
                tableBody.append('<tr><td colspan="12">No data found</td></tr>');
            }
        }
    });
}

$(document).ready(function() {
    var urlParams = new URLSearchParams(window.location.search);
    globalExamId = urlParams.get('exam_id');
    if (globalExamId) {
        fetchData();
        setInterval(fetchData, 3000); // Fetch data every 3 seconds
    }
});

function writeToken(erdId) {
    $.ajax({
        url: '/write_token',
        method: 'POST',
        data: { erd_id: erdId },
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.error('Error:', error);
        },
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
