var myChart5;
var myChart6;
(function ($) {
    "use strict";
    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });


    // Progress Bar
    $('.pg-bar').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Calender
    $('#calender').datetimepicker({
        inline: true,
        format: 'L'
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: true,
        loop: true,
        nav : false
    });
    
    $.ajax({   // Chart for room manager 
        url: '/report_on_exam', 
        type: 'GET',
        success: function(data) {
            var selectedValue = globalExamId; // This would be the selected value from your urls
                
            // Check if the selected value exists in the "exam_name" array
            var selectedIndex = data.exam_id.indexOf(selectedValue);
            // Single Bar Chart
            var ctx5 = $("#bar-chart").get(0).getContext("2d");
            myChart5 = new Chart(ctx5, {
                type: "bar",
                data: {
                    labels: ["Normal", "Abnormal"],
                    datasets: [{
                        label: data.exam_id[selectedIndex],
                        backgroundColor: [
                            "rgba(0, 156, 255, .7)",
                            "rgba(255, 0, 0, .6)"
                        ],
                        data: [data.number_of_normal[selectedIndex], data.number_of_abnormal[selectedIndex]]
                    }]
                },
                options: {
                    responsive: true,
                }
            });

            // Real-time change on status
            var ctx6 = $("#multi-line2").get(0).getContext("2d");
            // Define the duration in minutes (replace this with your variable)
            const duration = data.duration[selectedIndex];
            // Create an array to store each minute
            const minuteArray = [];
            // Iterate through each minute and add it to the array
            for (let minute = 0; minute <= duration; minute++) {
                minuteArray.push(minute);
            }

            myChart6 = new Chart(ctx6, {
                type: "line",
                data: {
                    labels: minuteArray,
                    datasets: [{
                            label: "Normal",
                            data: data.number_of_normal_time_series[selectedIndex],
                            backgroundColor: "rgba(0, 156, 255, .5)",
                            fill: true
                        },
                        {
                            label: "Abnormal",
                            data: data.number_of_abnormal_time_series[selectedIndex],
                            backgroundColor: "rgba(255, 0, 0, .3)",
                            fill: true
                        }
                    ]
                    },
                options: {
                    responsive: true
                }
            });
            // Initial call to update charts
            updateExamRoomChart();
            // Call updateCharts every 5 seconds (adjust as needed)
            // setInterval(updateExamRoomChart, 2000);
        }
    });



})(jQuery);

function updateExamRoomChart() {
    $.ajax({   
        url: '/report_on_exam', 
        type: 'GET',
        success: function(data) {
            var selectedValue = globalExamId;
            var selectedIndex = data.exam_id.indexOf(selectedValue);

            // Update Bar Chart
            myChart5.data.datasets[0].data = [data.number_of_normal[selectedIndex], data.number_of_abnormal[selectedIndex]];

            // Update Line Chart
            myChart6.data.datasets[0].data = data.number_of_normal_time_series[selectedIndex];
            myChart6.data.datasets[1].data = data.number_of_abnormal_time_series[selectedIndex];

            // Update both charts
            myChart5.update();
            myChart6.update();
        },
        error: function(xhr, status, error) {
            console.error("Error fetching data:", error);
        }
    });
}

// script.js
var globalExamId;
var fetchDataInterval;

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

    var tableBody = $('#joined-exam-room tbody');

    // Attach click event to table body (parent element)
    tableBody.on('click', '.unlock-btn', function(e) {
        e.preventDefault(); // Prevent the default link behavior

        // Extract his_id and erd_id from the clicked button's ID
        var ids = $(this).attr('id').split('+');
        var his_id = ids[0];
        var erd_id = ids[1];

        // Perform AJAX request
        $.ajax({
            url: `/unlock_jiuhduigaiugyueihdg19y7e61hdtg76badr56n816nb2t5c7ecne8t72nd?his_id=${his_id}&erd_id=${erd_id}`,
            method: 'GET',
            success: function(response) {
                // Handle success if needed
                console.log('Unlock successful');
            },
            error: function(error) {
                // Handle error if needed
                console.error('Error unlocking:', error);
            }
        });
    });

    // Original AJAX request for fetching data
    $.ajax({
        url: `/room_management_data?exam_id=${globalExamId}`,
        method: 'GET',
        success: function(response) {
            tableBody.empty();
            console.log(response.data);
            response.data.forEach(function(item) {
                isErdIdInFile(item.erd_id, function(exists) {
                    tableBody.append(
                        `<tr>
                            <td>${item.his_id}</td>
                            <td>${item.erd_id}</td>
                            <td>${item.htime}</td>
                            <td>${item.erd_id__username__username}</td>
                            <td>${item.labels}</td>
                            <td>${item.abnormal_count}</td>
                            <td>${item.erd_id__state}</td>
                            <td><a class="btn btn-sm btn-primary unlock-btn" id="${item.his_id}+${item.erd_id}" href="#">Unlock</a></td>
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

function show_history() {
    clearInterval(fetchDataInterval);  // Clear the interval to stop fetching data

    $.ajax({
        url: `/showall/${globalExamId}/`,
        method: 'GET',
        data: { exam_id: globalExamId },
        success: function(response) {
            var tableBody = $('#joined-exam-room tbody');
            tableBody.empty();
            response.data.forEach(function(item) {
                console.log(item)
                isErdIdInFile(item.erd_id, function(exists) {
                    var hideUnlock = exists ? 'style="display:none;"' : '';

                    tableBody.append(
                        `<tr>
                            <td>${item.his_id}</td>
                            <td>${item.erd_id}</td>
                            <td>${item.htime}</td>
                            <td>${item.erd_id__username__username}</td>
                            <td>${item.labels}</td>
                            <td>${item.abnormal_count}</td>
                            <td>${item.erd_id__state}</td>
                            <td><a class="btn btn-sm btn-primary" href="#">Unlock</a></td>
                        </tr>`
                    );
                });
            });

            if (response.data.length === 0) {
                tableBody.append('<tr><td colspan="12">No data found</td></tr>');
            }
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });
}

$(document).ready(function() {
    var urlParams = new URLSearchParams(window.location.search);
    globalExamId = urlParams.get('exam_id');
    if (globalExamId) {
        fetchData();
        fetchDataInterval = setInterval(fetchData, 3000);
        setInterval(updateExamRoomChart, 3000);
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
